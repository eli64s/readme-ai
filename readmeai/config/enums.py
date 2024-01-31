"""Enum classes for the readme-ai CLI."""

from enum import Enum


class GitService(str, Enum):
    """
    Enum class for Git service details.
    """

    LOCAL = "local"
    GITHUB = "github.com"
    GITLAB = "gitlab.com"
    BITBUCKET = "bitbucket.org"

    @property
    def api_url(self):
        """Gets the API URL for the Git service."""
        return {
            GitService.LOCAL: None,
            GitService.GITHUB: "https://api.github.com/repos/",
            GitService.GITLAB: "https://api.gitlab.com/v4/projects/",
            GitService.BITBUCKET: "https://api.bitbucket.org/2.0/repositories/",
        }.get(self)

    @property
    def file_url_template(self):
        """Gets the file URL template for the Git service."""
        return {
            GitService.LOCAL: "{file_path}",
            GitService.GITHUB: "https://github.com/{full_name}/blob/master/{file_path}",
            GitService.GITLAB: "https://gitlab.com/{full_name}/-/blob/master/{file_path}",
            GitService.BITBUCKET: "https://bitbucket.org/{full_name}/src/master/{file_path}",
        }.get(self)


class BadgeOptions(str, Enum):
    """
    Enum for CLI options for README file badge icons.
    """

    DEFAULT = "default"
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    FOR_THE_BADGE = "for-the-badge"
    PLASTIC = "plastic"
    SKILLS = "skills"
    SKILLS_LIGHT = "skills-light"
    SOCIAL = "social"


class ImageOptions(str, Enum):
    """
    Enum for CLI options for README file header images.
    """

    CUSTOM = "CUSTOM"
    BLACK = "https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png"
    BLUE = "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
    CLOUD = "https://cdn-icons-png.flaticon.com/512/6295/6295417.png"
    GRADIENT = "https://img.icons8.com/?size=512&id=55494&format=png"
    GREY = "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png"
    PURPLE = "https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png"
