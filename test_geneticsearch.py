import unittest
from GeneticSearch import FixDuplicates, alphabet

class GeneticSearchCase(unittest.TestCase):
    def test_basic(self):
        setA = alphabet()
        setA.remove('b')
        setA.insert(1, 'c')
        setB = alphabet()
        setB.remove('c')
        setB.insert(1, 'c')
        self.assertListEqual(setB,FixDuplicates(setA)) 

    def test_fix_duplicates(self):
        fixed = FixDuplicates(['s', 't', 'n', 'i', 'g', 'k', 'b', 'o', 'u', 'p', 'c', 'f', 'y', 'e', 'h', 'd', 'l', 'r', 'a', 'v', 'v', 'v', 'v', 'v', 'x', 'v'])
        dupes = [x for x in fixed if fixed.count(x)>1]
        #print(fixed)
        #print(dupes)
        self.assertEqual(0, len(dupes))

if __name__ == '__main__':
    unittest.main()