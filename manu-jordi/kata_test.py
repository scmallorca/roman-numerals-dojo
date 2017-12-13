#!/usr/bin/env python

import unittest
from kata import Kata

class KataTests(unittest.TestCase):
    def setUp(self):
        self.kata = Kata()

    def test_returns_a_string(self):
        self.assertIsInstance(self.kata.get_roman_numeral(1), str)

    def test_one_returns_I(self):
        self.assertEqual(self.kata.get_roman_numeral(1), 'I')

if __name__ == '__main__':
    unittest.main()