"""Unit tests for preprocess_parse.py."""

import sys

sys.path.append("src")

import json
import unittest
from tempfile import NamedTemporaryFile
from unittest.mock import mock_open, patch

import toml
import yaml

from src import parse
from src.factory import FileHandler

FILE_HANDLER = FileHandler()


def test_parse_conda_env_file():
    conda_env = {
        "dependencies": ["numpy=1.19.2", "pandas", {"scipy": "1.5.0"}]
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(yaml.dump(conda_env))
    dependencies = parse.parse_conda_env_file(temp_file.name)
    assert dependencies == ["numpy", "pandas", "scipy"]


def test_parse_pipfile():
    pipfile = {
        "packages": {"requests": "==2.25.1", "numpy": "~=1.19.2"},
        "dev-packages": {"pytest": "^6.2.2"},
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(toml.dumps(pipfile))
    dependencies = parse.parse_pipfile(temp_file.name)
    assert dependencies == ["requests", "numpy", "pytest"]


def test_parse_pyproject_toml():
    pyproject_toml = {
        "tool": {
            "poetry": {
                "dependencies": ["numpy", "requests"],
                "dev-dependencies": ["pytest"],
            }
        }
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(toml.dumps(pyproject_toml))
    dependencies = parse.parse_pyproject_toml(temp_file.name)
    assert dependencies == ["numpy", "requests", "pytest"]


def test_parse_requirements_file():
    requirements = ["numpy==1.19.2", "# A comment", "", "requests>=2.25.1"]
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write("\n".join(requirements))
    dependencies = parse.parse_requirements_file(temp_file.name)
    assert dependencies == ["numpy", "requests"]


class TestParseCargoToml(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="""
    [package]
    name = "test_package"

    [dependencies]
    dep1 = "1.0.0"
    dep2 = "2.0.0"

    [dev-dependencies]
    devdep1 = "1.0.0"
    """,
    )
    @patch("src.factory.FileHandler.read_toml")
    def test_parse_cargo_toml(self, mock_read_toml, mock_file):
        mock_read_toml.return_value = {
            "dependencies": {"dep1": "1.0.0", "dep2": "2.0.0"},
            "dev-dependencies": {"devdep1": "1.0.0"},
        }

        result = parse.parse_cargo_toml("Cargo.toml")
        self.assertListEqual(result, ["dep1", "dep2", "devdep1"])


class TestParseCargoLock(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="""
        [[package]]
        name = "aho-corasick"
        version = "0.7.20"
        source = "registry+https://github.com/rust-lang/crates.io-index"
        checksum = "cc936419f96fa211c1b9166887b38e5e40b19958e5b895be7c1f93adec7071ac"
        dependencies = [
        "memchr",
        ]

        [[package]]
        name = "ansi_term"
        version = "0.12.1"
        source = "registry+https://github.com/rust-lang/crates.io-index"
        checksum = "d52a9bb7ec0cf484c551830a7ce27bd20d67eac647e1befb56b0be4ee39a55d2"
        dependencies = [
        "winapi",
        ]
        """,
    )
    @patch("src.factory.FileHandler.read_toml")
    def test_parse_cargo_lock(self, mock_read_toml, mock_file):
        mock_read_toml.return_value = {
            "package": [
                {"name": "aho-corasick"},
                {"name": "ansi_term"},
            ]
        }
        expected_packages = ["aho-corasick", "ansi_term"]
        actual_packages = parse.parse_cargo_lock("Cargo.lock")
        self.assertEqual(expected_packages, actual_packages)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("src.factory.FileHandler.read_toml")
    def test_parse_cargo_lock_no_packages(self, mock_read_toml, mock_file):
        # Mock the read_toml function to return a data with no packages
        mock_read_toml.return_value = {}
        expected_packages = []
        actual_packages = parse.parse_cargo_lock("Cargo.lock")
        self.assertEqual(expected_packages, actual_packages)


def test_parse_package_json():
    package_json = {
        "dependencies": {"express": "^4.17.1", "lodash": "^4.17.21"},
        "devDependencies": {"mocha": "^9.0.0"},
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(package_json))
    dependencies = parse.parse_package_json(temp_file.name)
    assert dependencies == ["express", "lodash", "mocha"]


def test_parse_package_json():
    package_json = {
        "dependencies": {"express": "^4.17.1", "lodash": "^4.17.21"},
        "devDependencies": {"mocha": "^9.0.0"},
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(package_json))
    dependencies = parse.parse_package_json(temp_file.name)
    assert dependencies == ["express", "lodash", "mocha"]


class TestParseYarnLock(unittest.TestCase):
    def test_parse_yarn_lock(self):
        yarn_lock_content = """
            argparse@^1.0.7:
              version "1.0.10"
              resolved "https://registry.yarnpkg.com/argparse/-/argparse-1.0.10.tgz#bcd6791ea5ae09725e17e5ad988134cd40b3d911"
              integrity sha512-o5Roy6tNG4SL/FOkCAN6RzjiakZS25RLYFrcMttJqbdd8BWrnA+fGz57iN5Pb06pvBGvl5gQ0B48dJlslXvoTg==
              dependencies:
                sprintf-js "~1.0.2"
    
            arr-union@^3.1.0:
              version "3.1.0"
              resolved "https://registry.yarnpkg.com/arr-union/-/arr-union-3.1.0.tgz#e39b09aea9def866a8f206e288af63919bae39c4"
              integrity sha1-45sJrqne+Gao8gbiiK9jkZuuOcQ=
    
            array-filter@^1.0.0:
              version "1.0.0"
              resolved "https://registry.yarnpkg.com/array-filter/-/array-filter-1.0.0.tgz#baf79e62e6ef4c2a4c0b831232daffec251f9d83"
              integrity sha1-uveeYubvTCpMC4MSMtr/7CUfnYM=
    
            array-includes@^3.1.2:
              version "3.1.2"
              resolved "https://registry.yarnpkg.com/array-includes/-/array-includes-3.1.2.tgz#a8db03e0b88c8c6aeddc49cb132f9bcab4ebf9c8"
              integrity sha512-w2GspexNQpx+PutG3QpT437/BenZBj0M/MZGn5mzv/MofYqo0xmRHzn4lFsoDlWJ+THYsGJmFlW68WlDFx7VRw==
              dependencies:
                call-bind "^1.0.0"
                define-properties "^1.1.3"
                es-abstract "^1.18.0-next.1"
                get-intrinsic "^1.0.1"
                is-string "^1.0.5"
        """
        with NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write(yarn_lock_content)

        dependencies = parse.parse_yarn_lock(temp_file.name)
        expected_dependencies = [
            "argparse",
            "arr-union",
            "array-filter",
            "array-includes",
        ]
        self.assertEqual(dependencies, expected_dependencies)


def test_parse_go_mod():
    go_mod = """
        module example.com/mymodule

        go 1.17

        require (
            github.com/gin-gonic/gin v1.7.4
            github.com/stretchr/testify v1.7.0
        )
    """
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(go_mod)
    dependencies = parse.parse_go_mod(temp_file.name)
    assert dependencies == [
        "gin",
        "testify",
    ]


def test_parse_gradle():
    build_gradle = """
    dependencies {
        implementation("com.google.code.findbugs:annotations:3.0.1")
        implementation("com.google.guava:guava:27.1-android") {
            because("Gradle uses the android variant as well and we are running the same code there.")
        }
        implementation("com.typesafe:config:1.3.3")
        implementation("org.apache.ant:ant-compress:1.5")
    }
    """

    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(build_gradle)

    dependencies = parse.parse_gradle(temp_file.name)
    expected_dependencies = [
        "findbugs",
        "guava",
        "typesafe",
        "ant",
    ]

    assert dependencies == expected_dependencies


def test_parse_maven():
    maven_file = """
        <dependencies>
            <dependency>
                <groupId>com.google.guava</groupId>
                <artifactId>guava</artifactId>
                <version>30.1-jre</version>
            </dependency>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.13.2</version>
            </dependency>
        </dependencies>
    """
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(maven_file)
    dependencies = parse.parse_maven(temp_file.name)
    assert dependencies == [
        "com.google.guava:guava:30.1-jre",
        "junit:junit:4.13.2",
    ]


if __name__ == "__main__":
    unittest.main()
