#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Returning True if data is a valid UTF-8
    encoding, else returning False"""
    by_count = 0
    for i in data:
        if by_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                by_count = 1
            elif i >> 4 == 0b1110:
                by_count = 2
            elif i >> 3 == 0b11110:
                by_count = 3