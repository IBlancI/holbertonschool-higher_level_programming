#!/usr/bin/python3
"""A module for is_same_class function."""


def is_same_class(obj, a_class):
    """
    Description:
        A function that checks if the object is exactly an instance of the
        given specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False. (boolean)
    """
    return type(obj) is a_class