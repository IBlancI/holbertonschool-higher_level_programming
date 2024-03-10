#!/usr/bin/python3
"""A module for class_to_json function."""


def class_to_json(obj):
    """
    Description:
        A function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for JSON
        serialization of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        The dictionary description of the object.
    """
    return obj.__dict__