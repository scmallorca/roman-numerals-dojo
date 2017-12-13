#!/usr/bin/env python

class RomanNumerals:
    def convert_from_integer(self, integer):
        d = {1: "I", 2: "II", 3: "III", 5: "V", 10: "X"}

        return d[integer]



