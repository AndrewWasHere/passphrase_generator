"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from passphrase.build import scrape_html


def test_scrape_empty():
    """Scrape an empty string"""
    words = scrape_html('')

    assert len(list(words.iter_words())) == 0


def test_scrape_valid_html():
    """Scrape non-empty HTML"""
    words = scrape_html(
        """
        <head>
            <title>exempt</title>
        </head>
        <body>
            <p>valid words</p>
            <a href="http://someurl">in body</a>
        </body>
        """
    )

    scraped_words = list(words.iter_words())

    assert 'exempt' not in scraped_words
    for w in 'valid words in body'.split():
        assert w in scraped_words
