#!/usr/bin/python3
"""A module for to_json_string function."""
import json


def to_json_string(my_obj):
    """
    Description:
        A function that returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        The JSON representation of the object. (string)
    """
    return json.dumps(my_obj)