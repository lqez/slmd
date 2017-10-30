# -*- coding: utf-8 -*-
import sys
import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description='Markdown list sorter'
    )

    parser.add_argument('infile', nargs=1, type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs=1, type=argparse.FileType('w'),
                        default=sys.stdout)

    return parser


def main():
    args = get_parser().parse_args()
    print(args)
    pass


if __name__ == '__main__':
    main()
