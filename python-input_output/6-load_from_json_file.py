#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """function to load"""
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.load(file)
    return obj
