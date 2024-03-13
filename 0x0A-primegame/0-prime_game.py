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


def findMulti(num, targets):
    """Finding multiples of a num within list"""
    for i in targets:
        if i % num == 0:
            targets.remove(i)
    return targets


def findPrimes(n):
    """sending a set into prime nums and non-prime nums"""
    ct = 0
    


def isWinner(x, nums):
   