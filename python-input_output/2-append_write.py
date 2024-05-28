#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appending"""
    with open(filename, 'a', encoding='UTF-8') as file:
        file.write(text)
    chars = len(text)
    return chars
