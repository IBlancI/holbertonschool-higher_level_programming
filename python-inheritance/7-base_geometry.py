#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A class to define a shape"""
    def area(self):
        """
        Description:
            A function that raises an Exception with the message :
            "area() is not implemented"

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))