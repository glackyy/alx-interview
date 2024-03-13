#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Finding Winner"""
    wCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        rndWinner = isRoundWinner(nums[i], x)
        if rndWinner is not None:
            wCounter[rndWinner] += 1

    if wCounter['Maria'] > wCounter['Ben']:
        return 'Maria'
    elif wCounter['Ben'] > wCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    """Finding round winner"""
    list = [i for i in range(1, n + 1)]
    plys = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = plys[i % 2]
        selIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selIdxs.append(idx)
            else:
                if isPrime(num):
                    selIdxs.append(idx)
                    prime = num
        if prime == -1:
            if currentPlayer == plys[0]:
                return plys[1]
            else:
                return plys[0]
        else:
            for idx, val in enumerate(selIdxs):
                del list[val - idx]
    return None


def isPrime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
