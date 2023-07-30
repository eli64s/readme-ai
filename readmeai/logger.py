"""Custom logger class for the project."""

import logging
import sys

from colorlog import ColoredFormatter


class Logger:
    _instance = None

    def __new__(cls, name, level="DEBUG"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.level = level
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        formatter = ColoredFormatter(
            "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red",
            },
        )
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(formatter)
        logger = logging.getLogger(self.name)
        logger.addHandler(handler)
        logger.setLevel(self.level)

    def info(self, msg, *args, **kwargs):
        logging.getLogger(self.name).info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        logging.getLogger(self.name).debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        logging.getLogger(self.name).warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        logging.getLogger(self.name).error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        logging.getLogger(self.name).critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        logging.getLogger(self.name).log(level, msg, *args, **kwargs)
