def MatchWordsFromLetters(listOfUniqueLetters, wordlist):
    return [x for x in wordlist if not set(x)-set(listOfUniqueLetters)]

def CalculateWholeScore(sequence, wordlist):
    alphabetLength = 26
    return sum([len(MatchWordsFromLetters(sequence[:y], wordlist)) for y in list(range(alphabetLength))])

if __name__ == '__main__':
    letterList = ['c', 'a','t', 'h']
    wordList = ['cat', 'mat', 'hat', 'sat']