#!/usr/bin/python3
"""Reading stdin line by line and computing metrics"""
import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
tl_size = 0
c = 0

try:
    for l in sys.stdin:
        l_list = l.split(" ")
        if len(l_list) > 4:
            code = l_list[-2]
            size = int(l_list[-1])
            if code in cache.keys():
                cache[code] += 1
            tl_size += size
            c += 1
        if c == 10:
            c = 0
            print('File size: {}'.format(tl_size))
            