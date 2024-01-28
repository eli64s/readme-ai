"""Git operations for cloning and validating repositories."""

import os
import platform
import shutil
from pathlib import Path
from typing import Optional

import git

from readmeai.config.enums import GitService
from readmeai.core.logger import Logger
from readmeai.exceptions import GitCloneError

logger = Logger(__name__)


async def clone_repository(repository: str, temp_dir: str) -> str:
    """Clone repository to temporary directory and return the path."""
    try:
        temp_dir_path = Path(temp_dir)
        if not temp_dir_path.exists():
            temp_dir_path.mkdir(parents=True)

        if Path(repository).is_dir():
            repo = git.Repo.init(temp_dir)
            origin = repo.create_remote(
                "origin", f"file://{Path(repository).absolute()}"
            )
            repo.git.config("core.sparseCheckout", "true")

            sparse_checkout_path = (
                temp_dir_path / ".git" / "info" / "sparse-checkout"
            )
            with sparse_checkout_path.open("w") as sc_file:
                sc_file.write("/*\n!.git/\n")

            origin.fetch()
            repo.git.checkout("FETCH_HEAD")
        else:
            git.Repo.clone_from(
                repository, temp_dir, depth=1, single_branch=True
            )

        await remove_hidden_contents(temp_dir_path)

        return temp_dir

    except (
        git.GitCommandError,
        git.InvalidGitRepositoryError,
        git.NoSuchPathError,
    ) as exc:
        raise GitCloneError(f"Error cloning repository: {str(exc)}") from exc


async def remove_hidden_contents(directory: Path) -> None:
    """Remove hidden files and directories from a specified directory."""
    for item in directory.iterdir():
        if item.name.startswith(".") and item.name != ".github":
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()


async def fetch_git_api_url(repo_url: str) -> str:
    """Parses the repository URL and returns the API URL."""
    try:
        parts = repo_url.rstrip("/").split("/")
        repo_name = f"{parts[-2]}/{parts[-1]}"
        for service in GitService:
            if service in repo_url:
                api_url = f"{service.api_url}{repo_name}"
                logger.info(f"{service.name.upper()} API URL: {api_url}")
                return api_url

        raise ValueError("Unsupported Git service.")

    except (IndexError, ValueError) as exc:
        raise ValueError(f"Invalid repository URL: {repo_url}") from exc


def fetch_git_file_url(file_path: str, full_name: str, repo_url: str) -> str:
    """Returns the URL of the file in the remote repository."""
    if Path(repo_url).exists():
        return GitService.LOCAL.file_url_template.format(file_path=file_path)

    for service in GitService:
        if service in repo_url:
            return service.file_url_template.format(
                full_name=full_name, file_path=file_path
            )

    return file_path


def find_git_executable() -> Optional[Path]:
    """Find the path to the git executable, if available."""
    try:
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

    except Exception as exc:
        raise ValueError("Error finding Git executable") from exc


def validate_file_permissions(temp_dir: Path) -> None:
    """Validates file permissions of the cloned repository."""
    try:
        if platform.system() != "Windows":
            permissions = temp_dir.stat().st_mode & 0o777
            if permissions != 0o700:
                raise SystemExit(
                    f"Invalid file permissions for {temp_dir}.\n"
                    f"Expected 0o700, but found {oct(permissions)}."
                )

    except Exception as exc:
        raise ValueError(
            f"Error validating file permissions: {str(exc)}"
        ) from exc


def validate_git_executable(git_exec_path: str) -> None:
    """Validate the path to the git executable."""
    try:
        if not git_exec_path or not Path(git_exec_path).exists():
            raise ValueError(f"Git executable not found at {git_exec_path}")

    except Exception as exc:
        raise ValueError("Error validating Git executable path") from exc
