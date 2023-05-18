"""Unit tests for preprocess_helper.py."""

import json
import os
from tempfile import NamedTemporaryFile

import toml
import yaml

from src.preprocess_helper import *


# Test list_files function
def test_list_files():
    temp_dir = os.path.dirname(os.path.abspath(__file__))
    files = list_files(temp_dir)
    assert isinstance(files, list)


# Test parse_conda_env_file function
def test_parse_conda_env_file():
    conda_env = {"dependencies": ["numpy=1.19.2", "pandas", {"scipy": "1.5.0"}]}
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(yaml.dump(conda_env))
    dependencies = parse_conda_env_file(temp_file.name)
    assert dependencies == ["numpy", "pandas", "scipy"]


# Test parse_pipfile function
def test_parse_pipfile():
    pipfile = {
        "packages": {"requests": "==2.25.1", "numpy": "~=1.19.2"},
        "dev-packages": {"pytest": "^6.2.2"},
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(pipfile))
    dependencies = parse_pipfile(temp_file)
    assert dependencies == ["requests", "numpy", "pytest"]


# Test parse_pyproject_toml function
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
    dependencies = parse_pyproject_toml(temp_file)
    assert dependencies == ["numpy", "requests", "pytest"]


# Test parse_requirements_file function
def test_parse_requirements_file():
    requirements = ["numpy==1.19.2", "# A comment", "", "requests>=2.25.1"]
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write("\n".join(requirements))
    dependencies = parse_requirements_file(temp_file.name)
    assert dependencies == ["numpy", "requests"]


# Test parse_cargo_toml function
def test_parse_cargo_toml():
    cargo_toml = {
        "dependencies": [
            'serde = { version = "1.0", features = ["derive"] }',
            'tokio = { version = "1.0", features = ["full"] }',
        ],
        "dev-dependencies": ['serde-test = "1.0"'],
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(toml.dumps(cargo_toml))
    dependencies = parse_cargo_toml(temp_file)
    assert dependencies == ["serde", "tokio", "serde-test"]


# Test parse_cargo_lock function
def test_parse_cargo_lock():
    cargo_lock = {
        "package": [
            {"name": "serde", "version": "1.0.123"},
            {"name": "tokio", "version": "1.2.0"},
        ]
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(toml.dumps(cargo_lock))
    dependencies = parse_cargo_lock(temp_file)
    assert dependencies == ["serde", "tokio"]


# Test parse_package_json function
def test_parse_package_json():
    package_json = {
        "dependencies": {"express": "^4.17.1", "lodash": "^4.17.21"},
        "devDependencies": {"mocha": "^9.0.0"},
    }
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(json.dumps(package_json))
    dependencies = parse_package_json(temp_file)
    assert dependencies == ["express", "lodash", "mocha"]


# Test parse_yarn_lock function
def test_parse_yarn_lock():
    yarn_lock = """
        # yarn lockfile v1
        lodash@^4.17.21:
          version "4.17.21"
          resolved "https://registry.yarnpkg.com/lodash/-/lodash-4.17.21.tgz#a2b9403aefc699960bca3f8ba4469b03e26fa5dc"
          integrity sha512-v2kDEe57lecTulaDIuNTPcy+sFRkL9QxNf4X0BCl2PjrVcJN01pPE7Oyqt1H0AfQsisnvAMh0bAC3urB+w65gA==

        express@^4.17.1:
          version "4.17.1"
          resolved "https://registry.yarnpkg.com/express/-/express-4.17.1.tgz#7f71610a5f114caa30b40848ed3aeca6dce04de3"
          integrity sha512-mHJ9O79RqluphRrcw2X/GTh3k9tVv8YcoyY4Kkh4WDMUYKRZUq0h1o0w2rrrxBqM7VoeUVqgb27xlEMXTnYt4g==

        mocha@^9.0.0:
          version "9.0.3"
          resolved "https://registry.yarnpkg.com/mocha/-/mocha-9.0.3.tgz#f6056a39a14a87efb6a3e75e5e73982f366505f6"
          integrity sha512-y9yTyXcK61BZ0INB9L/dL0UhybjR+VxO2G3F3wIZ8n/KpMUKJxioWQyfLjjGdUlW/2JZaeWYHp28SOH2YwS7fg==
    """
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(yarn_lock)
    dependencies = parse_yarn_lock(temp_file)
    assert dependencies == ["lodash", "express", "mocha"]


# Test parse_go_mod function
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
    dependencies = parse_go_mod(temp_file.name)
    assert dependencies == ["github.com/gin-gonic/gin", "github.com/stretchr/testify"]


# Test parse_go_sum function
def test_parse_go_sum():
    go_sum = """
        github.com/gin-gonic/gin v1.7.4 h1:abcdefg
        github.com/gin-gonic/gin v1.7.4/go.mod h1:ijklmnop
        github.com/stretchr/testify v1.7.0 h1:qrstuvwxyz
        github.com/stretchr/testify v1.7.0/go.mod h1:12345678
    """
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(go_sum)
    dependencies = parse_go_sum(temp_file.name)
    assert dependencies == ["github.com/gin-gonic/gin", "github.com/stretchr/testify"]


# Test parse_gradle function
def test_parse_gradle():
    gradle_file = """
        dependencies {
            implementation 'com.google.guava:guava:30.1-jre'
            testImplementation 'junit:junit:4.13.2'
        }
    """
    with NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(gradle_file)
    dependencies = parse_gradle(temp_file.name)
    assert dependencies == ["com.google.guava:guava:30.1-jre", "junit:junit:4.13.2"]


# Test parse_maven function
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
    dependencies = parse_maven(temp_file.name)
    assert dependencies == ["com.google.guava:guava:30.1-jre", "junit:junit:4.13.2"]
