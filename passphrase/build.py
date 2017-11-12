"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import logging
import os

import requests
from bs4 import BeautifulSoup

from passphrase.word_store import WordStore


_logger = logging.getLogger(__name__)


def build(src: str, **_) -> str:
    """Build word store from URL(s).

    Args:
        src: source(s) to scrape. Can be URL, or file containing one URL per
            line.

    Returns:
        Words store as json.
    """
    # Make sure src is iterable.
    src_as_file = os.path.abspath(os.path.expanduser(src))
    sources = (
        (s for s in iter_sources(src))
        if os.path.isfile(src_as_file) else
        (s for s in [src])
    )

    # Scrape source(s).
    words = WordStore()
    for source in sources:
        words += scrape(source)

    # Output results.
    return words.to_json()


def iter_sources(path: str):
    """Generator of source URLs.

    Args:
        path: path to source file

    Returns:

    """
    with open(path, 'r') as f:
        for src in f:
            yield src.strip()


def scrape(url: str) -> WordStore:
    """Scrape HTML resource of its text.

    Args:
        url: HTML resource to scrape.

    Returns:
        words in resource.
    """
    r = requests.get(url)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        _logger.warning('Could not scrape %s', url)
        words = WordStore()
    else:
        words = scrape_html(r.text)

    return words


def scrape_html(html: str) -> WordStore:
    """Scrape HTML of its text.

    Args:
        html:

    Returns:
        words in HTML.
    """
    words = WordStore()
    soup = BeautifulSoup(html, 'html.parser')
    try:
        for s in soup.body.strings:
            for word in s.split():
                words.add(word)
    except AttributeError:
        _logger.info('HTML has no body.')

    return words
