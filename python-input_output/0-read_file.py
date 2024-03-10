#!/usr/bin/python3
"""A module for read_file function."""


def read_file(filename=""):
    """
    Description:
        A function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The file to read.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")