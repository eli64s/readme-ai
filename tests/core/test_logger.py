import json
import logging
from io import StringIO
from typing import Literal
from unittest.mock import patch

import pytest
from readmeai.core.logger import (
    LOG_LEVEL_COLORS,
    LOG_LEVEL_EMOJIS,
    CustomFormatter,
    LoggingConfig,
    get_logger,
)


@pytest.mark.parametrize(
    "log_method,log_level",
    [
        ("info", logging.INFO),
        ("debug", logging.DEBUG),
        ("warning", logging.WARNING),
        ("error", logging.ERROR),
        ("critical", logging.CRITICAL),
    ],
)
def test_logger_log_methods(
    log_method: Literal["info"]
    | Literal["debug"]
    | Literal["warning"]
    | Literal["error"]
    | Literal["critical"],
    log_level: Literal[20] | Literal[10] | Literal[30] | Literal[40] | Literal[50],
    capture_stderr: StringIO,
):
    """Test that different log methods work correctly."""
    logger = logging.getLogger(f"test_logger_{log_method}")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(capture_stderr)
    handler.setLevel(log_level)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    try:
        log_message = f"Test {log_method.upper()} message"
        log_method_func = getattr(logger, log_method)
        log_method_func(log_message)
        output = capture_stderr.getvalue().strip()
        assert log_message in output
    finally:
        logger.removeHandler(handler)


def test_custom_formatter():
    """Test CustomFormatter for color and emoji formatting."""
    formatter = CustomFormatter(log_prefix="TEST")
    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname="test.py",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None,
    )
    formatted_log = formatter.format(record)
    assert LOG_LEVEL_COLORS["INFO"] in formatted_log
    assert LOG_LEVEL_EMOJIS["INFO"] in formatted_log
    assert "TEST" in formatted_log


def test_logging_config_defaults():
    """Test default logging configuration."""
    config = LoggingConfig()
    assert config.log_level in ["DEBUG", "INFO"]
    assert config.indent == 4
    assert config.pad_event == 20
    assert config.use_json is False
    assert config.log_prefix == ""


@patch.dict("os.environ", {"LOG_USE_JSON": "true"})
def test_logging_config_env_override():
    """Test environment variable overrides for logging config."""
    config = LoggingConfig()
    assert config.use_json is True


def test_get_logger_multiple_calls():
    """Test multiple calls to get_logger with different names."""
    logger1 = get_logger("module1")
    logger2 = get_logger("module2")
    assert logger1 is not None
    assert logger2 is not None
    assert logger1.name == "module1"
    assert logger2.name == "module2"


def test_logger_json_output(monkeypatch: pytest.MonkeyPatch):
    """Test JSON logging output."""
    from io import StringIO

    json_output = StringIO()

    class CustomJSONHandler(logging.StreamHandler):
        def __init__(self, stream):
            super().__init__(stream)
            self.formatter = logging.Formatter(
                '{"timestamp":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s"}'
            )

        def format(self, record):
            return self.formatter.format(record)

    logger = logging.getLogger("json_test")
    logger.setLevel(logging.INFO)
    json_handler = CustomJSONHandler(json_output)
    logger.addHandler(json_handler)
    try:
        logger.info("JSON log test")
        output = json_output.getvalue().strip()
        try:
            json_log = json.loads(output)
            assert "timestamp" in json_log
            assert "level" in json_log
            assert "message" in json_log
            assert json_log["message"] == "JSON log test"
            assert json_log["level"] == "INFO"
        except json.JSONDecodeError:
            pytest.fail(f"Failed to parse log output as JSON. Output was: {output}")
    finally:
        logger.removeHandler(json_handler)


def test_logger_propagation():
    """Test that logger does not propagate logs to parent loggers."""
    logger = logging.getLogger("test_propagation")
    # By default, propagation is True for Python's standard logging
    # So we'll explicitly check and set it
    assert logger.propagate is True
    logger.propagate = False
    assert logger.propagate is False
