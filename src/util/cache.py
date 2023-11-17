from functools import lru_cache
from time import time

class FunctionCacher:
  def __init__(self, func, ttl_seconds=3600):
    self.ttl_seconds = ttl_seconds
    self.func = func

  @lru_cache(maxsize=None)
  def _cached_func(self, *args, ttl_hash=None):
    del ttl_hash # if argument of function is same as before, then return cached, else load computation. that's why we manipulate argument.
    return self.func(*args)

  def _get_ttl_hash(self):
    """Return the same value within `ttl_seconds` time period"""
    return round(time() / self.ttl_seconds)

  def __call__(self, *args):
    return self._cached_func(*args, ttl_hash=self._get_ttl_hash())