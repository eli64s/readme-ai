"""Utility that builds the full path for package resource files."""

from importlib import resources
from pathlib import Path

from readmeai.core.errors import FileReadError
from readmeai.core.logger import get_logger

_logger = get_logger(__name__)


def build_resource_path(
    file_path: str,
    module: str = "readmeai.config",
    submodule: str = "settings",
) -> Path:
    """Retrieves the path to a resource file within the package.

    Tries importlib.resources first, falls back to pkg_resources.
    """
    try:
        return resources.files(module).joinpath(submodule, file_path)

    except (TypeError, FileNotFoundError) as e:
        _logger.error(f"Error loading resource file via importlib.resources: {e}")

    try:
        import pkg_resources

        submodule = submodule.replace(".", "/")
        return Path(
            pkg_resources.resource_filename(
                module,
                f"{submodule}/{file_path}",
            ),
        ).resolve()

    except Exception as e:
        raise FileReadError(
            f"Failed to load resource file: {file_path} from {module}.{submodule}",
        ) from e
