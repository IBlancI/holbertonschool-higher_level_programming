#!/usr/bin/python3
"""function that define a student by public instance"""


class Student:
    """A class representating a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__
