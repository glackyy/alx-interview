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