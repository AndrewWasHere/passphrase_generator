"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import tempfile
from unittest import mock

from passphrase.build import build
from passphrase.word_store import WordStore


def test_build_with_url(wordstore):
    gold_wordstore = wordstore(['llama', 'rabbit', 'capybara'])

    with mock.patch('passphrase.build.scrape', return_value=gold_wordstore):
        words_json = build('http://nowhere.in.particular')

    words = WordStore.from_json(words_json)

    assert words.store == gold_wordstore.store


def test_build_with_file(wordstore):
    rodents = wordstore(['squirrel', 'rabbit', 'capybara'])
    mustelinae = wordstore(['wolverine', 'otter', 'mink'])
    birds = wordstore(['osprey', 'pigeon', 'wren'])
    stores = [rodents, mustelinae, birds]

    gold = rodents + mustelinae + birds

    lines = ['first', 'second', 'third']

    with mock.patch(
        'passphrase.build.scrape',
        side_effect=stores
    ) as mock_scrape, tempfile.NamedTemporaryFile('w') as f:
        # Create sources.
        for line in lines:
            f.write(line)
            f.write('\n')

        f.seek(0)

        json_str = build(f.name)

        words = WordStore.from_json(json_str)

        assert words.store == gold.store
        assert mock_scrape.call_count == len(stores)
