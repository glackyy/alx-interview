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
    