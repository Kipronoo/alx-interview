#!/usr/bin/python3
"""
A python program on Prime Game
"""


def isWinner(x, nums):
    """
    A python program on prime game
    """

    def sieve(n):
        """
        determine the prime number
        """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return is_prime

    def count_primes(n, is_prime):
        """
        function to get the number of count
        """
        count = 0
        for num in range(1, n + 1):
            if is_prime[num]:
                count += 1
                for multiple in range(num, n + 1, num):
                    is_prime[multiple] = False
        return count

    max_num = max(nums)
    is_prime = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes_count = count_primes(num, is_prime[:num + 1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return "None"
