import importlib


def is_available(name: str) -> bool:
    """Check if module is available to import in current environment."""
    try:
        importlib.import_module(name)
        return True
    except ModuleNotFoundError:  # pragma: no cover
        return False
