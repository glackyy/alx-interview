#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Finding Winner"""
    WCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        