#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """Finding the winner"""
    def is_prime(n):
        """checking if num is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def playRound(n):
        """Simulating a single round of the game"""
        maria_turn = True

        while n > 1:
            found_prime = False
            for i in range(2, n + 1):
                if is_prime(i) and n % i == 0:
                    n -= i
                    found_prime = True
                    break

            if not found_prime:
                break

            maria_turn = not maria_turn

        return 'Maria' if maria_turn else 'Ben'

    winners = {'Maria': 0, 'Ben': 0}

    for round_num in nums:
        winner = playRound(round_num)
        winners[winner] += 1

    if winners['Maria'] < winners['Ben']:
        return 'Ben'
    elif winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return None
