# tests/conftest.py

import pytest


@pytest.fixture(scope="function")
def test_conf():
    pass


@pytest.fixture
def my_fixture():
    return [1, 2, 3, 4, 5]
