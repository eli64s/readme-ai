import importlib


def is_available(name: str) -> bool:
    """Check if a module is available for import."""
    try:
        importlib.import_module(name)
        return True
    except ModuleNotFoundError:  # pragma: no cover
        return False
