# RNA Transcription
# Obtain a DNA strand, return its RNA Complement Transcription
import unittest


def to_rna(dna):
    """ inputs DNA strand and returns its RNA complement """
    
    rna = []
    
    # converts dna to rna; if dna has incorrect nucleotide, then raise error
    try:
        for n,i in enumerate(dna):
            if i == 'A':
                rna.append('U')
            elif i == 'C':
                rna.append('G')
            elif i == 'G':
                rna.append('C')
            elif i == 'T':
                rna.append('A')
            else:
                i + 5
    except:
        raise ValueError('Check the DNA strand for error.')
        
    return ''.join(rna)


# test provided by exercism
class RNATranscriptionTests(unittest.TestCase):

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual(to_rna('C'), 'G')

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurrences(self):
        self.assertEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')


# run test
unittest.main()
