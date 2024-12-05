#!/usr/bin/python3
"""Island perimeter"""
from typing import List


def island_perimeter(grid: List[List]):
    """calculate island perimetre"""
    perimeter = 0
    h = len(grid)
    w = len(grid[0])
    for y in range(0, h):
        # print(grid[y])
        for x in range(0, w):
            if grid[y][x] == 1:
                if x - 1 < 0 or grid[y][x - 1] == 0:
                    perimeter += 1
                if x + 1 > w or grid[y][x + 1] == 0:
                    perimeter += 1
                if y - 1 < 0 or grid[y - 1][x] == 0:
                    perimeter += 1
                if y + 1 > h or grid[y + 1][x] == 0:
                    perimeter += 1
    return perimeter
