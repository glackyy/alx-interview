#!/usr/bin/python3
"""Prime Game"""


def isPrime(i):
    """Checking if a number is prime"""
    if i == 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True


def findMulti(num, targets):
    """Finding multiples of a num within list"""
    multiples = [i for i in targets if i % num == 0]
    return [i for i in targets if i not in multiples]


def findPrimes(n):
    """Sending a set into prime nums and non-prime nums"""
    ct = 0
    target = list(n)
    for i in range(1, len(target) + 1):
        if isPrime(i):
            ct += 1
            target.remove(i)
            target = findMulti(i, target)
        else:
            pass
    return ct


def isWinner(x, nums):
    """Finding the winner"""
    plys = {'Maria': 0, 'Ben': 0}
    clst = set()
    for e in range(x):
        nums.sort()
        num = nums[e]
        for i in range(1, num + 1):
            clst.add(i)
            if i == num + 1:
                break
        tempo = findPrimes(clst)

        if tempo % 2 == 0:
            plys['Ben'] += 1
        elif tempo % 2 != 0:
            plys['Maria'] += 1

    if plys['Maria'] > plys['Ben']:
        return 'Maria'
    elif plys['Maria'] < plys['Ben']:
        return 'Ben'
    else:
        return None
