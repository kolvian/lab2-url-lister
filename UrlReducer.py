#!/usr/bin/env python3
"""UrlReducer.py -- sum the counts per URL and report only those seen more than five times."""

import sys

THRESHOLD = 5

current_url = None
current_count = 0
url = None


def emit(key, count):
    if key is not None and count > THRESHOLD:
        print('%s\t%s' % (key, count))


# Hadoop sorts the map output by key, so all counts for a URL arrive together.
for line in sys.stdin:
    line = line.strip()
    try:
        url, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_url == url:
        current_count += count
    else:
        emit(current_url, current_count)
        current_url = url
        current_count = count

emit(current_url, current_count)
