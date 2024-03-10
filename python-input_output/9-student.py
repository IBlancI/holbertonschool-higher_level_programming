#!/usr/bin/python3
""" Module for Student class"""


class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """
        Description:
            Initializes the Student instance.

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Description:
            A function that retrieves a dictionary
            representation of a Student instance"

        Returns:
            A dictionary.
        """
        return self.__dict__