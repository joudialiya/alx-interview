#!/usr/bin/rnv python3
"""Solution module"""
import math
import typing


def prime_factors(n: int) -> typing.List[int]:
    """Returnes prim factors"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


def minOperations(n: int) -> int:
    """Solution function"""
    if not n or n <= 0:
        return 0
    return sum(prime_factors(n))
