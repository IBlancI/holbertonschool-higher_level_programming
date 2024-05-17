#!/usr/bin/python3
"""A module for a square class."""


class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Description:
            Calculates the area of the square and returns it.

        Returns:
            The area of the square
        """
        return self.__size * self.__size
