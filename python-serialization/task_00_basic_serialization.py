#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    (str): The filename of the output JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Returns:
    dict: A Python dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
