import unittest
from Evaluator import MatchWordsFromLetters

class EvaluatorTestCase(unittest.TestCase):
    def test_basic_count(self):
        letterList = ['c', 'a','t', 'h']
        wordList = ['cat', 'mat', 'hat', 'sat']
        self.assertListEqual(MatchWordsFromLetters(letterList, wordList), ['cat', 'hat'])

if __name__ == '__main__':
    unittest.main()