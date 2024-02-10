#!/usr/bin/python3
"""A module for matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Description:
        Function that divides all elements of a matrix.

    Args:
        matrix = list of lists (int/float)
        div = num (int/float)

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
            If the rows are not the same size.
            If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with the result of the division
    """

    too_long = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(too_long)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for i in row:
                if type(i) not in [int, float]:
                    raise TypeError(too_long)
                new_row += [round(i / div, 2)]
            new_matrix += [new_row]
        return new_matrix