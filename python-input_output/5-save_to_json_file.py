#!/usr/bin/python3
"""function that writes an Obj to a text f using a JSON rep"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        json.dump(my_obj, file)
