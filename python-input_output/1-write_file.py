#!/usr/bin/python3
"""function that write a string"""


def write_file(filename="", text=""):
    """function that return number of character"""
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
