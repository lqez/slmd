# -*- coding: utf-8 -*-
"""
mdls
~~~~

A humble Markdown list sorter.

:copyright: (c) 2017 by Park Hyunwoo.
:license: MIT, see LICENSE for more details.

"""

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from collections import defaultdict

TAB_SIZE = 4
LIST_MARKERS = ('* ', '- ', '+ ')


def sort_bucket(bucket, sort_by=None, depth=0):
    order = 1

    if sort_by:
        try:
            order = sort_by[depth]
        except ValueError:
            order = 0

    if order == 1:
        bucket.sort()
    elif order == -1:
        bucket.sort(reversed=True)

    for item, child in bucket:
        if child:
            sort_bucket(child, sort_by, depth + 1)


def bake_bucket(output, bucket, depth=0):
    for item, child in bucket:
        output.write(item)
        if child:
            bake_bucket(output, child, depth + 1)


def sort(stream, output, sort_by=None):
    buckets = defaultdict(list)
    tab_positions = []
    last_depth = depth = 0

    for line in stream:
        stripped = line.lstrip()

        if not stripped:
            depth = 0
        else:
            if stripped[:2] in LIST_MARKERS:
                leading = len(line) - len(stripped)
                if not tab_positions:
                    if leading < TAB_SIZE:
                        # new list found
                        tab_positions.append(leading)
                        depth = 1
                else:
                    if leading in tab_positions:
                        depth = tab_positions.index(leading) + 1
                    else:
                        # new indent position found
                        if leading - tab_positions[-1] <= TAB_SIZE:
                            tab_positions.append(leading)
                            depth = len(tab_positions)

                # record latest depth for non-list items
                last_depth = depth
            else:
                # in list, but non-list item
                if tab_positions:
                    depth = last_depth + 1

        if depth > 0:
            buckets[depth] = []
            buckets[depth - 1].append((line, buckets[depth]))
        else:
            if buckets:
                sort_bucket(buckets[0], sort_by)
                bake_bucket(output, buckets[0])
                buckets.clear()
                del tab_positions[:]
            output.write(line)

    # for remains
    if buckets:
        sort_bucket(buckets[0], sort_by)
        bake_bucket(output, buckets[0])


def sort_string(string, sort_by=None):
    stream = StringIO(string)
    output = StringIO()
    sort(stream, output, sort_by)
    return output.getvalue()
