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

    def to_json(self, attrs=None):
        """
        Description:
            A function that retrieves a dictionary
            representation of a Student instance"

        Returns:
            A dictionary.
        """
        if attrs is None:
            return self.__dict__
        else:
            newD = {}
            for key in attrs:
                if key in self.__dict__:
                    newD[key] = self.__dict__[key]
            return newD

    def reload_from_json(self, json):
        """
        Description:
            A function that replaces all attributes of the Student instance.

        Args:
            json: A dictionary with attributes and values.
        """
        for key, value in json.items():
            setattr(self, key, value)