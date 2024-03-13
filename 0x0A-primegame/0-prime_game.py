#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Finding the winner"""
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes
    sieve = [True] * (max(max_num + 1, 2))
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if sieve[i]:
            multiples = range(i * i, max_num + 1, i)
            for multiple in multiples:
                sieve[multiple] = False

    primes_count = [0]
    for i in range(1, len(sieve)):
        if sieve[i]:
            primes_count.append(primes_count[-1] + 1)
        else:
            primes_count.append(primes_count[-1])

    maria_wins = sum(primes_count[num] % 2 == 1 for num in nums)

    return (
        'Maria' if maria_wins * 2 > x else
        'Ben' if maria_wins * 2 < x else
        None
    )
