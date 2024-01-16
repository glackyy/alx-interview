#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculating the fewest num of operations
    needed to result in exactly n H
    chars in the file"""
    past_chars = 1
    c = 0
    pasteboard = 0

    while past_chars < n:
        if pasteboard == 0:
            pasteboard = past_chars
            c += 1
        if past_chars == 1:
            past_chars += pasteboard
            c += 1
            continue
        remain = n - past_chars
        if remain < pasteboard:
            return 0
        if remain % past_chars != 0:
            past_chars += pasteboard
            c += 1
        else:
            pasteboard = past_chars
            past_chars += pasteboard
            c += 2

    if past_chars == n:
        return c
    else:
        return 0
