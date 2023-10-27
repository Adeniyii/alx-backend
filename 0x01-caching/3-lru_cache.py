#!/usr/bin/env python3
"""
3-lru-cache implements a `LRUCache` that inherits
from BaseCaching and is a caching system.
"""
from typing import List
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A cache mechanism implementing the LRU eviction algorithm."""
    lru_keys: List[str] = []

    def put(self, key, item):
        """Insert item using a LRU algo."""
        dk = None
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS == len(self.cache_data):
            if key not in self.cache_data.keys():
                dk = type(self).lru_keys[0]
                self.cache_data.pop(dk)
                print("DISCARD: {}".format(dk))

        self.cache_data[key] = item
        self.enqueue(key)

    def get(self, key):
        """Retrieve an item."""
        if key is None or key not in self.cache_data.keys():
            return
        self.enqueue(key)

        return self.cache_data.get(key)

    def enqueue(self, key):
        """Shift key to end of the queue."""
        type(self).lru_keys.remove(key)
        type(self).lru_keys.append(key)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
