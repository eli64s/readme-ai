"""Unit tests for enums and configuration settings."""

import pytest

from readmeai.config.enums import BadgeOptions, GitService, ImageOptions


@pytest.mark.parametrize(
    "service, expected_api_url",
    [
        (GitService.LOCAL, None),
        (GitService.GITHUB, "https://api.github.com/repos/"),
        (GitService.GITLAB, "https://api.gitlab.com/v4/projects/"),
        (GitService.BITBUCKET, "https://api.bitbucket.org/2.0/repositories/"),
    ],
)
def test_git_service_api_url(service, expected_api_url):
    """Test the API URL for the Git service."""
    assert service.api_url == expected_api_url


@pytest.mark.parametrize(
    "service, expected_file_url_template",
    [
        (GitService.LOCAL, "{file_path}"),
        (
            GitService.GITHUB,
            "https://github.com/{full_name}/blob/master/{file_path}",
        ),
        (
            GitService.GITLAB,
            "https://gitlab.com/{full_name}/-/blob/master/{file_path}",
        ),
        (
            GitService.BITBUCKET,
            "https://bitbucket.org/{full_name}/src/master/{file_path}",
        ),
    ],
)
def test_git_service_file_url_template(service, expected_file_url_template):
    """Test the file URL template for the Git service."""
    assert service.file_url_template == expected_file_url_template


def test_badge_options():
    """Test the CLI options for badge icons."""
    assert BadgeOptions.DEFAULT == "default"
    assert BadgeOptions.FLAT == "flat"
    assert BadgeOptions.FLAT_SQUARE == "flat-square"
    assert BadgeOptions.FOR_THE_BADGE == "for-the-badge"
    assert BadgeOptions.PLASTIC == "plastic"
    assert BadgeOptions.SKILLS == "skills"
    assert BadgeOptions.SKILLS_LIGHT == "skills-light"
    assert BadgeOptions.SOCIAL == "social"


def test_image_options():
    """Test the CLI options for header images."""
    assert ImageOptions.CUSTOM == "CUSTOM"
    assert isinstance(ImageOptions.DEFAULT, str)
    assert isinstance(ImageOptions.BLACK, str)
