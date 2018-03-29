# Isogram
# Determine if a word or phrase is an isogram
# Isogram is a word or phrase without a repeating letter, however spaces and
#      and hypens are allowed to appear multiple times
import re
import unittest



def is_isogram(phrase):
    """ inputs string and determines if isogram (returns True/False) """

    # strip string of everything except letters
    phrase = ''.join(re.findall('[a-zA-Z]+', phrase))
    phrase = phrase.lower()

    # obtain unique letters of phrase
    phrase2 = set(phrase)

    # compare lengths. if equal, then there were no duplicate letters
    if len(phrase) == len(phrase2):
        return True
    else:
        return False


# test from exercism   
class TestIsogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertIs(is_isogram(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(is_isogram("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(is_isogram("eleven"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(is_isogram("Alphabet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    def test_isogram_with_duplicated_hyphen(self):
        self.assertIs(is_isogram("six-year-old"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(is_isogram("accentor"), False)

    # Additional tests for this track

    def test_isogram_with_duplicated_letter_and_nonletter_character(self):
        self.assertIs(is_isogram("Aleph Bot Chap"), False)


# run test
unittest.main()
