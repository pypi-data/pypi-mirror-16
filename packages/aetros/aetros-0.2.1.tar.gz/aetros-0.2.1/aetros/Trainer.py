from __future__ import division
import json
from threading import Lock

class Trainer():
    def __init__(self, aetros_backend, job_model, logger):
        self.aetros_backend = aetros_backend
        self.logger = logger
        self.input_shape = []
        self.on_gpu = False

        # training sample count per epoch for generator. same name as in keras fit_generator
        self.samples_per_epoch = 1
        # validation sample count per epoch for generator. same name as in keras fit_generator
        self.nb_val_samples = 1

        self.data_validation = None
        self.data_train = None
        self.classes = []

        self.job_model = job_model
        self.job = job_model.job
        self.settings = self.job['config']['settings']
        self.model = None
        self.callbacks = []
        self.lock = Lock()

    def get_batch_size(self):
        return self.job_model.get_batch_size()

    def set_generator_validation_nb(self, number):
        """
        sets self.nb_val_samples which is used in model.fit if input is a generator
        :param number:
        :return:
        """

        self.nb_val_samples = number
        diff_to_batch = number % self.get_batch_size()
        if diff_to_batch > 0:
            self.nb_val_samples += self.get_batch_size() - diff_to_batch

    def set_generator_training_nb(self, number):
        """
        sets self.samples_per_epoch which is used in model.fit if input is a generator
        :param number:
        :return:
        """

        self.samples_per_epoch = number
        diff_to_batch = number % self.get_batch_size()
        if diff_to_batch > 0:
            self.samples_per_epoch += self.get_batch_size() - diff_to_batch

    def set_model(self, model):
        self.model = model

    def is_generator(self, obj):
        from keras.preprocessing.image import DirectoryIterator
        from aetros.auto_dataset import InMemoryDataGenerator

        if isinstance(obj, DirectoryIterator):
            return True

        if isinstance(obj, InMemoryDataGenerator):
            return True

        return False

    def has_generator(self, dict):
        for v in dict.values():
            if self.is_generator(v):
                return True

        return False

    def get_first_generator(self, dict):
        for v in dict.values():
            if self.is_generator(v):
                return v

        return None

    def set_status(self, status):
        self.lock.acquire()

        print 'Training status changed to %s ' % (status,)
        self.aetros_backend.job_add_status('status', status)

        self.lock.release()

    def set_job_info(self, key, value):
        self.aetros_backend.job_set_info_key(key, value)

