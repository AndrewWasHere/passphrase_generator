"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import tempfile

from passphrase.generate import load_database


def test_load(wordstore):
    gold = wordstore(['caramel', 'nougat', 'sugar'])
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(gold.to_json())
        f.seek(0)

        words = load_database(f.name)

    assert words.store == gold.store
