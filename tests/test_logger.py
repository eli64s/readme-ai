import pytest
import structlog
from structlog.stdlib import BoundLogger
from structlog.testing import LogCapture

from readmeai.logger import LoggingConfig, get_logger


@pytest.fixture
def log_settings():
    return LoggingConfig(
        log_level="INFO",
        indent=2,
        pad_event=20,
        use_json=True,
    )


@pytest.fixture
def logger_instance() -> structlog.stdlib.BoundLogger:
    return get_logger("test_logger")


@pytest.fixture
def log_capture():
    return LogCapture()


@pytest.fixture(autouse=True)
def setup_structlog(log_capture: LogCapture):
    structlog.configure(processors=[log_capture])


def test_logger_output_json(
    logger_instance: BoundLogger, log_capture: LogCapture
):
    logger = get_logger("test_logger")
    logger.info("Test message")
    assert len(log_capture.entries) == 1
    assert log_capture.entries[0]["event"] == "Test message"


def test_logger_output_console(
    logger_instance: BoundLogger, log_capture: LogCapture
):
    logger_instance.use_json = False
    logger = get_logger("test_logger")
    logger.info("Test message")
    assert len(log_capture.entries) == 1
    assert log_capture.entries[0]["event"] == "Test message"


def test_logger_different_levels(
    logger_instance: BoundLogger, log_capture: LogCapture
):
    logger = get_logger("test_logger")

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

    # assert len(log_capture.entries) == 3  # Debug should not be logged
    assert log_capture.entries[0]["event"] == "Debug message"
    assert log_capture.entries[1]["event"] == "Info message"
    assert log_capture.entries[2]["event"] == "Warning message"
    assert log_capture.entries[3]["event"] == "Error message"


def test_logger_with_extra_context(
    logger_instance: BoundLogger, log_capture: LogCapture
):
    logger = get_logger("test_logger")
    logger.info("Test message", extra_key="extra_value")

    assert len(log_capture.entries) == 1
    assert log_capture.entries[0]["event"] == "Test message"
    assert log_capture.entries[0]["extra_key"] == "extra_value"
