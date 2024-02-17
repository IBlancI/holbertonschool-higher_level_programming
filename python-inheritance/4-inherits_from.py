#!/usr/bin/python3
"""A module for inherits_from function."""


def inherits_from(obj, a_class):
    """
    Description:
        A function that checks if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked.

    Returns:
        True or False. (boolean)
    """
    return type(obj) is not a_class and isinstance(obj, a_class)