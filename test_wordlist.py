import unittest
from AlphaOrder import GetDictKeysFromValues, CombineUniqueSecondList, BasicFrequencyAlphaOrder

class WordTestCase(unittest.TestCase):
    
    def test_get_dict_keys(self):
        mydict = {'a':1,'b':2,'c':3, 'd':1}
        self.assertListEqual(GetDictKeysFromValues(mydict, 1), ['a', 'd'])
    
    def test_combine_unique_second_list(self):
        lista = ['a','b','c']
        listb = ['b','d']
        self.assertListEqual(CombineUniqueSecondList(lista, listb), ['a','b','c','d'])
    
    def test_get_dict_keys_from_values(self):
        dicta = {'ab':1, 'er':2, 'fd':3}
        self.assertListEqual(GetDictKeysFromValues(dicta, 2), ['e','r'])
    
    def test_basic(self):
        wordlist = ['abcc','def']
        self.assertListEqual(BasicFrequencyAlphaOrder(wordlist), ['c','a','b','d','e','f'])
    
    #def test_get_words_by_letters(self):
    #    wordList = ['cab', 'car', 'dog', 'carp','card']
    #    characterList = ['a','b','c','r','d']
    #    self.assertEqual(GetWordsByLetters(wordList, characterList), ['cab', 'car','card'])

if __name__ == '__main__':
    unittest.main()