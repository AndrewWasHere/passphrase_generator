"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import os
import random

from passphrase.word_store import WordStore


def generate(
    src: str,
    n: int,
    chars: int,
    min_len: int,
    max_len: int,
    fmt: str,
    **_
) -> str:
    """Generate a passphrase.

    Args:
        src: word database.
        n:  minimum number of words in passphrase. If 0, only `chars` will be
            used to constrain passphrase.
        chars: minimum number of characters in passpharse. If 0, only `n` will
            be used to constrain passphrase.
        min_len: minimum number of characters in words of passphrase.
        max_len: maximum number of characters in words of passphrase.
        fmt: word format.
        **_:

    Returns:
        passphrase
    """
    phrase = ''
    if n == chars == 0:
        return phrase

    words = load_database(src)
    choices = list(words.iter_words(min_len, max_len))
    random.shuffle(choices)
    for count, word in enumerate(choices, 1):
        if fmt == 'camel':
            word = word.title()
        elif fmt == 'lower':
            word = word.lower()
        elif fmt == 'upper':
            word = word.upper()

        phrase += word

        if count >= n and len(phrase) >= chars:
            break

    return phrase


def load_database(src: str) -> WordStore:
    """Load WordStore from file path.

    Args:
        src: file path.

    Returns:
        word store.
    """
    src = os.path.abspath(os.path.expanduser(src))
    with open(src, 'r') as f:
        data = f.read()
        words = WordStore.from_json(data)

    return words
