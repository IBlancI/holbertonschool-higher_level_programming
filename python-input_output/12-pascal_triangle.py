#!/usr/bin/python3
"""Module for pascal_triangle function."""


def pascal_triangle(n):
    """
    Description:
        Returns a list of lists of integers
        representing the Pascal’s triangle of n.

    Args:
        n: The number of rows in the triangle.

    Returns:
        A list of lists of integers.
    """
    if n < 0 or n == 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            last_row = triangle[-1]
            new_row = [1]
            for j in range(len(last_row) - 1):
                new_row.append(last_row[j] + last_row[j + 1])
            new_row.append(1)
            triangle.append(new_row)
        return triangle