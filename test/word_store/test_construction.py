"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.word_store import WordStore


def test_nominal():
    words = WordStore()

    assert len(list(words.iter_words())) == 0
