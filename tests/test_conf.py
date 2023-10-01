import unittest
from unittest.mock import MagicMock, patch

from readmeai.core.config import (
    ApiConfig,
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    DefaultHosts,
    GitConfig,
    MarkdownConfig,
    PathsConfig,
    PromptsConfig,
    load_config,
    load_config_helper,
)


class TestApiConfig(unittest.TestCase):
    def test_api_config(self):
        api_config = ApiConfig(
            endpoint="https://api.openai.com/v1",
            engine="davinci-codex",
            encoding="utf-8",
            rate_limit=5000,
            tokens=1000,
            tokens_max=2000,
            temperature=0.5,
            offline_mode=False,
        )

        self.assertEqual(api_config.endpoint, "https://api.openai.com/v1")
        self.assertEqual(api_config.engine, "davinci-codex")
        self.assertEqual(api_config.encoding, "utf-8")
        self.assertEqual(api_config.rate_limit, 5000)
        self.assertEqual(api_config.tokens, 1000)
        self.assertEqual(api_config.tokens_max, 2000)
        self.assertEqual(api_config.temperature, 0.5)
        self.assertEqual(api_config.offline_mode, False)


class TestGitConfig(unittest.TestCase):
    def test_git_config(self):
        git_config = GitConfig(
            repository="https://github.com/user/repo.git", name="repo"
        )

        self.assertEqual(
            git_config.repository, "https://github.com/user/repo.git"
        )
        self.assertEqual(git_config.name, "repo")

    def test_validate_repository(self):
        git_config = GitConfig(repository="https://github.com/user/repo.git")

        with self.assertRaises(ValueError):
            git_config.repository = "invalid_url"

        with self.assertRaises(ValueError):
            git_config.repository = "https://github.com/user/repo"

        with self.assertRaises(ValueError):
            git_config.repository = "https://gitlab.com/user/repo"

        with self.assertRaises(ValueError):
            git_config.repository = "https://github.com/user/repo/invalid"

        with self.assertRaises(ValueError):
            git_config.repository = "/path/to/repo"

        git_config.repository = "/path/to/repo/"
        self.assertEqual(git_config.repository, "/path/to/repo/")

        git_config.repository = "https://github.com/user/repo.git"
        self.assertEqual(
            git_config.repository, "https://github.com/user/repo.git"
        )

    def test_get_repository_name(self):
        git_config = GitConfig(repository="https://github.com/user/repo.git")

        self.assertEqual(git_config.name, "repo")

        git_config.repository = "https://github.com/user/repo"
        self.assertEqual(git_config.name, "repo")

        git_config.repository = "https://github.com/user/repo/"
        self.assertEqual(git_config.name, "repo")

        git_config.repository = "/path/to/repo"
        self.assertEqual(git_config.name, "repo")

        git_config.repository = "/path/to/repo/"
        self.assertEqual(git_config.name, "repo")


class TestMarkdownConfig(unittest.TestCase):
    def test_markdown_config(self):
        markdown_config = MarkdownConfig(
            badges="badges",
            default="default",
            dropdown="dropdown",
            ending="ending",
            header="header",
            intro="intro",
            modules="modules",
            setup="setup",
            tables="tables",
            toc="toc",
            tree="tree",
        )

        self.assertEqual(markdown_config.badges, "badges")
        self.assertEqual(markdown_config.default, "default")
        self.assertEqual(markdown_config.dropdown, "dropdown")
        self.assertEqual(markdown_config.ending, "ending")
        self.assertEqual(markdown_config.header, "header")
        self.assertEqual(markdown_config.intro, "intro")
        self.assertEqual(markdown_config.modules, "modules")
        self.assertEqual(markdown_config.setup, "setup")
        self.assertEqual(markdown_config.tables, "tables")
        self.assertEqual(markdown_config.toc, "toc")
        self.assertEqual(markdown_config.tree, "tree")


class TestPathsConfig(unittest.TestCase):
    def test_paths_config(self):
        paths_config = PathsConfig(
            badges="badges",
            dependency_files="dependency_files",
            ignore_files="ignore_files",
            language_names="language_names",
            language_setup="language_setup",
            readme="readme",
        )

        self.assertEqual(paths_config.badges, "badges")
        self.assertEqual(paths_config.dependency_files, "dependency_files")
        self.assertEqual(paths_config.ignore_files, "ignore_files")
        self.assertEqual(paths_config.language_names, "language_names")
        self.assertEqual(paths_config.language_setup, "language_setup")
        self.assertEqual(paths_config.readme, "readme")


class TestPromptsConfig(unittest.TestCase):
    def test_prompts_config(self):
        prompts_config = PromptsConfig(
            code_summary="code_summary",
            features="features",
            overview="overview",
            slogan="slogan",
        )

        self.assertEqual(prompts_config.code_summary, "code_summary")
        self.assertEqual(prompts_config.features, "features")
        self.assertEqual(prompts_config.overview, "overview")
        self.assertEqual(prompts_config.slogan, "slogan")


