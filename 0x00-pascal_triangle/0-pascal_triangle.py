#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):that returns a
    list of lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    triangle = []

    if n <= 0:
        triangle

    for i in range(n):
        temporary_list = []  # the first element in a row
        # generating the remaining rows based on the previous row
        for j in range(i+1):
            if j == 0 or j == i:
                temporary_list.append(1)
            else:
                temporary_list.append(triangle[i - 1][j - 1] +
                                      triangle[i - 1][j])
        triangle.append(temporary_list)
    return triangle
