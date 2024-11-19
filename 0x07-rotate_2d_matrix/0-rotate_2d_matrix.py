#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a matrix using geometry"""
    rotated = []
    n = len(matrix)
    for y in range(0, n):
        line = []
        for x in range(0, n):
            """
            x' = xcosθ - ysinθ.
            y' = xsinθ + ycosθ.
            θ = pi / 2
            """
            rotated_x = x - (n - 1) / 2
            rotated_y = y - (n - 1) / 2
            original_x = rotated_y
            original_y = - rotated_x
            original_x += (n - 1) / 2
            original_y += (n - 1) / 2
            line.append(matrix[int(original_y)][int(original_x)])
        rotated.append(line)
    for y in range(0, n):
        for x in range(0, n):
            matrix[y][x] = rotated[y][x]
