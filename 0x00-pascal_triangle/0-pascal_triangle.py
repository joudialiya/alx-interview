#!/usr/bin/python3
"""
PAscal Triangle
"""

def pascal_triangle(n):
    """main function"""
    if n <= 0 or n is None:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # the logic outside of the bondaries
    current_list = []
    prev_list = pascal_triangle(n - 1)
    for p in range(0, n):
        if p == 0:
            current_list.append(1)
        elif p == n - 1:
            current_list.append(1)
        else:
            current_list.append(prev_list[p] + prev_list[p - 1])