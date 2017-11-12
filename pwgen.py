"""
Copyright 2017, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import argparse

import os

from passphrase.build import build
from passphrase.generate import generate


def add_build_args(cmd_parser: argparse.ArgumentParser):
    """Add command line arguments for build command.
    
    Args:
        cmd_parser: parser for build command.

    Returns:

    """
    cmd_parser.add_argument(
        'src',
        help='source to scrape for words'
    )
    cmd_parser.add_argument(
        '-o', '--out',
        help='path to database file to create.'
    )
    cmd_parser.set_defaults(func=build)


def add_generate_args(cmd_parser: argparse.ArgumentParser):
    """Add command line arguments for generate command.

    Args:
        cmd_parser: parser for generate command.

    Returns:

    """
    cmd_parser.add_argument(
        'src',
        help='word database to draw from'
    )
    cmd_parser.add_argument(
        '--max',
        dest='max_len',
        type=int,
        default=0,
        help='maximum number of characters in a word'
    )
    cmd_parser.add_argument(
        '--min',
        dest='min_len',
        type=int,
        default=0,
        help='minimum number of characters in a word'
    )
    cmd_parser.add_argument(
        '-n',
        type=int,
        default=0,
        help='number of words to concatenate together'
    )
    cmd_parser.add_argument(
        '--chars',
        type=int,
        default=0,
        help='minimum number of characters in passphrase'
    )
    cmd_parser.add_argument(
        '--camelcase',
        dest='fmt',
        action='store_const',
        const='camel',
        help='camelcase words'
    )
    cmd_parser.add_argument(
        '--lower',
        dest='fmt',
        action='store_const',
        const='lower',
        help='lowercase words'
    )
    cmd_parser.add_argument(
        '--upper',
        dest='fmt',
        action='store_const',
        const='upper',
        help='uppercase words'
    )
    cmd_parser.set_defaults(func=generate, fmt='camel')


def parse_command_line() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        args: command line arguments.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    build_parser = subparsers.add_parser('build')
    add_build_args(build_parser)

    generate_parser = subparsers.add_parser('generate')
    add_generate_args(generate_parser)

    args = parser.parse_args()
    return args


def main():
    args = parse_command_line()
    if args.command == 'build':
        result = build(**vars(args))
        # Handle build result.
        if args.out:
            dest = os.path.abspath(os.path.expanduser(args.out))
            with open(dest, 'w') as f:
                f.write(result)
        else:
            print(result)
    else:
        result = generate(**vars(args))
        # Handle generate result.
        print(result)


if __name__ == '__main__':
    main()
