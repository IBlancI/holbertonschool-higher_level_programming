#!/usr/bin/python3
"""function that reads a file"""


def read_file(filename=""):
    """Read_file"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
