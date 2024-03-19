#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        """Test if the id is correctly assigned."""
        base1 = Base()
        base2 = Base(12)
        base3 = Base()

        self.assertIsNone(base1.id, "Id should be auto-incremented.")
        self.assertEqual(base2.id, 12, "Id should be 12.")
        self.assertIsNotNone(base3.id, "Id should be auto-incremented.")