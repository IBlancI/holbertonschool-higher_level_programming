#!/usr/bin/python3
"""
Define function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ return True if object is an instance of, or if the object is an
    instance of a class that inherited
    """
    return isinstance(obj, a_class)
