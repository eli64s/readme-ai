"""Utility that builds the full path for package resource files."""

from importlib import resources
from pathlib import Path
from typing import Union

from readmeai.errors import FileReadError
from readmeai.logger import get_logger
from readmeai.utils.module_importer import is_available

logger = get_logger(__name__)


def build_resource_path(
    file_path: str,
    module: str = "readmeai.config",
    submodule: str = "settings",
) -> Union[str, Path]:
    """
    Retrieve the path to a resource file within the package.

    Parameters
    ----------
    file_path : str
        Name of the resource file.
    module : str, optional
        Base module path, by default "readmeai.config"
    submodule : str, optional
        Submodule containing the resource, by default "settings

    Returns
    -------
    Union[str, Path]
        Path to the resource file.

    Raises
    ------
    FileReadError
        If resource cannot be located.
    """
    try:
        if hasattr(resources, "files"):
            return str(resources.files(module) / submodule / file_path)
    except Exception as e:
        logger.debug(f"Failed to read resource using importlib: {e!r}")

    if is_available("pkg_resources"):
        try:
            import pkg_resources

            resource_name = f"{submodule}/{file_path}"
            path = pkg_resources.resource_filename(module, resource_name)

            if path and Path(path).exists():
                return path

        except Exception as e:
            logger.debug(f"Failed to read resource using pkg_resources: {e!r}")

    try:
        base_dir = Path(__file__).parent.parent
        direct_path = base_dir / submodule / file_path

        if direct_path.exists():
            return str(direct_path)

    except Exception as e:
        logger.debug(f"Direct path resolution failed: {e!r}")

    raise FileReadError(
        f"Failed to locate file resource '{file_path}' in {module}.{submodule}"
    )
