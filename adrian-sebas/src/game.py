class Kata(object):
    tens = ['i','x']
    fives = ['v', 'l']
    def int_to_roman(self, number):
        if number is 0:
            return ''
        if number <= 3:
            return 'i' + self.int_to_roman(number - 1)
        if number is 4:
            return 'i' + self.int_to_roman(number + 1)
        if number >= 5 and number < 9:
            return 'v' + self.int_to_roman(number - 5)
        if number is 9:
            return 'i' + self.int_to_roman(number + 1)
        if number >= 10 and number < 40:
            return 'x' + self.int_to_roman(number - 10)
        if number >= 40 and number < 50:
            return 'x' + self.int_to_roman(number + 10)
        if number >=50 and number < 90:
            return 'l' + self.int_to_roman(number - 50)
        if number in range(90, 100):
            return 'x' + self.int_to_roman(number - 10)



        return 'i'
