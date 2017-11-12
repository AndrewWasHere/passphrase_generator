"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import tempfile

from passphrase.generate import generate


def test_generate_one(wordstore):
    gold = wordstore(['a', 'bb', 'ccc', 'dddd', 'eeeee'])
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(gold.to_json())
        f.seek(0)

        camel = generate(f.name, 1, 1, 1, 1, 'camel')
        lower = generate(f.name, 1, 1, 1, 1, 'lower')
        upper = generate(f.name, 1, 1, 1, 1, 'upper')

    assert camel == 'A'
    assert lower == 'a'
    assert upper == 'A'


def test_generate_two(wordstore):
    gold = wordstore(['a', 'bb', 'ccc', 'dddd', 'eeeee'])
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(gold.to_json())
        f.seek(0)

        camel = generate(f.name, 1, 1, 2, 2, 'camel')
        lower = generate(f.name, 1, 1, 2, 2, 'lower')
        upper = generate(f.name, 1, 1, 2, 2, 'upper')

    assert camel == 'Bb'
    assert lower == 'bb'
    assert upper == 'BB'


def test_concatenation(wordstore):
    gold = wordstore(['a', 'bb', 'ccc', 'dddd', 'eeeee'])
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(gold.to_json())
        f.seek(0)

        passphrase = generate(f.name, 2, 1, 3, 4, 'camel')

    assert passphrase in ['CccDddd', 'DdddCcc']


def test_chars(wordstore):
    gold = wordstore(['a', 'bb', 'ccc', 'dddd', 'eeeee'])
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(gold.to_json())
        f.seek(0)

        passphrase = generate(f.name, 0, 6, 0, 0, 'lower')

    assert len(passphrase) > 6
