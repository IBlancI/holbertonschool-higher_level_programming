#!/usr/bin/python3
"""A module for a square class."""


class Square:
    """A class to define a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
            type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()