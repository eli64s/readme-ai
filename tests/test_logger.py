"""Unit tests for the logger module."""
import logging

import pytest

from src.logger import Logger


@pytest.mark.parametrize(
    "level, expected_level",
    [
        (logging.INFO, "INFO"),
        (logging.DEBUG, "DEBUG"),
        (logging.WARNING, "WARNING"),
        (logging.ERROR, "ERROR"),
        (logging.CRITICAL, "CRITICAL"),
    ],
)
def test_logger_methods(capfd, level, expected_level):
    logger = Logger("test_logger", level=level)
    message = f"This is a {expected_level.lower()} message"
    method_name = expected_level.lower()

    method = getattr(logger, method_name)
    method(message)

    captured = capfd.readouterr()
    assert "test_logger" in captured.out
    assert expected_level in captured.out
    assert message in captured.out


@pytest.mark.parametrize(
    "level, expected_level",
    [
        (logging.INFO, logging.INFO),
        (logging.DEBUG, logging.DEBUG),
        (logging.WARNING, logging.WARNING),
        (logging.ERROR, logging.ERROR),
        (logging.CRITICAL, logging.CRITICAL),
    ],
)
def test_logger_set_level(capfd, level, expected_level):
    logger = Logger("test_logger", level=level)
    logger.set_level(expected_level)

    assert logger.logger.getEffectiveLevel() == expected_level


def test_logger_formatting(capfd):
    logger = Logger("test_logger", level=logging.INFO)
    logger.info("This is an info message")
    logger.warning("This is a warning message with %d parameters", 1)
    logger.error("This is an error message with %s parameter", "one")

    captured = capfd.readouterr()
    assert "test_logger" in captured.out
    assert "INFO" in captured.out
    assert "This is an info message" in captured.out
    assert "WARNING" in captured.out
    assert "This is a warning message with 1 parameters" in captured.out
    assert "ERROR" in captured.out
    assert "This is an error message with one parameter" in captured.out


def test_logger_output_file(tmp_path):
    log_file = tmp_path / "test.log"
    logger = Logger("test_logger", level=logging.INFO, output_file=log_file)

    logger.info("This is an info message")
    logger.warning("This is a warning message with %d parameters", 1)
    logger.error("This is an error message with %s parameter", "one")

    assert log_file.read_text() == (
        "\x1b[32mINFO\x1b[0m:test_logger:This is an info message\n"
        "\x1b[33mWARNING\x1b[0m:test_logger:This is a warning message with 1 parameters\n"
        "\x1b[31mERROR\x1b[0m:test_logger:This is an error message with one parameter\n"
    )
