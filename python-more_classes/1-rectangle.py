#!/usr/bin/python3
"""Define a class representing a rectangle"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - width (int): represent the width of the rectangle.
    - height (int): represent the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with the given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        else:
            self.__height = value
