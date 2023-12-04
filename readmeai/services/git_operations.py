"""Git operations for cloning and validating repositories."""

import os
import platform
import tempfile
from pathlib import Path
from typing import Optional

import git


def clone_repo_to_temp_dir(repo_path: str) -> Path:
    """Clone user repository to a temporary directory."""
    if Path(repo_path).exists():
        return Path(repo_path)

    temp_dir = tempfile.mkdtemp()
    try:
        git.Repo.clone_from(repo_path, temp_dir, depth=1, single_branch=True)

        return Path(temp_dir)

    except git.GitCommandError as excinfo:
        raise ValueError(f"Git clone error: {excinfo}") from excinfo

    except Exception as excinfo:
        raise ValueError(
            f"Error cloning git repository: {excinfo}"
        ) from excinfo


def find_git_executable() -> Optional[Path]:
    """Find the path to the git executable, if available."""
    git_exec_path = os.environ.get("GIT_PYTHON_GIT_EXECUTABLE")
    if git_exec_path:
        return Path(git_exec_path)

    # For Windows, set default location of git executable.
    if platform.system() == "Windows":
        default_windows_path = Path("C:\\Program Files\\Git\\cmd\\git.EXE")
        if default_windows_path.exists():
            return default_windows_path

    # For other OS, set executable path from PATH environment variable.
    paths = os.environ["PATH"].split(os.pathsep)
    for path in paths:
        git_path = Path(path) / "git"
        if git_path.exists():
            return git_path

    return None


def validate_file_permissions(temp_dir: Path) -> None:
    """Validates file permissions of the cloned repository."""
    if platform.system() != "Windows":
        if isinstance(temp_dir, str):
            temp_dir = Path(temp_dir)
        permissions = temp_dir.stat().st_mode & 0o777
        if permissions != 0o700:
            raise SystemExit(
                f"Invalid file permissions for {temp_dir}.\n"
                f"Expected 0o700, but found {oct(permissions)}."
            )


def validate_git_executable(git_exec_path: Optional[str]) -> None:
    """Validate the path to the git executable."""
    if not git_exec_path or not Path(git_exec_path).exists():
        raise ValueError(f"Git executable not found at {git_exec_path}")
