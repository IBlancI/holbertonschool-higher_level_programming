#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides the elements of a matrix and returns a new matrix."""
    if not isinstance(matrix, list):
        raise TypeError("Input must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Input must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("Input must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("The divisor must be a number")
    elif div == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    new_matrix = []
    size = len(matrix[0])

    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)

        new_matrix.append(new_row)

    return new_matrix
