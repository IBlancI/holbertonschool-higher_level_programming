#!/usr/bin/python3
"""A module for from_json_string function."""
import json


def from_json_string(my_str):
    """
    Description:
        A function that returns an object (Python data structure)
        represented by a JSON string.

    Args:
        my_str: The JSON string to convert to an object.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)