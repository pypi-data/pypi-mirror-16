from __future__ import division
import hashlib
import json
import random
import shutil
import urllib
import os
from pprint import pprint

import math
import numpy as np
import sys

import requests
from PIL import Image

from aetros.utils import get_option
from network import ensure_dir

from threading import Thread, Lock
from Queue import Queue

def download_image(url, path):
    if os.path.exists(path):
        return True

    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                return True
        else:
            print("Could not download image %s, response %d" % (url, r.status_code))
    except Exception as e:
        print("Could not download image %s due to %s" % (url, e.message))

    return False

class ImageDownloaderWorker(Thread):
    def __init__(self, q, trainer, dataset, max, images, controller):
        Thread.__init__(self)
        self.q = q
        self.trainer = trainer
        self.dataset = dataset
        self.max = max
        self.images = images
        self.controller = controller

    def run(self):
        try:
            while self.controller['running']:
                self.handle(self.q.get())
                self.q.task_done()
        except KeyboardInterrupt:
            self.controller['running'] = False
            return

    def handle(self, message):
        image = message[0]

        if 'id' not in image:
            return

        local_name = image['id']
        local_image_path = '%s/%s' % (self.trainer.job_model.get_dataset_downloads_dir(self.dataset), local_name)

        try:
            ensure_dir(os.path.dirname(local_image_path))
        except Exception:
            pass

        if not os.path.isfile(local_image_path):
            if download_image(image['src'], local_image_path):
                try:
                    img = Image.open(local_image_path)
                    resize = bool(get_option(self.dataset['config'], 'resize', True))
                    if resize:
                        os.remove(local_image_path)
                        size = (int(get_option(self.dataset['config'], 'resizeWidth', 512)), int(get_option(self.dataset['config'], 'resizeHeight', 512)))
                        quality = int(float(get_option(self.dataset['config'], 'resizeCompression', 0.8)) * 100)
                        img.thumbnail(size, Image.ANTIALIAS)

                        local_image_path = os.path.splitext(local_image_path)[0]+'.jpg'
                        img.save(local_image_path, 'JPEG', quality=quality, optimize=True)
                except IOError as e:
                    print("No valid image found %s" % (local_image_path,))
                    os.remove(local_image_path)
                except KeyboardInterrupt:
                    self.controller['running'] = False

        self.images[image['id']] = local_image_path
        self.trainer.set_status('LOAD IMAGE %d/%d' % (len(self.images), self.max))

def read_image(path, size, target_shape, grayscale=False, dim_ordering=None):
    if dim_ordering is None:
        import keras.backend
        dim_ordering = keras.backend.image_dim_ordering()

    try:
        image = Image.open(path)
    except:
        return None

    # do not only resize, maintain aspect ratio
    image = image.resize(size, Image.ANTIALIAS)

    if grayscale:
        image = image.convert("L")
    else:
        image = image.convert("RGB")

    image = np.asarray(image, dtype='float32')

    if len(target_shape) > 1:
        # RGB: height, width, channel -> channel, height, width
        if grayscale:
            if dim_ordering == 'th':
                image = image.reshape((1, size[0], size[0]))
            else:
                image = image.reshape((size[0], size[0], 1))
        else:
            if dim_ordering == 'th':
                image = image.transpose(2, 0, 1)
    else:
        # L: height, width => height*width
        image = image.reshape(size[0] * size[1])

    return image

# class to read all images in the ram at once
class ImageReadWorker(Thread):
    def __init__(self, q, trainer, path, grayscale, size, images, controller):
        Thread.__init__(self)
        self.q = q
        self.trainer = trainer
        self.path = path
        self.grayscale = grayscale
        self.size = size
        self.images = images
        self.controller = controller

    def run(self):
        while self.controller['running']:
            self.handle(self.q.get())
            self.q.task_done()

    def handle(self, message):
        path, validation, category_dir = message

        try:
            if os.path.isfile(path):
                image = read_image(path, self.size, self.trainer.input_shape, grayscale=self.grayscale)
            else:
                return

            if image is None:
                return

            self.images.append([image, validation, category_dir])
        except IOError as e:
            self.trainer.logger.write('Could not open %s due to %s' % (path, e.message))
            return

