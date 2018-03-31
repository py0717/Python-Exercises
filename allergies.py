# Allergies
# Given a person's allergy score, determine whether or not they're
#     allergic to a given item, and their full list of allergies
# Note: Program should ignore allergens with score 256, 512, 1024, etc
import unittest


class Allergies:
    def __init__(self, score):
        self.score = score

    def lst(self):
        """ returns list of allergies using initialized score """

        key = [('cats', 128), ('pollen', 64), ('chocolate', 32), ('tomatoes', 16),
               ('strawberries', 8), ('shellfish', 4), ('peanuts', 2), ('eggs', 1)]

        # ignore allergens with scores above 256
        x = self.score
        
        if(x >= 256):
            x = x % 1024 % 512 % 256

        # iterate through key to make allergies list
        allergies = []

        for i in key:
            if(i[1] <= x):
                x = x - i[1]
                allergies.append(i[0])
            else:
                continue

        # reverse allergies list
        # we want a list with increasing allergen scores
        return allergies[::-1]

    def is_allergic_to(self, x):
        """ input string item x that we want to check for and determine if allergic;
            returns True/False """

        # obtain list of allergies using lst method
        allergies = self.lst()

        # check to see if x is in list obtained 
        if x in allergies:
            return True
        else:
            return False
    

# tests given by exercism
class AllergiesTests(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertIs(allergies.is_allergic_to('peanuts'), False)
        self.assertIs(allergies.is_allergic_to('cats'), False)
        self.assertIs(allergies.is_allergic_to('strawberries'), False)

    def test_is_allergic_to_eggs(self):
        self.assertIs(Allergies(1).is_allergic_to('eggs'), True)

    def test_allergic_to_eggs_in_addition_to_other_stuff(self):
        allergies = Allergies(5)
        self.assertIs(allergies.is_allergic_to('eggs'), True)
        self.assertIs(allergies.is_allergic_to('shellfish'), True)
        self.assertIs(allergies.is_allergic_to('strawberries'), False)

    def test_no_allergies_at_all(self):
        self.assertEqual(Allergies(0).lst(), [])

    def test_allergic_to_just_eggs(self):
        self.assertEqual(Allergies(1).lst(), ['eggs'])

    def test_allergic_to_just_peanuts(self):
        self.assertEqual(Allergies(2).lst(), ['peanuts'])

    def test_allergic_to_just_strawberries(self):
        self.assertEqual(Allergies(8).lst(), ['strawberries'])

    def test_allergic_to_eggs_and_peanuts(self):
        self.assertCountEqual(Allergies(3).lst(), ['eggs', 'peanuts'])

    def test_allergic_to_more_than_eggs_but_not_peanuts(self):
        self.assertCountEqual(Allergies(5).lst(), ['eggs', 'shellfish'])

    def test_allergic_to_lots_of_stuff(self):
        self.assertCountEqual(
            Allergies(248).lst(),
            ['strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])

    def test_allergic_to_everything(self):
        self.assertCountEqual(
            Allergies(255).lst(), [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    def test_ignore_non_allergen_score_parts_only_eggs(self):
        self.assertEqual(Allergies(257).lst(), ['eggs'])

    def test_ignore_non_allergen_score_parts(self):
        self.assertCountEqual(
            Allergies(509).lst(), [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


# run tests
unittest.main()    




      
