# ISBN Verifier
import unittest, string

def verify(number):
    """input string of numbers and determine if valid ISBN-10 number (returns True/False) """

    # get rid of hypens
    number = list(number)

    while '-' in number:
        number.remove('-')

    # make sure number has 10 characters
    if len(number) != 10:
        return False

    # create new list
    # make sure digits only 
    # last digit can be 'X' but is converted to 10
    number2 = []
    
    for n,i in enumerate(number):
        if i in '0123456789':
            number2.append(int(i))
        elif number[-1] == 'X':
            number2.append(10)
        else:
            return False
    
    # check using formula that ISBN is valid
    total = 0; counter = 10

    for i in number2:
        total = total + i*counter
        counter -= 1
        
    if total % 11 == 0:
        return True
    else:
        return False


# test from exercism   
class IsbnVerifierTests(unittest.TestCase):

    def test_valid_isbn_number(self):
        self.assertIs(verify('3-598-21508-8'), True)

    def test_invalid_check_digit(self):
        self.assertIs(verify('3-598-21508-9'), False)

    def test_valid_with_X_check_digit(self):
        self.assertIs(verify('3-598-21507-X'), True)

    def test_invalid_check_digit_other_than_X(self):
        self.assertIs(verify('3-598-21507-A'), False)

    def test_invalid_character_in_isbn(self):
        self.assertIs(verify('3-598-2K507-0'), False)

    def test_invalid_X_other_than_check_digit(self):
        self.assertIs(verify('3-598-2X507-9'), False)

    def test_valid_isbn_without_separating_dashes(self):
        self.assertIs(verify('3598215088'), True)

    def test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertIs(verify('359821507X'), True)

    def test_invalid_isbn_without_check_digit_and_dashes(self):
        self.assertIs(verify('359821507'), False)

    def test_invalid_too_long_isbn_with_no_dashes(self):
        self.assertIs(verify('3598215078X'), False)

    def test_invalid_isbn_without_check_digit(self):
        self.assertIs(verify('3-598-21507'), False)

    def test_invalid_too_long_isbn(self):
        self.assertIs(verify('3-598-21507-XX'), False)

    def test_invalid_check_digit_X_used_for_0(self):
        self.assertIs(verify('3-598-21515-X'), False)

    def test_valid_empty_isbn(self):
        self.assertIs(verify(''), False)


# run test
unittest.main()    
