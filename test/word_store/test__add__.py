"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.word_store import WordStore


def test_empty_plus_empty():
    combined = WordStore() + WordStore()

    assert combined.store == WordStore().store


def test_empty_plus_nonempty(wordstore):
    words = wordstore(['a', 'b', 'c'])

    combined = WordStore() + words

    assert combined.store == words.store


def test_nonempty_plus_empty(wordstore):
    words = wordstore(['alpha', 'bravo', 'charlie'])

    combined = words + WordStore()

    assert combined.store == words.store


def test_nonempty_plus_nonempty(wordstore):
    rocks = ['granite', 'basalt']
    trees = ['larch', 'pine', 'fir']
    combined = wordstore(rocks) + wordstore(trees)

    assert combined.store == wordstore(rocks + trees).store
