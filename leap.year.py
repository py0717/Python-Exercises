# Leap in Python
# Given a year, report if it is a leap year
import unittest


def is_leap_year(x):
    """ returns True/False depending on if it is a leap year """
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 == 0:
            return True
        elif x % 100 == 0 and x % 400 != 0:
            return False
        else:
            return True
            
    else:
        return False



# test provided by exercism
class YearTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertIs(is_leap_year(2015), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(is_leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(is_leap_year(2100), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(2000), True)


# run test
unittest.main()
