#!/usr/bin/env python3
"""
This module contains the FIFOCache class that implements
a FIFO caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system.

    This caching system uses a FIFO (First In, First Out) algorithm to manage
    the cache. When the cache exceeds the maximum number of items, the oldest
    entry is discarded.
    """

    def __init__(self):
        """Initialize the FIFOCache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign the item value to the key key in self.cache_data.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the oldest item is discarded.

        Args:
            key (str): The key to store in the cache.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in_key = self.order.pop(0)
                del self.cache_data[first_in_key]
                print(f"DISCARD: {first_in_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with key if it exists, None otherwise.
        """
        return self.cache_data.get(key)
