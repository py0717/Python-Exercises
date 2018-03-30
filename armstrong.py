# Armstrong Numbers
# An Armstrong number is a number that is the sum of its own digits each raised
#     to the power of the number of digits
import unittest


def is_armstrong(x):
    """ inputs integer and determines if Armstrong number (returns True/False) """

    # get sum of all digits of x raised to to the power of the number of digits
    sum = 0
    x = list(str(x))
    
    for i in x:
        sum = sum + int(i)**len(x)

    # determine if sum is to equal to input number x    
    if(sum == int(''.join(x))):
        return True
    else:
        return False

    
# tests from exercism
class ArmstrongTests(unittest.TestCase):

    def test_single_digit_numbers_are_armstrong_numbers(self):
        self.assertIs(is_armstrong(5), True)

    def test_there_are_no_two_digit_armstrong_numbers(self):
        self.assertIs(is_armstrong(10), False)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(153), True)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(100), False)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(9474), True)

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(9475), False)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        self.assertIs(is_armstrong(9926315), True)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        self.assertIs(is_armstrong(9926314), False)


# run tests
unittest.main()
