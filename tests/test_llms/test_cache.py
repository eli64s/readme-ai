"""Tests for the cache manager module."""

from unittest.mock import patch

import pytest

from readmeai.llms.cache import CacheManager


@pytest.fixture
def cache_manager():
    return CacheManager(max_size=2, default_ttl=3600)


def test_cache_initialization(cache_manager):
    assert cache_manager.max_size == 2
    assert cache_manager.default_ttl == 3600
    assert len(cache_manager.cache) == 0


def test_cache_set_and_get(cache_manager):
    cache_manager.set("index1", "prompt1", 10, "response1")
    assert cache_manager.get(("index1", "prompt1", 10)) == "response1"


def test_cache_eviction(cache_manager):
    cache_manager.set("index1", "prompt1", 10, "response1")
    cache_manager.set("index2", "prompt2", 20, "response2")
    cache_manager.set("index3", "prompt3", 30, "response3")
    # Assuming FIFO eviction policy
    assert cache_manager.get(("index1", "prompt1", 10)) is None
    assert cache_manager.get(("index2", "prompt2", 20)) == "response2"
    assert cache_manager.get(("index3", "prompt3", 30)) == "response3"


def test_cache_expiration(cache_manager):
    patch("time.time", return_value=0)
    cache_manager.set("index", "prompt", 10, "response")
    patch("time.time", return_value=3601)
    assert cache_manager.get(("index", "prompt", 10)) == "response"


def test_cache_clear(cache_manager):
    cache_manager.set("index", "prompt", 10, "response")
    cache_manager.clear()
    assert len(cache_manager.cache) == 0
