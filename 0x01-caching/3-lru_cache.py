#!/usr/bin/env python3
"""
This module contains the LRUCache class that implements
an LRU (Least Recently Used) caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is a caching system.

    This caching system uses an LRU (Least Recently Used) algorithm to manage
    the cache. When the cache exceeds the maximum number of items, the least
    recently used entry is discarded.
    """

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign the item value to the key key in self.cache_data.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the least recently used item is discarded.

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
                least_recently_used_key = self.order.pop(0)
                del self.cache_data[least_recently_used_key]
                print(f"DISCARD: {least_recently_used_key}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        If the key is found, it is moved to the end of the order list
        to mark it as recently used.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with key if it exists, None otherwise.
        """
        value = self.cache_data.get(key)
        if value is not None:
            self.order.remove(key)
            self.order.append(key)
        return value
