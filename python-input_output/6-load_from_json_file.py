#!/usr/bin/python3
"""A module for load_from_json_file function."""
import json


def load_from_json_file(filename):
    """
    Description:
        A function that creates an Object from a "JSON file".

    Args:
        filename: The file to read from.

    Returns:
        The object represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)