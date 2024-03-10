#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Description:
        Unittest for max_integer([..])

    Test cases:
        test_max_at_end
        test_max_at_beginning
        test_max_in_middle
        test_one_negative_number
        test_only_negative_numbers
        test_list_of_one_element
        test_list_is_empty
    """
    def test_max_at_end(self):
        """
        Description:
            If max integer at the end of the list exists
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_beginning(self):
        """
        Description:
            If max integer at the beginning of the list exists
        """
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_middle(self):
        """
        Description:
            If max integer in the middle of the list exists
        """
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative_number(self):
        """
        Description:
            If only one negative number exists
        """
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_only_negative_numbers(self):
        """
        Description:
            If only negative numbers exist
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_one_element(self):
        """
        Description:
            If list has only one element
        """
        self.assertEqual(max_integer([1]), 1)

    def test_list_is_empty(self):
        """
        Description:
            If list is empty
        """
        self.assertEqual(max_integer([]), None)