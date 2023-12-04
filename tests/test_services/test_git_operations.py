"""Unit tests for git operations methods."""

import shutil
import tempfile
from pathlib import Path
from unittest import TestCase, mock

import pytest

from readmeai.services.git_operations import (
    clone_repo_to_temp_dir,
    find_git_executable,
    validate_file_permissions,
    validate_git_executable,
)


class GitOperationsTestCase(TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_clone_repo_to_temp_dir(self):
        repo_path = "https://github.com/eli64s/readmeai-ui"
        temp_dir = clone_repo_to_temp_dir(repo_path)
        self.assertIsInstance(temp_dir, Path)
        self.assertTrue(temp_dir.exists())

    def test_find_git_executable(self):
        git_exec_path = find_git_executable()
        self.assertIsInstance(git_exec_path, Path)
        self.assertTrue(git_exec_path.exists())

    @mock.patch("readmeai.services.git_operations.platform")
    def test_validate_git_executable(self, mock_platform):
        mock_platform.system.return_value = "Linux"
        git_exec_path = "/usr/bin/git"
        validate_git_executable(git_exec_path)
        self.assertIsInstance(git_exec_path, str)

    def test_validate_file_permissions(self):
        mock_file = mock.MagicMock()
        mock_file.stat.return_value.st_mode = 0o644
        with pytest.raises(SystemExit) as exc_info:
            validate_file_permissions(mock_file)
        assert exc_info.type == SystemExit
