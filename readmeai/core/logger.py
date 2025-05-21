"""Custom logger implementation with color and emoji support."""

import logging
import sys
from typing import Annotated, Any, ClassVar, Union

import structlog
from pydantic import Field, StringConstraints
from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_LEVEL_COLORS: dict[str, str] = {
    "DEBUG": "\033[34m",
    "INFO": "\033[35m",
    "WARNING": "\033[33m",
    "ERROR": "\033[31m",
    "CRITICAL": "\033[31m\033[1m",
}
LOG_LEVEL_EMOJIS: dict[str, str] = {
    "DEBUG": "⚙︎",
    "INFO": "►",
    "WARNING": "⚠️",
    "ERROR": "ⓧ",
    "CRITICAL": "‼",
}
RESET_COLOR: str = "\033[0m"


def parse_env_bool(value: str) -> bool:
    """Parse a string environment variable into a boolean."""
    return value.lower() in ("true", "1", "yes")


class LoggingConfig(BaseSettings):
    """
    Logging configuration settings.
    """

    log_level: Annotated[str, StringConstraints(to_upper=True)] = Field(default="DEBUG")
    indent: Annotated[int, Field(default=2, ge=2, le=50)] = 4
    pad_event: int = Field(default=20, ge=0, le=50)
    use_json: bool = Field(default=False)
    log_prefix: str = Field(default="")

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file="../.env",
        env_file_encoding="utf-8",
        env_prefix="LOG_",
        extra="ignore",
    )


class CustomFormatter(logging.Formatter):
    """
    Custom formatter adding colors and emojis to log messages.
    """

    def __init__(self, log_prefix: str = "") -> None:
        """Initialize the formatter with a log prefix."""
        super().__init__(
            fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.log_prefix = log_prefix

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with color and emoji."""
        super().format(record)
        emoji = LOG_LEVEL_EMOJIS.get(record.levelname, "")
        color = LOG_LEVEL_COLORS.get(record.levelname, "")
        prefix = f"{self.log_prefix} | " if self.log_prefix else ""
        return (
            f"{color}{emoji} {record.levelname} | {record.asctime} | "
            f"{prefix}{record.name} | {RESET_COLOR}{record.message}"
        )


class Logger:
    """
    Logger that dynamically switches between JSON and console output.
    """

    _instances: ClassVar[dict[str, "Logger"]] = {}

    def __new__(cls, name: str) -> "Logger":
        """Singleton pattern to ensure only one logger per name."""
        if name not in cls._instances:
            cls._instances[name] = super().__new__(cls)
        return cls._instances[name]

    def __init__(self, name: str) -> None:
        """Initialize the logger with the given name."""
        if not hasattr(self, "_initialized"):
            self.name = name
            self.config = LoggingConfig()
            self._logger = self._setup_logger()
            self._initialized = True

    def _setup_logger(self) -> Union[logging.Logger, structlog.stdlib.BoundLogger]:
        """Initialize either structlog or standard logger based on config."""
        if self.config.use_json:
            return self._setup_structlog()
        return self._setup_custom_logger()

    def _setup_structlog(self) -> structlog.stdlib.BoundLogger:
        """Configure and return a structured logger."""
        # Ensure root logger is configured
        root_logger = logging.getLogger()
        if not root_logger.handlers:
            handler = logging.StreamHandler(sys.stderr)
            root_logger.addHandler(handler)
            root_logger.setLevel(self.config.log_level)

        structlog.configure(
            processors=[
                structlog.stdlib.add_log_level,
                structlog.stdlib.add_logger_name,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
                structlog.processors.JSONRenderer(indent=self.config.indent),
            ],
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(self.name)

    def _setup_custom_logger(self) -> logging.Logger:
        """Configure and return a custom formatted logger."""
        logger = logging.getLogger(self.name)

        if not logger.handlers:
            handler = logging.StreamHandler(sys.stderr)
            formatter = CustomFormatter(log_prefix=self.config.log_prefix)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(self.config.log_level)
            logger.propagate = False

        return logger

    def _log(self, level: str, msg: str, *args: Any, **kwargs: Any) -> None:
        """Internal logging method."""
        getattr(self._logger, level)(msg, *args, **kwargs)

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log("info", msg, *args, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log("debug", msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log("warning", msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log("error", msg, *args, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._log("critical", msg, *args, **kwargs)


def get_logger(name: str) -> Logger:
    """Get a logger instance for the given name."""
    return Logger(name=name)
