from os.path import dirname, abspath
import time
import yaml
import logging

ROOT_DIR = dirname(dirname(abspath(__file__)))
LOG = object


def get_timestamp():
    return time.strftime("%Y%m%d-%H%M%S")


def get_str_day():
    return time.strftime("%Y%m%d")


def create_logger(filename):
    """creates log file with time stamp filename under log directory"""
    logging.basicConfig(filename=filename,
                        level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s',
                        filemode='a')  # use w to override with each run
    return logging.getLogger()


def load_yaml(filepath):
    """Loads a yaml file"""
    with open(filepath, 'r') as data:
        document = yaml.safe_load(data)
    return document


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)
