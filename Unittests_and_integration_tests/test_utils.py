#!/usr/bin/env python3
""" File test for utils
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Class test for access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test for access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class test for get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests):
        """ Test that utils.get_json returns the expected result
        """
        mock_requests.return_value.json.return_value = test_payload
        url = get_json(test_url)
        mock_requests.assert_called_once_with(test_url)
        self.assertEqual(url, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class test for memoize
    """

    def test_memoize(self):
        """ test_memoize methode
        """

        class TestClass:
            """ Class TestClass
            """

            def a_method(self):
                """ Return 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Call a_method
                """
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            mock = TestClass()
            self.assertEqual(mock.a_property, 42)
            self.assertEqual(mock.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
