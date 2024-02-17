#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to define a square"""

    def __init__(self, size):
        """
        Description:
            A function that initializes the instance of the class
            with given size.

        Args:
            size: size of the square
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """
        Description:
            Calculates the area (size * size) of the square.

        Returns:
            The area of the square. (int)
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Description:
            Returns a formal string representation of the square.
            EX :  [Square] 13/13

        Returns:
            The formal string representation of the square. (str)
        """
        return "[Square] {}/{}".format(self.__size, self.__size)