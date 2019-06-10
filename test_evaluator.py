import unittest
from Evaluator import MatchWordsFromLetters, CalculateWholeScore

class EvaluatorTestCase(unittest.TestCase):
    def test_basic_count(self):
        letterList = ['c', 'a','t', 'h']
        wordList = ['cat', 'mat', 'hat', 'sat']
        self.assertListEqual(MatchWordsFromLetters(letterList, wordList), ['cat', 'hat'])

    def test_complete_score(self):
        letterList = ['c', 'a','t', 'h']
        wordList = ['cat', 'mat', 'hat', 'sat']
        self.assertEquals(CalculateWholeScore(letterList, wordList), 45)

if __name__ == '__main__':
    unittest.main()