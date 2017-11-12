"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import json
from collections import defaultdict
import re


class WordStore:
    """Storage container for Words."""

    def __init__(self):
        self._search = re.compile(r'(\w*)')
        self.store = defaultdict(set)

    def __add__(self, other):
        """Combine word stores with `+`."""
        combined = WordStore()
        combined += self
        combined += other
        return combined

    def __iadd__(self, other):
        """Combine word stores with `+=`."""
        for k, v in other.store.items():
            self.store[k] |= v

        return self

    def add(self, word: str):
        """Add word to store.

        Args:
            word:

        Returns:

        """
        # Strip word of unusable characters.
        matches = self._search.match(word)
        if not matches:
            return

        # Reformat, and place word in store.
        word = matches.group(1).lower()
        self.store[len(word)].add(word)

    def iter_words(self, min_len: int = 0, max_len: int = 0):
        """Iterate words in store.

        Args:
            min_len: Minimum number of characters in words to iterate.
                0 => No minimum.
            max_len: Maximum number of characters in words to iterate.
                0 => No maximum.

        Returns:

        """
        for k, v in self.store.items():
            if k >= min_len and (k <= max_len or max_len == 0):
                for word in v:
                    yield word

    @classmethod
    def from_json(cls, json_str: str):
        values = json.loads(json_str)
        words = cls()
        for k, v in values.items():
            words.store[int(k)] = set(v)

        return words

    def to_json(self) -> str:
        converted = {
            k: list(v)
            for k, v in self.store.items()
        }
        json_str = json.dumps(converted)
        return json_str
