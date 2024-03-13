#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

nums = [0] * 10000
for i in range(100):
    nums[i] = i

print("Winner: {}".format(isWinner(10000, nums))) 
print("Winner: {}".format(isWinner(0, [0])))
print("Winner: {}".format(isWinner(-1, [10])))