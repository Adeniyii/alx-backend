#!/usr/bin/env python3
"""
0-basic-cache.py implements a class `BasicCache` that
inherits from `BaseCaching` and is a caching system.
"""
from cache.base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache datastructure."""

    def put(self, key, item):
        """Inserts an item into the cache using a simple caching algo."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache using a simple caching algo."""
        if key is None:
            return
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
