import matplotlib.pyplot as plt
from Evaluator import MatchWordsFromLetters

def PlotCharacterLists(wordlist, charListLabel):
    alphabetLength = 26
    xAxis = list(range(alphabetLength))
    for x in charListLabel:
        alist = (charListLabel[x])[0]
        print(alist)
        plt.plot(xAxis, alist, label=(charListLabel[x])[1])
    plt.legend(loc='upper left')
    plt.show()