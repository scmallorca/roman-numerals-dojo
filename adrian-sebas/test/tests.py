import unittest
from src.game import Kata


class Something(unittest.TestCase):
    kata = Kata()

    def test_function_returns_string(self):
        self.assertEqual(type(self.kata.int_to_roman(3)),type('vdfeefsfdz'))

    def test_function_works_with_small_numbers(self):
        self.assertEqual(self.kata.int_to_roman(2), 'ii')

    def test_function_works_with_three(self):
        self.assertEqual(self.kata.int_to_roman(3), 'iii')

    def test_function_works_with_four(self):
        self.assertEqual(self.kata.int_to_roman(4), 'iv')

    def test_function_works_with_five(self):
        self.assertEqual(self.kata.int_to_roman(5), 'v')

    def test_function_works_with_six(self):
        self.assertEqual(self.kata.int_to_roman(6), 'vi')

    def test_function_works_with_seven(self):
        self.assertEqual(self.kata.int_to_roman(7), 'vii')

    def test_function_works_with_eight(self):
        self.assertEqual(self.kata.int_to_roman(8), 'viii')

    def test_function_works_with_night(self):
        self.assertEqual(self.kata.int_to_roman(9), 'ix')

    def test_function_works_with_teen(self):
        self.assertEqual(self.kata.int_to_roman(10), 'x')

    def test_function_works_with_fiveteen(self):
        self.assertEqual(self.kata.int_to_roman(15), 'xv')

    def test_function_works_with_twenty(self):
        self.assertEqual(self.kata.int_to_roman(20), 'xx')

    def test_function_works_with_seventy(self):
        self.assertEqual(self.kata.int_to_roman(70), 'lxx')



if __name__ == '__main__':
    unittest.main()
