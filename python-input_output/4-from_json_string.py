#!/usr/bin/python3
"""function that returns an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """define json obj"""
    obj = json.loads(my_str)
    return obj
