#!/usr/bin/python3
"""
This module defines the mylist class
"""


class MyList(list):
    """
    MyList adds the ability to print the list elements
    """

    def print_sorted(self):
        """
        Prints list elements in ascending order without altering the original
        list.
        """
        sorted_list = sorted(self)
        print(sorted_list)