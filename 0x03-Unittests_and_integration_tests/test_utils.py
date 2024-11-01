#!/usr/bin/env python3
"""
Unittests for utils
"""

from utils import access_nested_map
import unittest
from parameterized import parameterized  # Import directly

class TestAccessNestedMap(unittest.TestCase):
    """
    Class to Test AccessNestedMap
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, a, b, expected):
        """
        parameterized test
        """
        self.assertEqual(access_nested_map(a, b), expected)
