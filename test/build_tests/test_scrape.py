"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
from unittest import mock

import requests

from passphrase.build import scrape


def test_bad_url():
    mock_response = mock.Mock(
        raise_for_status=mock.Mock(side_effect=requests.exceptions.HTTPError)
    )

    with mock.patch(
        'passphrase.build.requests.get',
        return_value=mock_response
    ), mock.patch(
        'passphrase.build.scrape_html',
    ) as mock_scrape_html:
        words = scrape('bogus URL')

        assert not mock_scrape_html.called
        assert len(list(words.iter_words())) == 0


def test_valid_url():
    mock_response = mock.Mock(
        raise_for_status=mock.Mock()
    )

    with mock.patch(
        'passphrase.build.requests.get',
        return_value=mock_response
    ), mock.patch(
        'passphrase.build.scrape_html',
        return_value='mock return'
    ) as mock_scrape_html:
        words = scrape('bogus URL')

        assert mock_scrape_html.called
        assert words == 'mock return'
