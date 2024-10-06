from importlib import resources
from pathlib import Path

from readmeai.errors import FileReadError
from readmeai.logger import get_logger

_logger = get_logger(__name__)


def get_resource_path(
    file_path: str,
    module: str = "readmeai.config",
    submodule: str = "settings",
) -> Path:
    """Retrieves the path to a resource file within the package.

    Tries importlib.resources first, falls back to pkg_resources.
    """
    try:
        return resources.files(module).joinpath(submodule, file_path)

    except (TypeError, FileNotFoundError) as exc:
        _logger.error(
            f"Error loading resource file via importlib.resources: {exc}"
        )

    try:
        import pkg_resources

        submodule = submodule.replace(".", "/")
        return Path(
            pkg_resources.resource_filename(
                module,
                f"{submodule}/{file_path}",
            ),
        ).resolve()

    except Exception as exc:
        raise FileReadError(
            "Error loading resource file via pkg_resources",
            f"{submodule}/{file_path}",
        ) from exc
