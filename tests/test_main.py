"""Test the main module of the package."""

import asyncio
from unittest.mock import MagicMock, patch

import pytest

from readmeai.main import readme_agent


@pytest.mark.asyncio
async def test_readme_agent():
    """Test the readme_agent function."""
    with patch("readmeai.main.clone_repo_to_temp_dir") as mock_clone, patch(
        "readmeai.main.build_readme_md"
    ) as mock_build_readme, patch(
        "readmeai.main.shutil.rmtree"
    ) as mock_rmtree, patch(
        "readmeai.main.Logger"
    ) as mock_logger:
        mock_clone.return_value = asyncio.Future()
        mock_clone.return_value.set_result(None)
        conf = MagicMock()
        conf_helper = MagicMock()
        conf.llm.rate_limit = 10
        await readme_agent(conf, conf_helper)
        mock_build_readme.assert_called_once()
        mock_rmtree.assert_called_once()
