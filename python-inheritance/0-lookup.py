#!/usr/bin/python3
"""A module for lookup function."""


def lookup(obj):
    """
    Description:
        A function that returns the list
        of available attributes and methods of an object.

    Args: The object to be checked.

    Returns: A list
    """
    return dir(obj)