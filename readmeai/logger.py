"""Custom structured logging implementation using structlog."""

import json
import logging
from collections.abc import MutableMapping
from typing import Annotated, Any

import structlog
from pydantic import BaseModel, Field, StringConstraints
from structlog.processors import CallsiteParameter
from structlog.stdlib import ProcessorFormatter
from structlog.types import Processor


class LoggingConfig(BaseModel):
    """
    Logging default configuration.
    """

    log_level: Annotated[str, StringConstraints(to_upper=True)] = "INFO"
    indent: Annotated[Any, Field(ge=2, le=50)] = 4
    pad_event: int = Field(default=20, ge=0, le=50)
    use_json: bool = True


class Logger:
    """
    Structured logging via structlog for the readme-ai package.
    """

    def __init__(self) -> None:
        self.log_config: LoggingConfig = LoggingConfig()
        self.log_level: str = self.log_config.log_level
        self.indent: int = self.log_config.indent
        self.pad_event: int = self.log_config.pad_event
        self.use_json: bool = self.log_config.use_json

    def configure_logger(self) -> None:
        """Configure the logger."""
        processors = self.get_processors()
        renderer = self.get_renderer()

        structlog.configure(
            processors=[*processors, renderer],
            context_class=dict,
            wrapper_class=structlog.stdlib.BoundLogger,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        root_logger = logging.getLogger()
        handler = logging.StreamHandler()

        formatter = ProcessorFormatter(
            processor=renderer,
            foreign_pre_chain=processors,
        )

        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
        root_logger.setLevel(self.log_config.log_level)

    def get_processors(self) -> list[Processor]:
        """Return list of structlog processors."""
        return [
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.CallsiteParameterAdder(
                [
                    CallsiteParameter.FILENAME,
                    CallsiteParameter.FUNC_NAME,
                    CallsiteParameter.LINENO,
                    # CallsiteParameter.THREAD_NAME,
                    # CallsiteParameter.PROCESS_NAME,
                ]
            ),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            self.format_message_processor,
        ]

    def get_renderer(self) -> Processor:
        """Sets the logging renderer to JSON or Console."""
        if self.use_json:
            return structlog.processors.JSONRenderer(indent=self.indent)
        else:
            return structlog.dev.ConsoleRenderer(pad_event=self.pad_event)

    @staticmethod
    def format_message_processor(
        logger: structlog.BoundLogger,
        method_name: str,
        event_dict: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]:
        """Extracts the message from the event dictionary and format it."""
        event = event_dict.get("event", "")
        try:
            event_data = json.loads(event)
            event_dict["event"] = event_data.get("event", event)
        except json.JSONDecodeError:
            ...
        return event_dict


Logger().configure_logger()


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """Return a logger instance."""
    return structlog.get_logger(name)
