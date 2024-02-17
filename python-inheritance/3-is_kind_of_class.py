#!/usr/bin/python3
"""A module for is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Description:
        A function that checks if the object is exactly an instance of the
        given specified class or an instance of a class that inherited from
        the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked.

    Returns:
        True or False. (boolean)
    """
    return type(obj) is a_class or isinstance(obj, a_class)