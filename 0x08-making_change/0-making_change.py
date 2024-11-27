#!/usr/bin/python3
"""Change problem"""
from typing import List


def minCoinsRecur(i, sum, coins):
    """Hepler function"""
    # base case
    if sum == 0:
        return 0
    if sum < 0 or i == len(coins):
        return float('inf')

    take = float('inf')

    # take a coin only if its value
    # is greater than 0.
    if coins[i] > 0:
        take = minCoinsRecur(i, sum - coins[i], coins)
        if take != float('inf'):
            take += 1

    noTake = minCoinsRecur(i + 1, sum, coins)

    return min(take, noTake)


def minCoins(coins, sum):
    """Solution function"""
    ans = minCoinsRecur(0, sum, coins)
    return ans if ans != float('inf') else -1


def makeChange(coins: List, total: int):
    """Logic funnction"""
    return minCoins(coins, total)
