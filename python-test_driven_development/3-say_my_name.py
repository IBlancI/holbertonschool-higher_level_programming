#!/usr/bin/python3
"""A module say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    Description:
        A function that prints My name is <first name> <last name>

    Args:
        first_name = string
        last_name = string

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))