"""
Utility methods to read package resource files.
"""

from importlib import resources
from pathlib import Path

from readmeai._exceptions import FileReadError


def get_resource_path(
    file_path: str,
    package: str = "readmeai.config",
    submodule: str = "settings",
) -> str:
    """Retrieves the path to a resource file within the package.

    This function attempts to first use `importlib.resources` for preferred
    access to resources within the package. It falls back to `pkg_resources`
    for compatibility with older environments.

    Parameters
    ----------
    file_path
        The path to the resource file relative to the package's submodule.
    package, optional
        The package name containing the resource file.
        - default: "readmeai.config"
    submodule, optional
        The submodule within the package where the resource is located.
        - default: "settings"

    Returns
    -------
        The absolute path to the resource file.

    Raises
    ------
    FileReadError
        FileReadError: If the resource file cannot be found or accessed.
    """
    resource_path = None
    try:
        resource_path = resources.files(package).joinpath(submodule, file_path)

    except TypeError:  # pragma: no cover
        try:
            import pkg_resources

            submodule = submodule.replace(".", "/")
            resource_path = Path(
                pkg_resources.resource_filename(
                    "readmeai",
                    f"{submodule}/{file_path}",
                ),
            ).resolve()

        except Exception as exc:  # pragma: no cover
            raise FileReadError(
                "Error loading resource file via pkg_resources",
                str(resource_path),
            ) from exc

    if resource_path is None:
        raise FileReadError("Resource file not found", str(resource_path))

    return str(resource_path)
