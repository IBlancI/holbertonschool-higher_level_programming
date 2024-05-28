#!/usr/bin/python3
"""function that return the JSON representation"""

import json


def to_json_string(my_obj):
    """define json obj"""
    json_str = json.dumps(my_obj)
    return json_str
