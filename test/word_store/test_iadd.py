"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.word_store import WordStore


def test_add_empty():
    words = WordStore()
    words += WordStore()

    assert len(list(words.iter_words())) == 0


def test_add_empty_to_nonempty():
    gold = ['alpha', 'bravo', 'charlie']
    words = WordStore()
    for word in gold:
        words.add(word)

    words += WordStore()

    assert len(list(words.iter_words())) == len(gold)


def test_add_nonempty_to_empty():
    gold = ['alpha', 'bravo', 'charlie']
    gold_words = WordStore()
    for word in gold:
        gold_words.add(word)

    words = WordStore()
    words += gold_words

    assert len(list(words.iter_words())) == len(gold)



def test_add_nonempty_to_nonempty():
    gold = ['left', 'center', 'right']
    more_gold = ['surround']

    words = WordStore()
    for word in gold:
        words.add(word)

    more_words = WordStore()
    for word in more_gold:
        words.add(word)

    words += more_words

    assert len(list(words.iter_words())) == len(gold) + len(more_gold)
    for word in words.iter_words():
        assert word in gold or word in more_gold


def test_add_duplicate():
    gold = ['left', 'center', 'right']
    more_gold = ['surround', 'center']

    words = WordStore()
    for word in gold:
        words.add(word)

    more_words = WordStore()
    for word in more_gold:
        words.add(word)

    words += more_words

    assert len(list(words.iter_words())) == len(frozenset(gold + more_gold))
    for word in words.iter_words():
        assert word in gold or word in more_gold
