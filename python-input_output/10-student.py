#!/usr/bin/python3
"""Defines a Student class and methods for data representation"""


class Student:
    """A class representing a student with information"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_attr = {}
            for i in attrs:
                if i in self.__dict__:
                    new_attr[i] = self.__dict__[i]
            return new_attr
