# Pangram
# Determine if sentence is a pangram
# A pangram is a sentence using every letter of the alphabet at least once
import unittest, re


def is_pangram(phrase):
    """ inputs string and determines if pangram (returns True/False) """
    
    phrase = ''.join(re.findall('[a-zA-Z]+', phrase))
    phrase = set(phrase.lower())

    if len(phrase) == 26:
        return True
    else:
        return False


# test provided by exercism      
class PangramTests(unittest.TestCase):

    def test_sentence_empty(self):
        self.assertIs(is_pangram(''), False)

    def test_recognizes_a_perfect_lower_case_pangram(self):
        self.assertIs(is_pangram('abcdefghijklmnopqrstuvwxyz'), True)

    def test_pangram_with_only_lower_case(self):
        self.assertIs(
            is_pangram('the quick brown fox jumps over the lazy dog'),
            True)

    def test_missing_character_x(self):
        self.assertIs(
            is_pangram('a quick movement of the enemy will '
                       'jeopardize five gunboats'),
            False)

    def test_another_missing_character(self):
        self.assertIs(is_pangram('five boxing wizards jump quickly at it'),
                      False)

    def test_pangram_with_underscores(self):
        self.assertIs(
            is_pangram('the_quick_brown_fox_jumps_over_the_lazy_dog'),
            True)

    def test_pangram_with_numbers(self):
        self.assertIs(
            is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs'),
            True)

    def test_missing_letters_replaced_by_numbers(self):
        self.assertIs(
            is_pangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'),
            False)

    def test_pangram_with_mixedcase_and_punctuation(self):
        self.assertIs(
            is_pangram('"Five quacking Zephyrs jolt my wax bed."'),
            True)

    def test_upper_and_lower_case_versions_of_the_same_character(self):
        self.assertIs(
            is_pangram('the quick brown fox jumped over the lazy FX'),
            False)

        
# run test
unittest.main()
