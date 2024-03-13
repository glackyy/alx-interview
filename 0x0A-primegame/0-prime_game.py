#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Finding Winner"""
    WCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        rdWinner = isRoundWinner(nums[i], x)
        if rdWinner is not None:
            WCounter[rdWinner] += 1

    if WCounter['Maria'] > WCounter['Ben']:
        return 'Maria'
    elif WCounter['Ben'] > WCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    """Finding round Winner"""
    list = [i for i in range(1, n + 1)]
    pl = ['Maria', 'Ben']

    for i in range(n):
        currPlayer = pl[i % 2]
        selIndexs = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selIndexs.append(idx)
            else:
                if isPrime(num):
                    selIndexs.append(idx)
                    prime = num
    if prime == -1:
        if currPlayer == pl[0]:
            return pl[1]