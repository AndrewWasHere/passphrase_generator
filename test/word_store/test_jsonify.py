"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.word_store import WordStore


def test_empty():
    words = WordStore()
    json_str = words.to_json()
    reconstructed_words = WordStore.from_json(json_str)

    assert reconstructed_words.store == words.store


def test_populated(wordstore):
    words = wordstore(['something', 'in', 'the', 'way', 'she', 'moves'])
    json_str = words.to_json()
    reconstructed_words = WordStore.from_json(json_str)

    assert reconstructed_words.store == words.store
