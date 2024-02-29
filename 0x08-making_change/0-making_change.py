#!/usr/bin/python3
"""Determining the fewest number of coins needed to meet
a amount total on a pile of coins if different values"""
import sys


def makeChange(coins, total):
    """Returning fewest number of coins needed
    to meet total"""
    if total <= 0:
        return 0
    tab = [sys.maxsize for i in range(total + 1)]
    tab[0] = 0
    ma = len(coins)
    for i in range(1, total + 1):
        for j in range(ma):
            if coins[j] <= i:
                sures = tab[i - coins[j]]
                if sures != sys.maxsize and sures + 1 < tab[i]:
                    tab[i] = sures + 1
                