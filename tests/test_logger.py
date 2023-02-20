import logging
import unittest

from logger import SingletonLogger


class TestSingletonLogger(unittest.TestCase):
    def test_singleton_instance(self):
        logger1 = SingletonLogger.get_instance()
        logger2 = SingletonLogger.get_instance()

        self.assertIs(logger1, logger2)

    def test_log_levels(self):
        logger = SingletonLogger.get_instance()

        # Test debug level logging
        debug_message = "This is a debug message"
        logger.debug(debug_message)
        self.assertLogRecord(logger, logging.DEBUG, debug_message)

        # Test info level logging
        info_message = "This is an info message"
        logger.info(info_message)
        self.assertLogRecord(logger, logging.INFO, info_message)

        # Test warning level logging
        warning_message = "This is a warning message"
        logger.warning(warning_message)
        self.assertLogRecord(logger, logging.WARNING, warning_message)

        # Test error level logging
        error_message = "This is an error message"
        logger.error(error_message)
        self.assertLogRecord(logger, logging.ERROR, error_message)

        # Test critical level logging
        critical_message = "This is a critical message"
        logger.critical(critical_message)
        self.assertLogRecord(logger, logging.CRITICAL, critical_message)

    def assertLogRecord(self, logger, level, message):
        last_log_record = logger.logger.handlers[0].stream.getvalue().strip()
        self.assertIn(message, last_log_record)
        self.assertIn(logging.getLevelName(level), last_log_record)
