"""Custom cache manager for handling LLM responses."""

import hashlib
import time
from threading import Lock
from typing import Any, Dict, Optional, Tuple

from readmeai.core.logger import Logger

logger = Logger(__name__)


class CacheManager:
    """Manages caching of LLM responses with optional expiry times."""

    def __init__(self, max_size: int = 1000, default_ttl: int = 3600):
        """Initializes the cache manager."""
        self.cache: Dict[str, Tuple[Any, float]] = {}
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.lock = Lock()

    def _hash_key(self, key: Tuple[str, str, int]) -> str:
        """Creates a hash of the key for efficient storage."""
        key_str = f"{key[0]}-{key[1]}-{key[2]}"
        return hashlib.md5(key_str.encode()).hexdigest()

    def get(self, cache_key: str) -> Optional[Any]:
        """Retrieves a response from the cache if available and not expired."""
        key = self._hash_key(cache_key)
        with self.lock:
            cached = self.cache.get(key)
            if cached and (time.time() - cached[1]) < self.default_ttl:
                # logger.info(f"Cache hit for key: {key}")
                return cached[0]
            elif cached:
                # logger.debug(f"Cache expired for key: {key}")
                del self.cache[key]

        # logger.debug(f"Cache miss for key: {key}")
        return None

    def set(self, index: str, prompt: str, tokens: int, response: Any) -> None:
        """Adds a new response to the cache, respecting the max size limit."""
        key = self._hash_key((index, prompt, tokens))
        with self.lock:
            if len(self.cache) >= self.max_size:
                self._evict_oldest()
            self.cache[key] = (response, time.time())
            # logger.debug(f"Cache updated for key: {key}")

    def _evict_oldest(self) -> None:
        """Evicts the oldest item from the cache."""
        oldest_key = min(self.cache, key=lambda k: self.cache[k][1])
        del self.cache[oldest_key]
        # logger.debug(f"Evicted oldest cache item: {oldest_key}")

    def clear(self) -> None:
        """Clears the entire cache."""
        with self.lock:
            self.cache.clear()
            # logger.info("Cache has been cleared.")
