"""Custom logger module using loguru for README-AI."""

import sys

from loguru import logger


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
        logger.configure(
            handlers=[
                {
                    "sink":
                        sys.stderr,
                    "level":
                        self.level,
                    "colorize":
                        True,
                    "format":
                        "<level>{time:YYYY-MM-DD HH:mm:ss}</level> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>:{message}",
                }
            ]
        )

    def info(self, msg, *args, **kwargs):
        logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        logger.critical(msg, *args, **kwargs)

    def trace(self, msg, *args, **kwargs):
        logger.trace(msg, *args, **kwargs)

    def success(self, msg, *args, **kwargs):
        logger.success(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        logger.exception(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        logger.log(level, msg, *args, **kwargs)
