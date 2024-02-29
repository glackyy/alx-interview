#!/usr/bin/python3
"""Determining the fewest number of coins needed to meet
a amount total on a pile of coins if different values"""
import sys


def makeChange(coins, total):
    """Returning fewest number of coins needed
    to meet total"""
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < tab[i]:
                    tab[i] = subres + 1
    if table[total] == sys.maxsize:
        return -1
    return table[total]
