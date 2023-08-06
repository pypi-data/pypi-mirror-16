import sys
import os
from argparse import RawTextHelpFormatter

import aetros.const
from aetros.commands.PredictCommand import PredictCommand
from aetros.commands.StartCommand import StartCommand

commands_dict = {
    'start': StartCommand,
    'predict': PredictCommand
}
command_summaries = [
    ['start', 'Starts a training of a network in current working directory'],
    ['stop', 'Stops a training'],
    ['predict', 'Runs a prediction locally']
]

def create_main_parser():
    import argparse
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, add_help=False, prog=const.__prog__)

    pkg_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser.version = 'aetros %s from %s (python %s)' % (
        const.__version__, pkg_dir, sys.version[:3])

    parser.add_argument('command', nargs='?')
    parser.add_argument('--version', action='version', version='%s' % (const.__version__,))
    parser.add_argument("-h", "--help", action='store_true', help="show this help message and exit")

    # # add the general options
    # gen_opts = cmdoptions.make_option_group(cmdoptions.general_group, parser)
    # parser.add_option_group(gen_opts)

    # parser.main = True  # so the help formatter knows

    # create command listing for description
    command_summaries = [
        ['start', 'Starts a training of a network'],
        ['stop', 'Stops a tranining']
    ]
    description = [''] + ['%-27s %s' % (i, j) for i, j in command_summaries]
    parser.description = 'Please don not forget to provide API_KEY as environment variable.\nPossible commands:\n' + ('\n'.join(description))

    return parser


def parseopts(args):
    if len(args) == 0:

        description = [''] + ['%-27s %s' % (i, j) for i, j in command_summaries]
        print("usage: API_KEY='key' aetros [command]\n")
        print('Please don not forget to provide API_KEY as environment variable.\n\nPossible commands:\n' + ('\n'.join(description)))

        sys.exit(1)

    cmd_name = args[0]

    # all the args without the subcommand
    cmd_args = args[1:]

    if not os.getenv('API_KEY'):
        print aetros.const.bcolors.FAIL + "API_KEY not defined." + aetros.const.bcolors.ENDC
        sys.exit(1)

    return cmd_name, cmd_args


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    cmd_name, cmd_args = parseopts(args)

    command = commands_dict[cmd_name]()

    return command.main(cmd_args)