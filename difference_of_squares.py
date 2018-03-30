# Difference of Squares
# Find the difference between the square of the sum and the sum of the squares
#       of the first N natural numbers
import unittest


def square_of_sum(x):
    """ inputs integer and returns square of the sum """
    
    sqsum = sum(i for i in range(1,x+1))
    sqsum = sqsum**2

    return sqsum

def sum_of_squares(x):
    """ inputs integer and returns sum of squares of first N numbers """
    
    sumsq = 0

    for i in range(1,x+1):
        sumsq += i**2  

    return sumsq

def difference(x):
    """ inputs integer and returns difference of sqsum and sumsq """
    
    return(square_of_sum(x) - sum_of_squares(x))


# tests from exercism
class DifferenceOfSquaresTest(unittest.TestCase):    
    def test_square_of_sum_1(self):
        self.assertEqual(square_of_sum(1), 1)

    def test_square_of_sum_5(self):
        self.assertEqual(square_of_sum(5), 225)

    def test_square_of_sum_100(self):
        self.assertEqual(square_of_sum(100), 25502500)

    def test_sum_of_squares_1(self):
        self.assertEqual(sum_of_squares(1), 1)

    def test_sum_of_squares_5(self):
        self.assertEqual(sum_of_squares(5), 55)

    def test_sum_of_squares_100(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_difference_of_squares_1(self):
        self.assertEqual(difference(1), 0)

    def test_difference_of_squares_5(self):
        self.assertEqual(difference(5), 170)

    def test_difference_of_squares_100(self):
        self.assertEqual(difference(100), 25164150)


# run tests
unittest.main()
