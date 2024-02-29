#!/usr/bin/python3
"""Determining the fewest number of coins needed to meet
a amount total on a pile of coins if different values"""
import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    INF = sys.maxsize
    table = [INF] * (total + 1)
    table[0] = 0

    for coin in coins:
        for am in range(coin, total + 1):
            table[am] = min(table[am], table[am - coin] + 1)

    return table[total] if table[total] != INF else -1