class TestAppConfig(unittest.TestCase):
    def test_app_config(self):
        api_config = ApiConfig(
            endpoint="https://api.openai.com/v1",
            engine="davinci-codex",
            encoding="utf-8",
            rate_limit=5000,
            tokens=1000,
            tokens_max=2000,
            temperature=0.5,
            offline_mode=False,
        )

        git_config = GitConfig(
            repository="https://github.com/user/repo.git", name="repo"
        )

        markdown_config = MarkdownConfig(
            badges="badges",
            default="default",
            dropdown="dropdown",
            ending="ending",
            header="header",
            intro="intro",
            modules="modules",
            setup="setup",
            tables="tables",
            toc="toc",
            tree="tree",
        )

        paths_config = PathsConfig(
            badges="badges",
            dependency_files="dependency_files",
            ignore_files="ignore_files",
            language_names="language_names",
            language_setup="language_setup",
            readme="readme",
        )

        prompts_config = PromptsConfig(
            code_summary="code_summary",
            features="features",
            overview="overview",
            slogan="slogan",
        )

        app_config = AppConfig(
            api=api_config,
            git=git_config,
            md=markdown_config,
            paths=paths_config,
            prompts=prompts_config,
        )

        self.assertEqual(app_config.api, api_config)
        self.assertEqual(app_config.git, git_config)
        self.assertEqual(app_config.md, markdown_config)
        self.assertEqual(app_config.paths, paths_config)
        self.assertEqual(app_config.prompts, prompts_config)


class TestAppConfigModel(unittest.TestCase):
    def test_app_config_model(self):
        api_config = ApiConfig(
            endpoint="https://api.openai.com/v1",
            engine="davinci-codex",
            encoding="utf-8",
            rate_limit=5000,
            tokens=1000,
            tokens_max=2000,
            temperature=0.5,
            offline_mode=False,
        )

        git_config = GitConfig(
            repository="https://github.com/user/repo.git", name="repo"
        )

        markdown_config = MarkdownConfig(
            badges="badges",
            default="default",
            dropdown="dropdown",
            ending="ending",
            header="header",
            intro="intro",
            modules="modules",
            setup="setup",
            tables="tables",
            toc="toc",
            tree="tree",
        )

        paths_config = PathsConfig(
            badges="badges",
            dependency_files="dependency_files",
            ignore_files="ignore_files",
            language_names="language_names",
            language_setup="language_setup",
            readme="readme",
        )

        prompts_config = PromptsConfig(
            code_summary="code_summary",
            features="features",
            overview="overview",
            slogan="slogan",
        )

        app_config = AppConfig(
            api=api_config,
            git=git_config,
            md=markdown_config,
            paths=paths_config,
            prompts=prompts_config,
        )

        app_config_model = AppConfigModel(app=app_config)

        self.assertEqual(app_config_model.app, app_config)


class TestConfigHelper(unittest.TestCase):
    def test_config_helper(self):
        api_config = ApiConfig(
            endpoint="https://api.openai.com/v1",
            engine="davinci-codex",
            encoding="utf-8",
            rate_limit=5000,
            tokens=1000,
            tokens_max=2000,
            temperature=0.5,
            offline_mode=False,
        )

        git_config = GitConfig(
            repository="https://github.com/user/repo.git", name="repo"
        )

        markdown_config = MarkdownConfig(
            badges="badges",
            default="default",
            dropdown="dropdown",
            ending="ending",
            header="header",
            intro="intro",
            modules="modules",
            setup="setup",
            tables="tables",
            toc="toc",
            tree="tree",
        )

        paths_config = PathsConfig(
            badges="badges",
            dependency_files="dependency_files",
            ignore_files="ignore_files",
            language_names="language_names",
            language_setup="language_setup",
            readme="readme",
        )

        prompts_config = PromptsConfig(
            code_summary="code_summary",
            features="features",
            overview="overview",
            slogan="slogan",
        )

        app_config = AppConfig(
            api=api_config,
            git=git_config,
            md=markdown_config,
            paths=paths_config,
            prompts=prompts_config,
        )

        app_config_model = AppConfigModel(app=app_config)

        with patch(
            "readmeai.conf._get_config_dict",
            MagicMock(return_value={"dependency_files": ["file1", "file2"]}),
        ):
            config_helper = ConfigHelper(conf=app_config_model)

        self.assertEqual(config_helper.conf, app_config_model)
        self.assertEqual(config_helper.dependency_files, ["file1", "file2"])
        self.assertEqual(config_helper.ignore_files, {})
        self.assertEqual(config_helper.language_names, {})
        self.assertEqual(config_helper.language_setup, {})
