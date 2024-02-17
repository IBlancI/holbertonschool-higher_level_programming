#!/usr/bin/python3
"""Module for Rectangle class inheriting from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to define a rectangle"""

    def __init__(self, width, height):
        """
        Description:
            A function that initializes the instance of the class
            with given width and height.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height