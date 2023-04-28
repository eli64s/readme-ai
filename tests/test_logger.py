"""Unit tests for the custom logger module."""

import io
from unittest.mock import patch

import pytest

from src.logger import Logger


@pytest.fixture
def logger():
    return Logger("test_logger", level="DEBUG")


def test_logger_info(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.info("This is an info message")
        assert "INFO" in fake_stderr.getvalue()


def test_logger_debug(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.debug("This is a debug message")
        assert "DEBUG" in fake_stderr.getvalue()


def test_logger_warning(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.warning("This is a warning message")
        assert "WARNING" in fake_stderr.getvalue()


def test_logger_error(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.error("This is an error message")
        assert "ERROR" in fake_stderr.getvalue()


def test_logger_critical(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.critical("This is a critical message")
        assert "CRITICAL" in fake_stderr.getvalue()


def test_logger_trace(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.trace("This is a trace message")
        assert "TRACE" in fake_stderr.getvalue()


def test_logger_success(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.success("This is a success message")
        assert "SUCCESS" in fake_stderr.getvalue()


def test_logger_exception(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        try:
            1 / 0
        except ZeroDivisionError as e:
            logger.exception("This is an exception message: {}", e)
        assert "ERROR" in fake_stderr.getvalue()
        assert "ZeroDivisionError" in fake_stderr.getvalue()


def test_logger_log(logger):
    with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
        logger.log("WARNING", "This is a custom log message")
        assert "WARNING" in fake_stderr.getvalue()
        assert "This is a custom log message" in fake_stderr.getvalue()
