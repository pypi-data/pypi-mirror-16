"""Starts opsdroid."""

import sys
import os
import logging
import argparse

from opsdroid.loader import Loader
from opsdroid.core import OpsDroid
from opsdroid.helper import set_logging_level
from opsdroid.const import LOG_FILENAME


def parse_args(args):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Run opsdroid.')
    parser.add_argument('--gen-config', action="store_true",
                        help='prints out an example configuration file')
    return parser.parse_args(args)


def main():
    """The main function."""
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    logging.info("="*40)
    logging.info("Stated application")

    args = parse_args(sys.argv[1:])

    if args.gen_config:
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "configuration/example_configuration.yaml")
        with open(path, 'r') as conf:
            print(conf.read())
        sys.exit(0)

    with OpsDroid() as opsdroid:
        loader = Loader(opsdroid)
        opsdroid.config = loader.load_config_file([
            "./configuration.yaml",
            "~/.opsdroid/configuration.yaml",
            "/etc/opsdroid/configuration.yaml"
            ])
        if "logging" in opsdroid.config:
            set_logging_level(opsdroid.config['logging'])
        loader.load_config(opsdroid.config)
        opsdroid.exit()

if __name__ == "__main__":
    main()
