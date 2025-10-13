#!/usr/bin/python3
"""
MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching
    This cache uses the MRU (Most Recently Used) algo
    """

    def __init__(self):
        """
        Initialize the MRU cache by calling the parent constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.

        Args:
            key: The key under which to store the item
            item: The value to store
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key

        Args:
            key: The key to look up

        Returns:
            The value associated with key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value

        return value
