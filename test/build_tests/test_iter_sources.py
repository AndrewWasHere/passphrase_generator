"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import tempfile

from passphrase.build import iter_sources


def test_iter_sources():
    lines = ['first', 'second', 'third']

    with tempfile.NamedTemporaryFile('w') as f:
        # Create sources.
        for line in lines:
            f.write(line)
            f.write('\n')

        f.seek(0)

        # Test iteration.
        for gold, line in zip(lines, list(iter_sources(f.name))):
            assert line == gold
