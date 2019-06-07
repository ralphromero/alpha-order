import matplotlib.pyplot as plt
from Evaluator import MatchWordsFromLetters

def PlotCharacterLists(wordlist, charListLabel):
    alphabetLength = 26
    xAxis = list(range(alphabetLength))
    for x in charListLabel:
        otherAxis = [len(MatchWordsFromLetters((x[0])[:y], wordlist)) for y in xAxis]
        plt.plot(xAxis, otherAxis, label=x[1])
    plt.legend(loc='upper left')
    plt.show()


# def PlotLettersByWords(wordList, characterList, labelx):
#     classicAlphabet = string.ascii_lowercase[:26]
#     xAxis = list(range(len(classicAlphabet)))
#     yAxis = [len(MatchWordsFromLetters(characterList[:x], wordList)) for x in xAxis]
#     zAxis = [len(MatchWordsFromLetters(classicAlphabet[:x], wordList)) for x in xAxis]
#     plt.plot(xAxis, yAxis, label=labelx)
#     plt.plot(xAxis, zAxis, label="Classic Alphabet")
#     plt.legend(loc='upper left')
#     plt.show()