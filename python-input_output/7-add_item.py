#!/usr/bin/python3
"""A module for add all arguments to a Python list, and then save"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


"""
Description:
    A script that adds all arguments to a Python list, and then save them to a
    file.
Steps:
    1. Import the necessary modules.
    2. Load the file add_item.json.
    3. If the file doesn't exist, create an empty list.
    3. Add all arguments from the command line to the list.
    4. Save the updated list to the file add_item.json.
    5. Save also creates the file if it doesn't exist.
"""
try:
    file = load("add_item.json")
except FileNotFoundError:
    file = []

file = file + sys.argv[1:]
save(file, "add_item.json")