# -*- coding: utf-8 -*-
import sys
import argparse
from slmd import sort_string


def get_parser():
    parser = argparse.ArgumentParser(description='Sort lists in Markdown')

    parser.add_argument('infile', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', type=argparse.FileType('w'), nargs='?',
                        default=sys.stdout)
    parser.add_argument('-s', type=int, dest='sort_by', nargs='*',
                        help='Set order by depth (1:ASC / -1:DESC / 0:Do not sort)')

    return parser


def main():
    args = get_parser().parse_args()

    source = args.infile.read()
    result = sort_string(source, args.sort_by)

    args.outfile.write(result)

    sys.exit(0 if (source == result) else 1)


if __name__ == '__main__':
    main()
