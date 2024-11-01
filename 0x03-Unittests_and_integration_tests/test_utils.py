#!/usr/bin/env python3
"""
Unittests for utils
"""

from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock, PropertyMock
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
        Assert Equal
        """
        self.assertEqual(access_nested_map(a, b), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, a, b):
        """
        parameterized test
        Assert Raises
        """
        with self.assertRaises(KeyError):
            access_nested_map(a, b)


class TestGetJson(unittest.TestCase):
    """
    Class to Test GetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, url, res, mock_get):
        """
        Test GetJSON Method from utils
        """
        mock_respone = Mock()
        mock_respone.json.return_value = res
        mock_get.return_value = mock_respone

        response = get_json(url)
        self.assertEqual(response, res)


class TestMemoize(unittest.TestCase):
    """
    Class to Test memoize decorator
    """
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_instance = TestClass()
            first_call_result = test_instance.a_property()
            second_call_result = test_instance.a_property()

            mock_method.assert_called_once()
