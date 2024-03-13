#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Finding the winner"""
    if not nums or x < 1:
        return None
    max_n = max(nums)

    sort = [True for _ in range(max(max_n + 1, 2))]
    for i in range(2, int(pow(max_n, 0.5)) + 1):
        if not sort[i]:
            continue
        for j in range(i * i, max_n + 1, i):
            sort[j] = False
    sort[0] = sort[1] = False
    y = 0
    for i in range(len(sort)):
        if sort[i]:
            y += 1
        sort[i] = y
    pl1 = 0
    for x in nums:
        pl1 += sort[x] % 2 == 1
    if pl1 * 2 == len(nums):
        return None
    if pl1 * 2 > len(nums):
        return "Maria"
    return "Ben"
