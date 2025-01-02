import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.offline import OfflineHandler


@pytest.fixture
def offline_handler(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    """Fixture to provide an OfflineHandler instance."""
    return OfflineHandler(mock_config_loader, mock_repository_context)


@pytest.mark.asyncio
async def test_make_request_no_files(offline_handler: OfflineHandler):
    """Test `_make_request` when `repo_files` is None or empty."""
    # When `repo_files` is None
    result = await offline_handler._make_request(
        index=None, prompt=None, tokens=None, repo_files=None
    )
    assert result == [(offline_handler.placeholder, offline_handler.placeholder)]

    # When `repo_files` is an empty list
    result = await offline_handler._make_request(
        index=None, prompt=None, tokens=None, repo_files=[]
    )
    assert result == [(offline_handler.placeholder, offline_handler.placeholder)]


@pytest.mark.asyncio
async def test_make_request_with_files(offline_handler: OfflineHandler):
    """Test `_make_request` when `repo_files` contains file data."""
    repo_files = [("file1.txt", "Some content"), ("file2.py", "Other content")]

    result = await offline_handler._make_request(
        index=None, prompt=None, tokens=None, repo_files=repo_files
    )

    assert len(result) == len(repo_files)
    assert all(file_path == offline_handler.placeholder for _, file_path in result)
    assert [file[0] for file in result] == ["file1.txt", "file2.py"]


@pytest.mark.asyncio
async def test_build_payload(offline_handler: OfflineHandler):
    """Test `_build_payload` method."""
    payload = await offline_handler._build_payload(prompt="This is a test prompt.")
    assert payload == {}


@pytest.mark.asyncio
async def test_model_settings(offline_handler: OfflineHandler):
    """Test `_model_settings` method (no-op)."""
    result = await offline_handler._model_settings()
    assert result is None  # The method is no-op and returns nothing
