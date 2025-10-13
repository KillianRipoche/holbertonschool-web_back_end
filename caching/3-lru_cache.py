#!/usr/bin/python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system
    This cache uses the LRU (Least Recently Used) algo
    """

    def __init__(self):
        """
        Initialize the LRU cache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using LRU algo

        Args:
            key: the key
            item: the value to store
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key

        Args:
            key: the key to look up

        Returns:
            The value associated with key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value

        return value
