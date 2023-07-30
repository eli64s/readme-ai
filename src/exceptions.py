"""Custom exception classes for OpenAI errors."""


class OpenAIException(Exception):
    """Custom exception for OpenAI errors."""

    def __init__(self, message: str, original_exception: Exception):
        super().__init__(message)
        self.original_exception = original_exception


class HTTPStatusException(Exception):
    """Custom exception for HTTP status errors."""

    def __init__(self, message: str, original_exception: Exception):
        super().__init__(message)
        self.original_exception = original_exception


class RetryException(Exception):
    """Custom exception for retry errors."""

    def __init__(self, message: str, original_exception: Exception):
        super().__init__(message)
        self.original_exception = original_exception


class GeneralException(Exception):
    """Custom exception for general errors."""

    def __init__(self, message: str, original_exception: Exception):
        super().__init__(message)
        self.original_exception = original_exception
