"""Unit tests for preprocess.py."""

import os

import git
import pytest

from src.preprocess_helper import (
    add_space_between_sentences,
    get_file_contents,
    get_local_codebase,
    get_project_dependencies,
    get_repo_name,
    make_temp_directory,
    remove_comments,
)


def test_add_space_between_sentences():
    assert add_space_between_sentences("This is a sentence.") == "This is a sentence."
    assert (
        add_space_between_sentences("This is a sentence. Here is another sentence.")
        == "This is a sentence. Here is another sentence."
    )


def test_clone_codebase():
    with make_temp_directory() as temp_dir:
        git.Repo.clone_from("https://github.com/bard/pytorch-lightning", temp_dir)
        assert os.path.isdir(temp_dir)


def test_get_file_contents():
    with make_temp_directory() as temp_dir:
        with open(os.path.join(temp_dir, "README.md"), "w") as f:
            f.write("This is a README file.")

        contents = get_file_contents(temp_dir)
        assert contents["README.md"] == "This is a README file."


def test_get_local_codebase():
    with make_temp_directory() as temp_dir:
        with open(os.path.join(temp_dir, "README.md"), "w") as f:
            f.write("This is a README file.")

        contents = get_local_codebase(temp_dir)
        assert contents["README.md"] == "This is a README file."


def test_get_project_dependencies():
    with make_temp_directory() as temp_dir:
        with open(os.path.join(temp_dir, "requirements.txt"), "w") as f:
            f.write("numpy\npandas")

        dependencies = get_project_dependencies(temp_dir, ["requirements.txt"])
        assert dependencies == ["numpy", "pandas"]


def test_get_repo_name():
    assert (
        get_repo_name("https://github.com/bard/pytorch-lightning")
        == "pytorch-lightning"
    )
    assert get_repo_name("/home/bard/code/pytorch-lightning") == "pytorch-lightning"


def test_make_temp_directory():
    with make_temp_directory() as temp_dir:
        assert os.path.isdir(temp_dir)


def test_remove_comments():
    assert remove_comments("# This is a comment.") == ""
    assert remove_comments("This is not a comment.") == "This is not a comment."


if __name__ == "__main__":
    pytest.main()