class InMemoryDataGenerator():
    def __init__(self, datagen, images, classes_count, batch_size):
        self.index = -1
        self.datagen = datagen
        self.images = images
        random.shuffle(self.images)
        self.lock = Lock()

        self.classes_count = classes_count
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def next(self):
        batch_x = []
        batch_y = []

        for i in range(self.batch_size):

            with self.lock:
                self.index += 1
                # reset iterator if necessary
                if self.index == len(self.images):
                    self.index = 0
                    random.shuffle(self.images)

            image, class_idx = self.images[self.index]
            image = np.copy(image) # we need to copy it, otherwise we'd operate on the same object again and again

            if self.datagen is not None:
                image = self.datagen.random_transform(image)
                image = self.datagen.standardize(image)
            else:
                image /= 255.0

            batch_x.append(image)

            y = np.zeros((self.classes_count,), dtype='float32')
            y[class_idx] = 1.
            batch_y.append(y)

        return np.array(batch_x), np.array(batch_y)


def read_images_in_memory(job_config, dataset, node, trainer):
    """
    Reads all images into memory and applies augmentation if enabled
    """
    from keras.utils import np_utils
    concurrent = 6

    dataset_config = dataset['config']
    controller = {'running': True}
    config = dataset['config']
    q = Queue(concurrent)

    size = (node['width'], node['height'])

    if node['inputType'] == 'image':
        trainer.input_shape = (1, size[0], size[1])
        grayscale = True
    elif node['inputType'] == 'image_rgb':
        grayscale = False
        trainer.input_shape = (3, size[0], size[1])
    else:
        trainer.input_shape = (size[0] * size[1],)
        grayscale = True

    result = {
        'X_train': [],
        'Y_train': [],
        'X_test': [],
        'Y_test': []
    }

    images = []
    max = 0

    path = trainer.job_model.get_dataset_downloads_dir(dataset)
    if 'path' in dataset['config']:
        path = dataset['config']['path']

    classes_count = 0
    category_map = {}
    classes = []

    try:
        for i in range(concurrent):
            t = ImageReadWorker(q, trainer, path, grayscale, size, images, controller)
            t.daemon = True
            t.start()

        for validation_or_training in ['validation', 'training']:
            if os.path.isdir(path+'/'+validation_or_training):
                for category_name in os.listdir(path+'/'+validation_or_training):
                    if os.path.isdir(path+'/'+validation_or_training+'/'+category_name):

                        if category_name not in category_map:
                            category_map[category_name] = classes_count
                            if 'category_' in category_name:
                                category_idx = int(category_name.replace('category_', ''))
                                category_map[category_name] = category_idx
                                target_category = dataset_config['classes'][category_idx]
                                classes.append(target_category['title'] or 'Class %s' % (category_idx, ))
                            else:
                                classes.append(category_name)

                            classes_count += 1

                        for id in os.listdir(path+'/'+validation_or_training+'/'+category_name):
                            file_path = os.path.join(path, validation_or_training, category_name, id)
                            q.put([file_path, validation_or_training == 'validation', category_name])
                            max += 1

        q.join()
        controller['running'] = False

        train_images = []
        test_images = []

        for v in images:
            image, validation, category_dir = v
            if validation is True:
                test_images.append([image, category_map[category_dir]])
            else:
                train_images.append([image, category_map[category_dir]])

        train_datagen = None
        augmentation = bool(get_option(dataset_config, 'augmentation', False))
        if augmentation:
            train_datagen = get_image_data_augmentor_from_dataset(dataset)
        train = InMemoryDataGenerator(train_datagen, train_images, classes_count, job_config['settings']['batchSize'])

        test = InMemoryDataGenerator(None, test_images, classes_count, job_config['settings']['batchSize'])

        nb_sample = len(train_images)
        trainer.set_generator_training_nb(nb_sample)
        trainer.set_generator_validation_nb(len(test_images))

        print ("Found %d classes, %d images (%d in training [%saugmented], %d in validation). Read all images into memory from %s" %
               (classes_count, max, len(train_images), 'not ' if augmentation is False else '', len(test_images), path))
        pprint(category_map)

        trainer.output_size = classes_count
        trainer.set_job_info('classes', classes)
        trainer.classes = classes

        result['X_train'] = train
        result['Y_train'] = train
        result['X_test'] = test
        result['Y_test'] = test

        return result

    except KeyboardInterrupt:
        controller['running'] = False
        sys.exit(1)

