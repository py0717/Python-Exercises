# Run Length Encoding
# Implement Run-Length Encoding and Decoding
# RLE is a form of data compression, where runs (consecutive data elements) are replaced by element and its count
# For this exercise, assume that the string will only contain letters
import unittest


def encode(phrase):
    """ inputs string and returns RLE string """

    phrase = list(phrase)

    # create list (phrase2) that alternates between count and letter
    phrase2 = []
    count = 1

    phrase.append(9)  # for for loop; 9 has no significance here
    
    for n,i in enumerate(phrase[:-1]):
        if i == phrase[n+1]:
            count += 1
        else:
            phrase2.append(str(count))
            phrase2.append(i)
            count = 1

    # remove all '1's in list
    while '1' in phrase2:
        phrase2.remove('1')

    # joined phrase2 is the final encoded string
    return(''.join(phrase2))


def decode(phrase):
    """ inputs RLE string and returns decoded string """

    # put a '1' before single letters or spaces in phrase
    phrase = list(phrase)
    
    try:
        if phrase[0].isalpha() == True or phrase[0] == ' ':
                phrase.insert(0, '1')
    except:
        pass

    phrase.append(9)   # for for loop; 9 has no significance here
    
    try:
        for n,i in enumerate(phrase):
            if(i.isalpha() == True or i == ' ') and (phrase[n+1].isalpha() == True or phrase[n+1] == ' '):
                phrase.insert(n+1, '1')
    except:
        pass
            
    # combine consecutive numbers. for example: ['1', '2'] --> ['12']
    phrase2 = []

    for n,i in enumerate(phrase):
        try:
            if i.isdigit() == True and phrase[n+1].isdigit() == True:
                phrase2.append(i + phrase[n+1])
                phrase.pop(n+1)      
            else:
                phrase2.append(i)
        except:
            pass
            
    # phrase2 now alternates between count and data
    # multiply first two elements (count and data) and add to decoded
    decoded = ''
    
    while(len(phrase2) > 0):
        decoded += int(phrase2[0]) * phrase2[1]
        phrase2.pop(0)
        phrase2.pop(0)

    return(decoded)
        

# tests provided by exercism
class RunLengthEncodingTests(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertMultiLineEqual(encode(''), '')

    def test_encode_single_characters_only_are_encoded_without_count(self):
        self.assertMultiLineEqual(encode('XYZ'), 'XYZ')

    def test_encode_string_with_no_single_characters(self):
        self.assertMultiLineEqual(encode('AABBBCCCC'), '2A3B4C')

    def test_encode_single_characters_mixed_with_repeated_characters(self):
        self.assertMultiLineEqual(
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
            '12WB12W3B24WB')

    def test_encode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual(encode('  hsqq qww  '), '2 hs2q q2w2 ')

    def test_encode_lowercase_characters(self):
        self.assertMultiLineEqual(encode('aabbbcccc'), '2a3b4c')

    def test_decode_empty_string(self):
        self.assertMultiLineEqual(decode(''), '')

    def test_decode_single_characters_only(self):
        self.assertMultiLineEqual(decode('XYZ'), 'XYZ')

    def test_decode_string_with_no_single_characters(self):
        self.assertMultiLineEqual(decode('2A3B4C'), 'AABBBCCCC')

    def test_decode_single_characters_with_repeated_characters(self):
        self.assertMultiLineEqual(
            decode('12WB12W3B24WB'),
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')

    def test_decode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual(decode('2 hs2q q2w2 '), '  hsqq qww  ')

    def test_decode_lower_case_string(self):
        self.assertMultiLineEqual(decode('2a3b4c'), 'aabbbcccc')

    def test_combination(self):
        self.assertMultiLineEqual(decode(encode('zzz ZZ  zZ')), 'zzz ZZ  zZ')


# run tests
unittest.main()
