def MatchWordsFromLetters(listOfUniqueLetters, wordlist):
    return [x for x in wordlist if not set(x)-set(listOfUniqueLetters)]

if __name__ == '__main__':
    letterList = ['c', 'a','t', 'h']
    wordList = ['cat', 'mat', 'hat', 'sat']