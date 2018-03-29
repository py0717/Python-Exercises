# Hamming Exercise
# Hamming Difference = number of different nucleotides from equivalent in another strand (mutations)
import unittest


def hamming_distance(one, two):
    """ inputs two dna strands and returns integer (hamming difference) """

    counter = 0

    # check that strands are equal length
    if len(one) != len(two):
        raise ValueError(".+")

    # count each difference
    for n,i in enumerate(one):
        if i != two[n]:
            counter += 1

    return counter


    
# tests from exercism
class HammingTest(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(hamming_distance("", ""), 0)

    def test_identical_strands(self):
        self.assertEqual(hamming_distance("A", "A"), 0)

    def test_long_identical_strands(self):
        self.assertEqual(hamming_distance("GGACTGA", "GGACTGA"), 0)

    def test_complete_distance_in_single_nucleotide_strands(self):
        self.assertEqual(hamming_distance("A", "G"), 1)

    def test_complete_distance_in_small_strands(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2)

    def test_small_distance_in_small_strands(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1)

    def test_small_distance(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1)

    def test_small_distance_in_long_strands(self):
        self.assertEqual(hamming_distance("ACCAGGG", "ACTATGG"), 2)

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(hamming_distance("AAG", "AAA"), 1)

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(hamming_distance("AAA", "AAG"), 1)

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2)

    def test_large_distance(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4)

    def test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming_distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming_distance("ATA", "AGTG")
            
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


# run test
unittest.main()
