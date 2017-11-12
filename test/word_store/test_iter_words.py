"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import pytest


@pytest.fixture
def gold():
    return ['a', 'bb', 'ccc', 'dddd', 'eeeee']


@pytest.fixture
def goldwords(gold, wordstore):
    words = wordstore(gold)
    return words


def test_iter_all(gold, goldwords):
    for word in goldwords.iter_words():
        assert word in gold


def test_iter_upper_bound(gold, goldwords):
    test_gold = gold[:4]

    for word in goldwords.iter_words(max_len=4):
        assert word in test_gold


def test_iter_lower_bound(gold, goldwords):
    test_gold = gold[1:]

    for word in goldwords.iter_words(min_len=2):
        assert word in test_gold


def test_iter_range_bound(gold, goldwords):
    test_gold = gold[1:4]

    for word in goldwords.iter_words(min_len=2, max_len=4):
        assert word in test_gold
