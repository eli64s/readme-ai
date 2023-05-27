"""Unit tests for the custom logger module."""

import pytest
from loguru import logger

from src.logger import Logger


@pytest.fixture
def setup_logger():
    return Logger("Test", "DEBUG")


def test_logger_singleton(setup_logger):
    assert setup_logger is Logger("Test", "DEBUG")


def test_logger_info(setup_logger):
    with logger.catch() as log_data:
        setup_logger.info("Test info log")
        assert log_data[0].level.name == "INFO"
        assert log_data[0].message == "Test info log"


def test_logger_debug(setup_logger):
    with logger.catch() as log_data:
        setup_logger.debug("Test debug log")
        assert log_data[0].level.name == "DEBUG"
        assert log_data[0].message == "Test debug log"


def test_logger_warning(setup_logger):
    with logger.catch() as log_data:
        setup_logger.warning("Test warning log")
        assert log_data[0].level.name == "WARNING"
        assert log_data[0].message == "Test warning log"


def test_logger_error(setup_logger):
    with logger.catch() as log_data:
        setup_logger.error("Test error log")
        assert log_data[0].level.name == "ERROR"
        assert log_data[0].message == "Test error log"


def test_logger_critical(setup_logger):
    with logger.catch() as log_data:
        setup_logger.critical("Test critical log")
        assert log_data[0].level.name == "CRITICAL"
        assert log_data[0].message == "Test critical log"


def test_logger_trace(setup_logger):
    with logger.catch() as log_data:
        setup_logger.trace("Test trace log")
        assert log_data[0].level.name == "TRACE"
        assert log_data[0].message == "Test trace log"


def test_logger_success(setup_logger):
    with logger.catch() as log_data:
        setup_logger.success("Test success log")
        assert log_data[0].level.name == "SUCCESS"
        assert log_data[0].message == "Test success log"


def test_logger_exception(setup_logger):
    with logger.catch() as log_data:
        try:
            raise Exception("Test exception")
        except Exception as e:
            setup_logger.exception(e)
            assert log_data[0].level.name == "ERROR"
            assert "Test exception" in log_data[0].message


def test_logger_log(setup_logger):
    with logger.catch() as log_data:
        setup_logger.log("DEBUG", "Test log message")
        assert log_data[0].level.name == "DEBUG"
        assert log_data[0].message == "Test log message"
