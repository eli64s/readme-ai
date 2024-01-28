"""Custom logger implementation for the readme-ai CLI."""

import logging
import sys

from colorlog import ColoredFormatter

LOG_LEVEL_EMOJIS = {
    "DEBUG": "⚙︎",
    "INFO": "►",
    "WARNING": "⚠️",
    "ERROR": "ⓧ",
    "CRITICAL": "‼",
}


class CustomFormatter(ColoredFormatter):
    """Custom colored log formatter."""

    def format(self, record) -> str:
        """Formats the log record."""
        record.emoji = LOG_LEVEL_EMOJIS.get(record.levelname, "")
        return super().format(record)


class Logger:
    """Custom logger implementation."""

    _instances = {}

    def __new__(cls, name, level="DEBUG"):
        if name not in cls._instances:
            instance = super().__new__(cls)
            instance._name = name
            instance._level = level
            instance._configure_logger()
            cls._instances[name] = instance
        return cls._instances[name]

    def _configure_logger(self):
        """Configures the logger."""
        formatter = CustomFormatter(
            "%(log_color)s%(emoji)s %(levelname)s | %(white)s%(asctime)s | %(cyan)s%(name)s | %(purple)s%(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            reset=True,
            log_colors={
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
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
