# tests/test_conf.py

from conf import AppConfig
from conf import GitHub
from conf import Markdown
from conf import OpenAI
from conf import Paths


def test_AppConfig():
    api = OpenAI(engine="davinci-codex", key="my_key")
    github = GitHub(file_type="py", url="https://github.com/myproject")
    md = Markdown(
        head="# My Project", body="This is my project", modules="", tree="", usage=""
    )
    paths = Paths(badges="badges/", docs="docs/", md="md/")
    app_config = AppConfig(api=api, github=github, md=md, paths=paths)

    assert app_config.api.engine == "davinci-codex"
    assert app_config.api.key == "my_key"
    assert app_config.github.file_type == "py"
    assert app_config.github.url == "https://github.com/myproject"
    assert app_config.md.head == "# My Project"
    assert app_config.md.body == "This is my project"
    assert app_config.md.modules == ""
    assert app_config.md.tree == ""
    assert app_config.md.usage == ""
    assert app_config.paths.badges == "badges/"
    assert app_config.paths.docs == "docs/"
    assert app_config.paths.md == "md/"
