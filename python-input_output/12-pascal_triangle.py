#!/usr/bin/python3
""" Function to generate a Pascal's Triangle """


def pascal_triangle(n):
    """Generates Pascal's Triangle up to 'n' rows"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    previous_triangle = pascal_triangle(n - 1)
    last_row = previous_triangle[-1]
    current_row = [1]

    for i in range(1, len(last_row)):
        current_row.append(last_row[i - 1] + last_row[i])

    current_row.append(1)
    previous_triangle.append(current_row)

    return previous_triangle
