"""Configuration constants for the application."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from cachetools import TTLCache, cached

from file_factory import FileHandler
from logger import Logger

LOGGER = Logger("readmeai_logger")


@dataclass
class OpenAI:
    api_key: str
    prompt_intro: str
    prompt_slogan: str


@dataclass
class Git:
    local: str
    name: str
    path: str
    remote: str


@dataclass
class Markdown:
    close: str
    head: str
    intro: str
    dropdown: str
    modules: str
    setup: str
    slogan: str
    toc: str
    tree: str


@dataclass
class Paths:
    file_extensions: str
    file_names: str
    ignore_files: str
    setup_guide: str
    badges: str
    docs: str
    md: str


@dataclass
class AppConf:
    api: OpenAI
    git: Git
    md: Markdown
    paths: Paths


@dataclass
class AppConfHelper:
    file_names: List[str]
    file_extensions: Dict[str, str]
    ignore_files: List[str]
    setup: Dict[str, str]


@cached(TTLCache(maxsize=1024, ttl=300))
def read_config_file(path: Path) -> Dict[str, str]:
    handler = FileHandler()
    return handler.read(path)


def load_conf_helper(conf: AppConf) -> AppConfHelper:
    handler = FileHandler()
    file_names, file_extensions, ignore_files, setup = read_helper_configurations(
        handler, conf
    )

    return AppConfHelper(
        file_names=file_names,
        file_extensions=file_extensions,
        ignore_files=ignore_files,
        setup=setup,
    )


def read_helper_configurations(handler: FileHandler, conf: AppConf):
    conf_path_list = [
        conf.paths.file_names,
        conf.paths.file_extensions,
        conf.paths.ignore_files,
        conf.paths.setup_guide,
    ]

    file_extensions = {}
    file_names = []
    ignore_files = []
    setup = {}

    for path in conf_path_list:
        path = Path("conf/").joinpath(path).resolve()
        conf_dict = handler.read(path)
        update_helper_configurations(
            file_names, file_extensions, ignore_files, setup, conf_dict
        )

    return file_names, file_extensions, ignore_files, setup


def update_helper_configurations(
    file_names, file_extensions, ignore_files, setup, conf_dict
):
    if "file_names" in conf_dict:
        file_names.extend(conf_dict["file_names"].get("name", []))

    if "file_extensions" in conf_dict:
        file_extensions.update(conf_dict["file_extensions"])

    if "ignore_files" in conf_dict:
        ignore_files.extend(conf_dict["ignore_files"].get("ignore", []))

    if "setup" in conf_dict:
        setup.update(conf_dict["setup"])
