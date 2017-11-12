"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.word_store import WordStore


def test_add():
    words = WordStore()
    words.add('albatross')

    assert len(list(words.iter_words())) == 1
    assert 'albatross' in words.iter_words()

    words.add('ganet')

    assert len(list(words.iter_words())) == 2
    assert 'albatross' in words.iter_words()
    assert 'ganet' in words.iter_words()
