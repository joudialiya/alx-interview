#!/usr/bin/python3
"""Nqueens problem"""
from typing import List
import sys


def valid_point(point: List, state: List):
    """checks is a point is threten by any placed queen"""
    if point[0] in map(lambda e: e[0], state):
        return False
    if point[1] in map(lambda e: e[1], state):
        return False
    if list(filter(lambda e: point[0] - e[0] == point[1] - e[1], state)):
        return False
    if list(filter(lambda e: point[0] - e[0] == - (point[1] - e[1]), state)):
        return False
    return True


def nquenes_helper(n: int, state: List):
    """Nqueens solution"""
    if len(state) == n:
        print(state)
        return
    column = len(state)
    for i in range(0, n):
        point = [column, i]
        if valid_point(point, state):
            nquenes_helper(n, [*state, point])


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdecimal():
        print("N must be a number")
        exit(1)
    "".isdecimal()
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nquenes_helper(int(argv[1]), [])
