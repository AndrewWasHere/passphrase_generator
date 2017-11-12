"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import pytest

from passphrase.word_store import WordStore


@pytest.fixture
def wordstore():
    def build_store(words):
        store = WordStore()
        for word in words:
            store.add(word)

        return store

    return build_store
