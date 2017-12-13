#!/usr/bin/env python


class RomanNumerals:
    def __init__(self):
        self.romans = {1: "I", 5: "V", 10: "X"}

    def convert_from_integer(self, integer):

        if integer in self.romans.keys():
            return self.romans[integer]
        else:
            return self.romans[1] + self.convert_from_integer(integer - 1)