def get_image_data_augmentor_from_dataset(dataset):
    from keras.preprocessing.image import ImageDataGenerator
    dataset_config = dataset['config']

    augShearRange = float(get_option(dataset_config, 'augShearRange', 0.1))
    augZoomRange = float(get_option(dataset_config, 'augZoomRange', 0.1))
    augHorizontalFlip = bool(get_option(dataset_config, 'augHorizontalFlip', False))
    augVerticalFlip = bool(get_option(dataset_config, 'augVerticalFlip', False))
    augRotationRange = float(get_option(dataset_config, 'augRotationRange', 0.2))

    return ImageDataGenerator(
            rescale=1./255,
            rotation_range=augRotationRange,
            shear_range=augShearRange,
            zoom_range=augZoomRange,
            horizontal_flip=augHorizontalFlip,
            vertical_flip=augVerticalFlip
    )

def read_images_keras_generator(job_config, dataset, node, trainer):
    from keras.preprocessing.image import ImageDataGenerator

    size = (node['width'], node['height'])

    if node['inputType'] == 'image':
        trainer.input_shape = (1, size[0], size[1])
        grayscale = True
    elif node['inputType'] == 'image_rgb':
        grayscale = False
        trainer.input_shape = (3, size[0], size[1])
    else:
        trainer.input_shape = (size[0] * size[1],)
        grayscale = True

    dataset_config = dataset['config']
    print("Generate image iterator in folder %s " % (dataset_config['path'],))

    augmentation = bool(get_option(dataset_config, 'augmentation', False))

    if augmentation:
        train_datagen = get_image_data_augmentor_from_dataset(dataset)
    else:
        train_datagen = ImageDataGenerator()

    train_generator = train_datagen.flow_from_directory(
            directory=os.path.join(dataset_config['path'], 'training'),
            target_size=size,
            batch_size=job_config['settings']['batchSize'],
            color_mode='grayscale' if grayscale is True else 'rgb',
            class_mode='categorical')

    classes = []
    for folderName, outputNeuron in train_generator.class_indices.iteritems():
        if dataset['type'] == 'images_search' or dataset['type'] == 'images_upload':
            category_idx = int(folderName.replace('category_', ''))
            target_category = dataset_config['classes'][category_idx]
            classes.append(target_category['title'] or 'Category %s' % (category_idx, ))
        else:
            classes.append(folderName)

    trainer.set_job_info('classes', classes)
    trainer.classes = classes
    trainer.output_size = train_generator.nb_class

    # ensure_dir(dataset_config['path'] + '/preview')

    test_datagen = ImageDataGenerator(rescale=1./255)
    validation_generator = test_datagen.flow_from_directory(
            directory=os.path.join(dataset_config['path'], 'validation'),
            # save_to_dir=dataset_config['path'] + '/preview',
            target_size=size,
            batch_size=trainer.get_batch_size(),
            color_mode='grayscale' if grayscale is True else 'rgb',
            class_mode='categorical')

    trainer.set_generator_validation_nb(validation_generator.nb_sample)
    trainer.set_generator_training_nb(train_generator.nb_sample)

    print ("Found %d classes, %d images (%d in training [%saugmented], %d in validation) in %s " %
           (len(classes), validation_generator.nb_sample+train_generator.nb_sample, train_generator.nb_sample, 'not ' if augmentation is False else '', validation_generator.nb_sample, dataset_config['path']))

    pprint(train_generator.class_indices)
    pprint(classes)

    return {
        'X_train': train_generator,
        'Y_train': train_generator,
        'X_test': validation_generator,
        'Y_test': validation_generator,
    }

