#!/usr/bin/env python

import unittest
from roman_numerals import RomanNumerals

class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.roman_numerals = RomanNumerals()

    def test_returns_a_string(self):
        self.assertIsInstance(self.roman_numerals.get_roman_numeral(1), str)

    def test_one_returns_I(self):
        self.assertEqual(self.roman_numerals.get_roman_numeral(1), 'I')

    def test_two_returns_II(self):
        self.assertEqual(self.roman_numerals.get_roman_numeral(2), 'II')

if __name__ == '__main__':
    unittest.main()