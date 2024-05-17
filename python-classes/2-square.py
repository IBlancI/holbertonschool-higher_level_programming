#!/usr/bin/python3
"""A module for a square class."""


class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """
        Description:
            Creates a instance of a square and
            initializes the size of it with the given parameter.
            If no value is given, it defaults to 0.

        Args:
            size (int): The size of the square given as an integer.
        """
        self.__size = size

    @property
    def size(self):
        """
        Description:
            Gets the value of the size attribute and returns it.

        Returns:
            The value of the size attribute (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Description:
            Checks the given parameter value and
            sets it to the size attribute. (setter)

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Description:
            Calculates the area of the square and returns it.

        Returns:
            The area of the square (int)
        """
        return self.__size * self.__size