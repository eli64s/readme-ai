"""Utility methods for the readme-ai CLI application."""

from __future__ import annotations

import os
from importlib import resources
from pathlib import Path

from readmeai.config.enums import ModelOptions, SecretKeys
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.exceptions import FileReadError
from readmeai.utils.logger import Logger

_logger = Logger(__name__)


def filter_file(config_loader: ConfigLoader, file_path: Path) -> bool:
    """
    Check if the given file should be excluded based on provided rules.
    """
    ignore_files = config_loader.blacklist["blacklist"]

    if (
        (file_path.name in ignore_files["files"])
        or (file_path.suffix.lstrip(".") in ignore_files["extensions"])
        or any(
            directory in file_path.parts
            for directory in ignore_files["directories"]
        )
    ):
        return True

    return False


def get_resource_path(
    file_name: str, module: str = "settings", package: str = "readmeai.config"
) -> None:
    """
    Use importlib.resources or pkg_resources to get resource path.
    - Python >= 3.9+ uses importlib.resources to access files in packages.
    - Python < 3.9 uses pkg_resources to access files in packages.
    """
    try:
        full_package_path = f"{package}.{module}".replace("/", ".")
        resource_path = resources.files(full_package_path) / file_name
    except Exception as exc:
        _logger.debug(f"Error using importlib.resources: {exc}")

        try:
            import pkg_resources

            file_path = f"{module}/{file_name}"
            resource_path = pkg_resources.resource_filename(package, file_path)
            resource_path = Path(resource_path).resolve()

        except Exception as exc:
            raise FileReadError(
                "Error loading file via pkg_resources", file_path
            ) from exc

    if resource_path.exists() is False:
        raise FileReadError("File not found", resource_path) from None

    return resource_path


def set_model_engine(config: Settings) -> None:
    """Set LLM environment variables based on the specified LLM service."""
    llm_engine = config.llm.api
    openai_env = _scan_environ([SecretKeys.OPENAI_API_KEY.value])
    vertex_env = _scan_environ(
        [
            SecretKeys.VERTEXAI_LOCATION.value,
            SecretKeys.VERTEXAI_PROJECT.value,
        ]
    )

    if llm_engine is None:
        _logger.info(
            "LLM API CLI input not provided. Checking environment variables..."
        )

        if openai_env and os.environ["OPENAI_API_KEY"] not in ["", "None"]:
            config.llm.api = ModelOptions.OPENAI.name
            config.llm.model = config.llm.model
            config.llm.offline = False
            _logger.info("Running CLI with OpenAI API llm engine...")
            return config
        elif vertex_env:
            config.llm.api = ModelOptions.VERTEX.name
            config.llm.model = "gemini-pro"
            config.llm.offline = False
            _logger.info("Running CLI with Google Vertex AI llm engine...")
            return config
        elif config.llm.api == ModelOptions.OLLAMA.name:
            config.llm.model = "ollama"
            config.llm.offline = False
            _logger.info("Running CLI with Ollama llm engine...")
            return config
        else:
            if config.llm.api == ModelOptions.OFFLINE.name:
                message = "Offline mode enabled by user via CLI."
            else:
                message = (
                    "\n\n\t\t...No LLM API settings exist in environment..."
                )
            return _set_offline(config, message)

    elif llm_engine is not None:
        _logger.info(f"LLM API CLI input received: {llm_engine}")

        if llm_engine == ModelOptions.OPENAI.name:
            if "OPENAI_API_KEY" in os.environ:
                config.llm.api = ModelOptions.OPENAI.name
                config.llm.model = config.llm.model
                config.llm.offline = False
                _logger.info("OpenAI settings found in environment!")
                return config
            else:
                return _set_offline(
                    config,
                    "\n\t\t...OpenAI settings NOT FOUND in environment...",
                )

        elif llm_engine == ModelOptions.OLLAMA.name:
            config.llm.api = ModelOptions.OLLAMA.name
            config.llm.model = "ollama"
            config.llm.offline = False
            _logger.info("Ollama settings found in environment!")
            return config

        elif llm_engine == ModelOptions.VERTEX.name:
            if (
                "VERTEXAI_LOCATION" in os.environ
                and "VERTEXAI_PROJECT" in os.environ
            ):
                config.llm.model = "gemini-pro"
                config.llm.offline = False
                _logger.info("Vertex AI settings found in environment!")
                return config

            else:
                return _set_offline(
                    config,
                    "\n\t\t...Vertex AI settings NOT FOUND in environment...",
                )

        else:
            if llm_engine == ModelOptions.OFFLINE.name:
                message = "\n\t\t...Offline mode enabled by user..."
            else:
                message = "Invalid LLM API service provided!"
            return _set_offline(config, message)


def _scan_environ(keys: list[str]) -> bool:
    """Check if both keys in the tuple exist in the os.environ."""
    _logger.debug(f"Scanning environment for keys: {keys}")

    for _, key in enumerate(keys):
        if key not in os.environ:
            _logger.debug(f"LLM Secret Key not found: {key}!")
            return False
        else:
            _logger.debug(f"LLM Secret Key found: {key}!")

    return True


def _set_offline(config: Settings, log_msg: str) -> Settings:
    """Set the LLM service to offline mode."""
    _logger.warning(
        f"{log_msg}\n\t\t...Generating README.md in offline mode...\n"
    )
    config.llm.api = ModelOptions.OFFLINE.name
    config.llm.offline = True
    return config
