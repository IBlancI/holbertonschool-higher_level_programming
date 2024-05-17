#!/usr/bin/python3
"""A module for a square class."""


class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
