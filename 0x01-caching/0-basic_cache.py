#!/usr/bin/env python3
"""
0-basic-cache.py implements a class `BasicCache` that
inherits from `BaseCaching` and is a caching system.
"""
from cache.base_caching import BaseCaching

class BasicCache(BaseCaching):
	"""A basic cache datastructure."""
	def put(self, key, item):
		if key is None or item is None:
			return
		self.cache_data[key] = item

	def get(self, key):
		if key is None:
			return
		return self.cache_data.get(key, None)