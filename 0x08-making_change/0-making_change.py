#!/usr/bin/python3
"""Determining the fewest number of coins needed to meet
a amount total on a pile of coins if different values"""
import sys


def makeChange(coins, total):
    """Returning fewest number of coins needed
    to meet total"""
    if total <= 0:
        return 0
    INF = sys.maxsize
    table = [INF] * (total + 1)
    table[0] = 0

    for coin in coins:
        for am in range(coin, total + 1):
            table[am] = min(table[am], table[am - coin] + 1)
    return table[total] if table[total] != INF else -1
