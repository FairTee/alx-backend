#!/usr/bin/env python3
"""
This module contains the BasicCache class that implements
a simple caching system without any limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and is a caching system.

    This caching system has no limit and allows storing and retrieving values
    using a simple dictionary.
    """

    def put(self, key, item):
        """
        Assigns the item value to the key key in self.cache_data.

        Args:
            key (str): The key to store in the cache.
            item (any): The item to store in the cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with key if it exists, None otherwise.
        """
        return self.cache_data.get(key)
