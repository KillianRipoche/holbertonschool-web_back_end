#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BasicCaching.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
        Key: the key under which to store the item
        item: the value to store
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key

        Args:
        key: the key to look up

        Returns:
        the value associated with key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