def get_images(job_config, dataset, node, trainer):
    concurrent = 15

    q = Queue(concurrent)
    config = dataset['config']

    dir = trainer.job_model.get_dataset_downloads_dir(dataset)

    ensure_dir(dir)

    classes = config['classes']

    size = (node['width'], node['height'])

    trainer.set_status('PREPARE_IMAGES')

    if node['inputType'] == 'image':
        trainer.input_shape = (1, size[0], size[1])
    elif node['inputType'] == 'image_rgb':
        trainer.input_shape = (3, size[0], size[1])
    else:
        trainer.input_shape = (size[0] * size[1],)

    max = 0
    images = {}

    dataset_path = trainer.job_model.get_dataset_downloads_dir(dataset)
    meta_information_file = dataset_path + '/meta.json'

    classes_changed = False
    config_changed = False
    had_previous = False
    classes_md5 = hashlib.md5(json.dumps(classes)).hexdigest()

    validationFactor = 0.2

    if os.path.isdir(dataset_path):
        if os.path.isfile(meta_information_file):
            with open(meta_information_file) as f:
                meta = json.load(f)
                if meta:
                    had_previous = True
                    if 'classes_md5' in meta and meta['classes_md5'] != classes_md5:
                        classes_changed = True

                    trigger_changed = ['resize', 'resizeWidth', 'resizeHeight', 'resizeCompression']
                    for i in trigger_changed:
                        if i in meta['config'] and i in config and meta['config'][i] != config[i]:
                            config_changed = True
                else:
                    config_changed = True
        else:
            config_changed = True

    need_download = classes_changed or config_changed

    if need_download:
        if had_previous:
            print "Reset dataset and re-download images to " + dir
            if classes_changed:
                print (" .. because classes changed")
            if config_changed:
                print (" .. because settings changed")
        else:
            print "Download images to " + dir

        resize = bool(get_option(config, 'resize', True))
        if resize:
            resizeSize = (int(get_option(config, 'resizeWidth', 64)), int(get_option(config, 'resizeHeight', 64)))
            print " .. with resizing to %dx%d " % resizeSize

        # we need to donwload all images
        shutil.rmtree(dataset_path)

        controller = {'running': True}
        try:
            for category in classes:
                max += len(category['images'])

            for i in range(concurrent):
                t = ImageDownloaderWorker(q, trainer, dataset, max, images, controller)
                t.daemon = True
                t.start()

            for category_idx, category in enumerate(classes):
                for image in category['images']:
                    q.put([image, category_idx])

            q.join()
            controller['running'] = False

            def move_image(image, category = 'training'):
                if image['id'] in images and os.path.isfile(images[image['id']]):
                    target_path = dataset_path + '/%s/category_%s/%s' % (category, category_idx, os.path.basename(images[image['id']]))
                    ensure_dir(os.path.dirname(target_path))
                    os.rename(images[image['id']], target_path)

            for category_idx, category in enumerate(classes):
                random.shuffle(category['images'])
                position = int(math.ceil(len(category['images']) * validationFactor))

                ensure_dir(dataset_path + '/training')
                ensure_dir(dataset_path + '/validation')

                for image in category['images'][position:]: #test data
                    if image['id'] in images and os.path.isfile(images[image['id']]):
                        move_image(image, 'training')

                for image in category['images'][:position]: #validation data
                    if image['id'] in images and os.path.isfile(images[image['id']]):
                        move_image(image, 'validation')

            with open(meta_information_file, 'w') as f:
                meta = {
                    'loaded_at': classes_md5,
                    'classes_md5': classes_md5,
                    'config': config
                }
                json.dump(meta, f)

        except KeyboardInterrupt:
            controller['running'] = False
            sys.exit(1)
    else:
        print "Downloaded images up2date in " + dir
        print " - Remove this directory if you want to re-download all images of your dataset and re-shuffle training/validation images."

    trainer.output_size = len(classes)
    trainer.set_status('LOAD IMAGE DONE')

    # change to type local_images
    dataset_transformed = dataset.copy()
    dataset_transformed['config']['path'] = dir

    all_memory = get_option(dataset['config'], 'allMemory', False, 'bool')

    if all_memory:
        return read_images_in_memory(job_config, dataset_transformed, node, trainer)
    else:
        return read_images_keras_generator(job_config, dataset_transformed, node, trainer)