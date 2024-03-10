#!/usr/bin/python3
"""A module for write_file function."""


def write_file(filename="", text=""):
    """
    Description:
        A function that writes a string to a text file (UTF8)

    Args:
        filename: The file to write to.
        text: The text to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return len(text)