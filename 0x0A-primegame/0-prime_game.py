#!/usr/bin/python3
"""Prime Game"""


def isPrime(i):
    """Checking if a number is prime"""
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True 


def isWinner(x, nums):
   