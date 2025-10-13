#!/usr/bin/python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that uses the FIFO algo
    """

    def __init__(self):
        """
        Initialize the FIFO cache by calling the parent constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algo

        Args:
            key: they key under
            item: the value to store
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

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



