# Anagram
# Given a word and a list of possible anagrams, select the correct sublist
import unittest


def detect_anagrams(word, candidates):
    """ inputs string and list of candidate words, returns list of anagrams """

    # get rid of identical words in candidates list
    for n,i in enumerate(candidates):
        if i.lower() == word.lower():
            candidates.pop(n)

    
    # candidates2 will be a list of dictionaries
    # each dictionary contains letter counts for respective words
    candidates2=[] 

    for i in candidates:
        counts = {}
    
        for j in i:
            j = j.lower()
            
            if j in counts:
                counts[j] += 1
            else:
                counts[j] = 1

        candidates2.append(counts)

    # word2 is a dictionary with letter count of word
    word2 = {}

    for i in word:
        i = i.lower()
        
        if i in word2:
            word2[i] += 1
        else:
            word2[i] = 1
            
    # anagrams are words with same letter counts (equal dictionaries)
    # determine anagrams in candidates2 and replace each dictionary with True/False
    for n,i in enumerate(candidates2):
        if i == word2:
            candidates2[n] = True
        else:
            candidates2[n] = False

    # pop words out from candidates list if respective position in candidates2 is False
    # iterating in reverse allows us to keep same order while popping
    for n,i in reversed(list(enumerate(candidates2))):
        if i == False:
            candidates.pop(n)

    return candidates


# tests provided by exercism
class AnagramTests(unittest.TestCase):
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        self.assertEqual(detect_anagrams("diaper", candidates), [])

    def test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        self.assertEqual(
            detect_anagrams("master", candidates), ["stream", "maters"])

    def test_does_not_detect_anagram_subsets(self):
        self.assertEqual(detect_anagrams("good", ["dog", "goody"]), [])

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        self.assertEqual(detect_anagrams("listen", candidates), ["inlets"])

    def test_detects_three_anagrams(self):
        candidates = [
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]
        self.assertEqual(
            detect_anagrams("allergy", candidates),
            ["gallery", "regally", "largely"])

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        self.assertEqual(detect_anagrams("mass", ["last"]), [])

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("Orchestra", candidates), ["Carthorse"])

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("Orchestra", candidates), ["carthorse"])

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("orchestra", candidates), ["Carthorse"])

    def test_does_not_detect_a_anagram_if_the_original_word_is_repeated(self):
        self.assertEqual(detect_anagrams("go", ["go Go GO"]), [])

    def test_anagrams_must_use_all_letters_exactly_once(self):
        self.assertEqual(detect_anagrams("tapper", ["patter"]), [])

    def test_capital_word_is_not_own_anagram(self):
        self.assertEqual(detect_anagrams("BANANA", ["Banana"]), [])


# run tests
unittest.main()
