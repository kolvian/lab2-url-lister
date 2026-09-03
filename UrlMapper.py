#!/usr/bin/env python3
"""UrlMapper.py -- emit every href target found in the input, one per line."""

import re
import sys

# Match a whole href attribute and keep just the URL inside the quotes.
HREF = re.compile(r'href="([^"]*)"')

for line in sys.stdin:
    for url in HREF.findall(line):
        print('%s\t%s' % (url, 1))
