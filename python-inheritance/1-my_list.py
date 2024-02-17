#!/usr/bin/python3
"""A module for MyList class."""


class MyList(list):
    """
    Description:
        A class MyList that inherits from list.

    Args:
        List to be inherited.
    """
    def print_sorted(self):
        """
        Description:
            A function that prints the list, but sorted.

        Returns:
            A sorted list of the original list (list of integers).
        """
        sorted_list = sorted(self)
        print(sorted_list)