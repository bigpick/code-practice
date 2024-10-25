#!/usr/bin/env python

# Problem:
#
# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with
# a cache size n, and contain the following methods:
#
# set(key, value): sets key to value. If there are already n items in the cache and we
# are adding a new item, then it should also remove the least recently used item.
#
# get(key): gets the value at key. If no such key exists, return null.
#
# Each operation should run in O(1) time.

from collections import OrderedDict  # , deque
from json import dumps
from typing import Any, Optional


class LruCache:
    def __init__(self, n: int) -> None:
        self.cache_size = n
        self.cache = OrderedDict()
        # self.last_inserted_key = None
        self.current_cache_size = 0
        # self.insertion_deque = deque()

    def set(self, key: str, val: Any) -> None:
        # sets key to value
        # if there are already n items in the chace and we are adding a new item, then
        # it should also remove the least recently used item
        existing = self.cache.get(key)

        if existing:
            self.cache[key] = val
            self.cache.move_to_end(key)
            # this won't work bc if the key is somewhere in the deque already, then
            # when we go to LRU it, it woudn't work
            # self.insertion_deque.append(key)
            return

        # otherwise, we _know_ it doesn't exist.
        # we need to:
        #   (1) make sure the cache isn't full
        #   (2) add the item to the cache, update the cache ordering

        # (1) make sure cache isn't full:
        if self.current_cache_size >= self.cache_size:
            # need to pop oldest
            self.cache.popitem(last=False)  # last=False is FIFO
            self.current_cache_size -= 1

        # (2) add the item to the cache, update the cache ordering
        self.cache[key] = val
        self.cache.move_to_end(key)
        self.current_cache_size += 1

    def get(self, key: str) -> Optional[Any]:
        # Gets the value at ``key`` if it exists, null else
        val = self.cache.get(key)
        if val is not None:
            self.cache.move_to_end(key)
        return val

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2)


cache = LruCache(10)
print(cache)
for i in range(20):
    cache.set(f"foo{i}", "bar")
    print(cache)
    print(cache.get(f"foo{i-1}"))
    print(cache)
