import matplotlib.pyplot as plt
from Evaluator import MatchWordsFromLetters

def PlotCharacterLists(wordlist, charListLabel):
    alphabetLength = 26
    xAxis = list(range(alphabetLength))
    for x in charListLabel:
        otherAxis = [len(MatchWordsFromLetters((x[0])[:y], wordlist)) for y in xAxis]
        plt.plot(xAxis, otherAxis, label=x[1] + " Score: " + str(sum(otherAxis)))
    plt.legend(loc='upper left')
    plt.show()