# Rotational Cipher
# Create an implementation of the rotational cipher aka the Caesar cipher
# This is a simple shift cipher that transposes all letters using an integer
#    key between 0 and 26. The generation notation for rotational ciphers
#    is ROT+<key>. Most commonly used is ROT13
import string, unittest


class rotational_cipher:
    def rotate(phrase, key):
        """ inputs string phrase and integer key, returns transposed string """
        
        letters = string.ascii_lowercase
        LETTERS = string.ascii_uppercase    

        # transpose all letters according to key
        newphrase = ''
        
        for i in phrase:
            if(i in letters):
                location = (letters.find(i) + key) % 26
                newphrase += letters[location]              
            elif(i in LETTERS):
                location = (LETTERS.find(i) + key) % 26
                newphrase += LETTERS[location]
            else:
                newphrase += i
                
        return newphrase
    

# tests from exercism
class RotationalCipher(unittest.TestCase):
    def test_rotate_a_by_0(self):
        self.assertEqual(rotational_cipher.rotate('a', 0), 'a')

    def test_rotate_a_by_1(self):
        self.assertEqual(rotational_cipher.rotate('a', 1), 'b')

    def test_rotate_a_by_26(self):
        self.assertEqual(rotational_cipher.rotate('a', 26), 'a')

    def test_rotate_m_by_13(self):
        self.assertEqual(rotational_cipher.rotate('m', 13), 'z')

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        self.assertEqual(rotational_cipher.rotate('n', 13), 'a')

    def test_rotate_capital_letters(self):
        self.assertEqual(rotational_cipher.rotate('OMG', 5), 'TRL')

    def test_rotate_spaces(self):
        self.assertEqual(rotational_cipher.rotate('O M G', 5), 'T R L')

    def test_rotate_numbers(self):
        self.assertEqual(
            rotational_cipher.rotate('Testing 1 2 3 testing', 4),
            'Xiwxmrk 1 2 3 xiwxmrk')

    def test_rotate_punctuation(self):
        self.assertEqual(
            rotational_cipher.rotate("Let's eat, Grandma!", 21),
            "Gzo'n zvo, Bmviyhv!")

    def test_rotate_all_letters(self):
        self.assertEqual(
            rotational_cipher.rotate("The quick brown fox jumps"
                                     " over the lazy dog.", 13),
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")


# run tests
unittest.main()
