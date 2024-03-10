#!/usr/bin/python3
"""A module for save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Description:
        A function that writes an Object to a text file, using a JSON
        representation.

    Args:
        my_obj: The object to write to the file.
        filename: The file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)