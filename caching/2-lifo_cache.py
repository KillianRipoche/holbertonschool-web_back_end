#!/usr/bin/python3
"""
LIFOCache module - A caching system using LIFO algorithm
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache is a caching systel thats uses the LIFO algo (Last in First out)
    """

    def __init__(self):
        """
        Initialize the LIFO
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using LIFO

        Args:
            key: the key under which to store the item
            item: the value to store
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache of key

        Args:
            key: the key to look up

        Returns:
            the value associated with key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
