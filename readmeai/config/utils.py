"""Utility methods to read package resources."""

from importlib import resources
from pathlib import Path

from readmeai.exceptions import FileReadError
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.logger import Logger

_logger = Logger(__name__)


def get_resource_path(
    handler: FileHandler,
    file_path: str,
    package: str = "readmeai.config",
    submodule: str = "settings",
) -> dict:
    """Get configuration dictionary from TOML file."""
    try:
        resource_path = resources.files(package).joinpath(submodule, file_path)
        _logger.debug(f"Loading file via importlib.resources: {resource_path}")

    except TypeError as exc:
        _logger.debug(f"Error using importlib.resources: {exc}")

        try:
            import pkg_resources

            submodule = submodule.replace(".", "/")
            resource_path = Path(
                pkg_resources.resource_filename(
                    "readmeai", f"{submodule}/{file_path}"
                )
            ).resolve()

        except Exception as exc:
            _logger.error(f"Error loading file via pkg_resources: {exc}")

            raise FileReadError(
                "Error loading file via pkg_resources", str(file_path)
            ) from exc

    if not resource_path.exists():
        _logger.error(f"File not found: {str(resource_path)}")
        raise FileReadError("File not found", str(resource_path))

    if str(file_path).endswith(".toml"):
        return handler.read_toml(str(resource_path))

    elif str(file_path).endswith(".json"):
        return handler.read_json(str(resource_path))

    _logger.error(f"Unsupported file format: {file_path}")

    raise FileReadError("Unsupported file format", str(file_path))
