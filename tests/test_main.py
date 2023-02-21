# tests/test_main.py
from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch

import pytest

import main


@pytest.fixture
def mock_conf_dict():
    return {
        "github": {"url": "https://github.com/myproject", "file_type": "py"},
        "paths": {"docs": "docs/"},
        "api": {"engine": "davinci-codex"},
    }


@pytest.fixture
def mock_files():
    return {"packages": ["package1", "package2"], "extensions": ["ext1", "ext2"]}


@patch("main.LOGGER")
@patch("main.dacite")
@patch("main.processor.clone_codebase")
@patch("main.model.code_to_text")
@patch("main.builder.build")
@patch("main.FileFactory")
def test_main(
    mock_FileFactory,
    mock_builder_build,
    mock_model_code_to_text,
    mock_processor_clone_codebase,
    mock_dacite,
    mock_LOGGER,
    mock_conf_dict,
    mock_files,
):
    mock_conf = Mock()
    mock_conf.github.url = mock_conf_dict["github"]["url"]
    mock_conf.github.file_type = mock_conf_dict["github"]["file_type"]
    mock_conf.paths.docs = mock_conf_dict["paths"]["docs"]
    mock_conf.api.engine = mock_conf_dict["api"]["engine"]
    mock_dacite.from_dict.return_value = mock_conf

    mock_path = Mock()
    mock_path.resolve.return_value = Path("conf/conf.toml")
    mock_FileFactory.return_value.get_handler.return_value.read_file.return_value = (
        mock_conf_dict
    )

    mock_processor_clone_codebase.return_value = mock_files

    mock_model_code_to_text.return_value = "This is a code summary."

    mock_csv_file = Mock()
    mock_FileFactory.return_value.get_handler.return_value = mock_csv_file

    main.main()

    mock_LOGGER.warning.assert_any_call("PydocsAI processing has begun.")
    mock_LOGGER.warning.assert_any_call("PydocsAI processing complete.")
    mock_LOGGER.warning.assert_any_call("Find your project readme docs ➡️ docs/*")

    mock_path.resolve.assert_called_once()
    mock_FileFactory.assert_called_once_with(mock_path.resolve.return_value)
    mock_FileFactory.return_value.get_handler.assert_called_once()
    mock_FileFactory.return_value.get_handler.return_value.read_file.assert_called_once()

    mock_dacite.from_dict.assert_called_once_with(main.AppConfig, mock_conf_dict)

    mock_processor_clone_codebase.assert_called_once_with(
        mock_conf_dict["github"]["file_type"], mock_conf_dict["github"]["url"]
    )

    mock_model_code_to_text.assert_called_once_with(
        mock_conf_dict["api"]["engine"], mock_files
    )

    mock_FileFactory.return_value.get_handler.assert_called_with(
        mock_conf_dict["paths"]["docs"]
    )
    mock_csv_file.write_file.assert_called_once_with("This is a code summary.")

    mock_builder_build.assert_called_once_with(
        mock_conf,
        mock_files["packages"] + mock_files["extensions"],
        mock_conf_dict["github"]["url"],
    )
