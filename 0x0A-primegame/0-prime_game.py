#!/usr/bin/python3
"""Prime game"""


def isPrime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primesTo(n):
    return [n for n in range(1, n + 1) if isPrime(n)]


def isWinner(x, nums):
    """Solution function"""
    MWinsCount = 0
    BWinsCount = 0
    for round in range(0, x):
        primes = primesTo(nums[round])
        if len(primes) % 2 == 0:
            BWinsCount += 1
        else:
            MWinsCount += 1
    if MWinsCount > BWinsCount:
        return "Maria"
    if BWinsCount > MWinsCount:
        return "Ben"
    return None
