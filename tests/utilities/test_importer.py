from typing import Literal
from unittest import mock

import pytest
from readmeai.utilities.importer import is_available


@pytest.fixture
def mock_import():
    """Provides a mock for importlib.import_module."""
    with mock.patch("importlib.import_module") as mock_imp:
        yield mock_imp


def test_existing_module():
    """Verify stdlib modules are correctly identified as available."""
    assert is_available("os") is True


def test_nonexistent_module():
    """Verify non-existent modules are correctly identified as unavailable."""
    assert is_available("definitely_not_a_real_module_name_12345") is False


def test_module_import_error(mock_import: mock.MagicMock | mock.AsyncMock):
    """Verify proper handling of ModuleNotFoundError."""
    mock_import.side_effect = ModuleNotFoundError()
    assert is_available("mocked_module") is False
    mock_import.assert_called_once_with("mocked_module")


@pytest.mark.parametrize(
    "exception_class",
    [
        pytest.param(ImportError, id="ImportError"),
        pytest.param(PermissionError, id="PermissionError"),
    ],
)
def test_module_import_error_exception(
    mock_import: mock.MagicMock | mock.AsyncMock,
    exception_class: type[ImportError] | type[PermissionError],
):
    """Verify that non-ModuleNotFoundError exceptions are propagated."""
    mock_import.side_effect = exception_class()
    with pytest.raises(exception_class):
        is_available("mocked_module")


def test_empty_module_name():
    """Verify that empty module names raise appropriate ValueError."""
    with pytest.raises(ValueError, match="Empty module name"):
        is_available("")


@pytest.mark.parametrize(
    "module_name",
    [
        pytest.param("sys", id="core_module"),
        pytest.param("datetime", id="time_module"),
        pytest.param("collections", id="data_module"),
        pytest.param("json", id="serialization_module"),
    ],
)
def test_standard_modules(
    module_name: Literal["sys"]
    | Literal["datetime"]
    | Literal["collections"]
    | Literal["json"],
):
    """Verify availability check for various standard library modules."""
    assert is_available(module_name) is True


def test_module_side_effects(mock_import: mock.MagicMock | mock.AsyncMock):
    """Verify that availability check doesn't pollute global namespace."""
    test_module = "some_test_module"
    is_available(test_module)

    mock_import.assert_called_once_with(test_module)
    assert test_module not in globals()


@pytest.mark.parametrize(
    ("module_name", "expected"),
    [
        pytest.param("OS", False, id="uppercase_invalid"),
        pytest.param("os", True, id="lowercase_valid"),
    ],
)
def test_case_sensitivity(module_name, expected):
    """Verify case-sensitive module name handling."""
    assert is_available(module_name) is expected
