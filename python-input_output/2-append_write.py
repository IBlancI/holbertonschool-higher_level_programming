#!/usr/bin/python3
"""A module for append_write function."""


def append_write(filename="", text=""):
    """
    Description:
        A function that appends a string at the end of a text file (UTF8).

    Args:
        filename: The file to append to.
        text: The text to append to the file.

    Returns:
        The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)