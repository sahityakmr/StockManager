import logging


def initialize():
    logging.basicConfig()
    logging.root.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)


initialize()
