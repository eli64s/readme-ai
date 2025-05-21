import os
import sys
from pathlib import Path
from typing import Literal

import pytest
from readmeai.core.errors import FileReadError
from readmeai.utilities.resource_manager import build_resource_path


def test_build_resource_path_default_module(tmp_path: Path):
    """Test build_resource_path with default module and submodule."""
    config_file = tmp_path / "config.toml"
    config_file.write_text("# Test Config")
    # Monkey patch the resources.files method to return our temp directory

    def mock_files(module):
        class MockPath:
            def joinpath(self, *args):
                return tmp_path / os.path.join(*args)

        return MockPath()

    with pytest.MonkeyPatch.context() as m:
        m.setattr("importlib.resources.files", mock_files)
        path = build_resource_path("config.toml")
        assert isinstance(path, Path)
        assert path.name == "config.toml"
        assert str(tmp_path) in str(path)


def test_build_resource_path_custom_module(tmp_path: Path):
    """Test build_resource_path with a custom module and submodule."""
    config_file = tmp_path / "test_config.toml"
    config_file.write_text("# Test Custom Config")

    # Monkey patch the resources.files method to return our temp directory
    def mock_files(module):
        class MockPath:
            def joinpath(self, *args):
                return tmp_path / os.path.join(*args)

        return MockPath()

    with pytest.MonkeyPatch.context() as m:
        m.setattr("importlib.resources.files", mock_files)
        path = build_resource_path(
            file_path="test_config.toml", module="readmeai.tests", submodule="resources"
        )
        assert isinstance(path, Path)
        assert path.name == "test_config.toml"
        assert str(tmp_path) in str(path)


def test_build_resource_path_fallback(tmp_path):
    """Test fallback mechanism when importlib.resources fails."""

    # Simulate importlib.resources failure
    def mock_files(module):
        raise TypeError("Simulated importlib.resources error")

    # Attempt to import pkg_resources, but use a fallback if not available
    try:
        import pkg_resources

        # Create a mock config file
        config_file = tmp_path / "config.toml"
        config_file.write_text("# Test Fallback Config")

        # Monkey patch pkg_resources.resource_filename to return our temp path
        with pytest.MonkeyPatch.context() as m:
            m.setattr("importlib.resources.files", mock_files)
            m.setattr(
                "pkg_resources.resource_filename",
                lambda module, path: str(tmp_path / path),
            )
            path = build_resource_path("config.toml")
            assert isinstance(path, Path)
            assert path.name == "config.toml"
            assert str(tmp_path) in str(path)

    except ImportError:
        pytest.skip("pkg_resources not available")


def test_build_resource_path_failure(tmp_path: Path):
    """Test that FileReadError is raised when all methods fail."""

    # Simulate both importlib.resources and pkg_resources failures
    def mock_files(module):
        raise TypeError("Simulated importlib.resources error")

    with pytest.MonkeyPatch.context() as m:
        m.setattr("importlib.resources.files", mock_files)

        # Remove pkg_resources if it exists
        if "pkg_resources" in sys.modules:
            del sys.modules["pkg_resources"]

        with pytest.raises(FileReadError, match="Failed to load resource file"):
            build_resource_path("nonexistent.toml")


@pytest.mark.parametrize("file_path", ["config.toml", "settings.json", "template.txt"])
def test_build_resource_path_multiple_files(
    tmp_path: Path,
    file_path: Literal["config.toml"]
    | Literal["settings.json"]
    | Literal["template.txt"],
):
    """Test building paths for multiple different files."""
    mock_file = tmp_path / file_path
    mock_file.write_text(f"# Test {file_path}")

    # Monkey patch the resources.files method to return our temp directory
    def mock_files(module):
        class MockPath:
            def joinpath(self, *args):
                return tmp_path / os.path.join(*args)

        return MockPath()

    with pytest.MonkeyPatch.context() as m:
        m.setattr("importlib.resources.files", mock_files)
        path = build_resource_path(file_path)
        assert isinstance(path, Path)
        assert path.name == file_path
        assert str(tmp_path) in str(path)
