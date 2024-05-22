#!/usr/bin/env python3
"""
This module contains the LFUCache class that implements
an LFU (Least Frequently Used) caching system.
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is a caching system.

    This caching system uses an LFU (Least Frequently Used) algorithm to manage
    the cache. When the cache exceeds the maximum number of items, the least
    frequently used entry is discarded. If there is a tie, the least recently
    used entry among them is discarded.
    """

    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """
        Assign the item value to the key key in self.cache_data.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the least frequently used item is discarded.
        If there is a tie in frequency, the least recently used item is discarded.

        Args:
            key (str): The key to store in the cache.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                candidates = [k for k, v in self.frequency.items() if v == min_freq]
                
                # Among the candidates, find the least recently used item
                if len(candidates) > 1:
                    lru_key = None
                    for k in self.usage_order:
                        if k in candidates:
                            lru_key = k
                            break
                else:
                    lru_key = candidates[0]

                # Discard the least frequently used, and if tie, least recently used item
                if lru_key is not None:
                    print(f"DISCARD: {lru_key}")
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    self.usage_order.remove(lru_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.

        If the key is found, increment its frequency and update its usage order.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            The value associated with key if it exists, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
