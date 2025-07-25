#!/usr/bin/env python3
"""
Test file for example.py
"""

import unittest
from src.example import greet, process_data


class TestExample(unittest.TestCase):
    """Test cases for example module."""

    def test_greet(self):
        """Test the greet function."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_process_data(self):
        """Test the process_data function."""
        input_data = ["hello", "world", ""]
        expected = ["HELLO", "WORLD"]
        self.assertEqual(process_data(input_data), expected)

    def test_process_data_empty(self):
        """Test process_data with empty list."""
        self.assertEqual(process_data([]), [])


if __name__ == "__main__":
    unittest.main() 