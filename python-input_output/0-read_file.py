#!/usr/bin/python3
"""function to read a file"""


def read_file(filename=""):
    """Read_file"""
    with open('my_file_0.txt', encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
