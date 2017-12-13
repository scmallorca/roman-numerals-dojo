#!/usr/bin/env python

import unittest
from roman_numerals import RomanNumerals


class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.roman_numerals = RomanNumerals()

    def test_returns_a_string(self):
        self.assertIsInstance(self.roman_numerals.convert_from_integer(1), str)

    def test_one_returns_I(self):
        self.assertEqual(self.roman_numerals.convert_from_integer(1), 'I')

    def test_two_returns_II(self):
        self.assertEqual(self.roman_numerals.convert_from_integer(2), 'II')

    def test_five_returns_V(self):
        self.assertEqual(self.roman_numerals.convert_from_integer(5), 'V')

    def test_ten_returns_X(self):
        self.assertEqual(self.roman_numerals.convert_from_integer(10), 'X')

    def test_roman_letters_can_repeat_three_times(self):
        for number in [1, 10, 100, 1000]:
            one_roman = self.roman_numerals.convert_from_integer(number)
            three_roman = self.roman_numerals.convert_from_integer(number * 3)

            self.assertEqual(three_roman, one_roman * 3)


if __name__ == '__main__':
    unittest.main()