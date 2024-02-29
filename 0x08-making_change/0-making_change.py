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
    t_val = 0
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    for c in coins:
        if total % c <= total:
            t_val += total // c
            total = total % c
    return t_val if total == 0 else -1
