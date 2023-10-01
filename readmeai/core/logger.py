"""Custom logger class for the project."""

import logging
import sys

from colorlog import ColoredFormatter


class Logger:
    """Custom logger implementation."""

    _instance = None

    def __new__(cls, name, level="DEBUG"):
        """Checks if an instance of the Logger class exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._name = name
            cls._instance._level = level
            cls._instance._configure_logger()
        return cls._instance

    def _configure_logger(self):
        """Configures the logger."""
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
        logger = logging.getLogger(self._name)
        logger.addHandler(handler)
        logger.setLevel(self._level)

    def info(self, msg, *args, **kwargs):
        """Logs an info message."""
        logging.getLogger(self._name).info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """Logs a debug message."""
        logging.getLogger(self._name).debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Logs a warning message."""
        logging.getLogger(self._name).warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """Logs an error message."""
        logging.getLogger(self._name).error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """Logs a critical message."""
        logging.getLogger(self._name).critical(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        """Logs a message at the specified level."""
        logging.getLogger(self._name).log(level, msg, *args, **kwargs)
