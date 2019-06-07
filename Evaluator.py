def MatchWordsFromLetters(listOfUniqueLetters, wordlist):
    return [x for x in wordlist if not set(x)-set(listOfUniqueLetters)]

def CountWords(listOfUniqueLetters, wordlist):
    return len(MatchWordsFromLetters(listOfUniqueLetters, wordlist))

def CalculateOptimalScore(scoreList):
    return sum([x for x in scoreList])

if __name__ == '__main__':
    letterList = ['c', 'a','t', 'h']
    wordList = ['cat', 'mat', 'hat', 'sat']