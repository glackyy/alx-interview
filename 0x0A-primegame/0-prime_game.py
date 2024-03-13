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
            else:
                return pl[0]
        else:
            for idx, val in enumerate(selIndexs):
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
