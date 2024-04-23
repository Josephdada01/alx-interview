#!/usr/bin/env python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):that returns a
    list of lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []
    triangle = []

    for i in range(n):
        row = [1]  # the first element in a row
        if i > 0:
            # generating the remaining rows based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle
