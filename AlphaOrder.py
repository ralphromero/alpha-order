from itertools import groupby
import matplotlib.pyplot as plt
import string

def GetAdjacentPairList(word):
    pairs = [word[x] + word[x+1] for x,y in enumerate(word) if x+1 < len(word)]
    sortedPairs = [''.join(sorted(x)) for x in pairs]
    sortedPairsNoDupes = list(set(sortedPairs))
    sortedPairsNoDupes = [x for x in sortedPairsNoDupes if x[0] != x[1]]
    return sorted(sortedPairsNoDupes)

def CombineFrequencyDictAndList(theDict, nonDupeList):
    return {x:(int(theDict.get(x, 0))+1) for x in nonDupeList}

def UniqueValuesFromDict(theDict):
    return sorted(list(set([theDict[x] for x in theDict])),reverse=True)

def GetDictKeysFromValues(keyVals, val):
    tempList = [list(x) for x in keyVals if keyVals[x] == val]
    return SortMakeUniqueList([x for y in tempList for x in y])

def SortMakeUniqueList(theList):
    return sorted(list(set(theList)))

def CombineUniqueSecondList(lista, listb):
    return lista + [x for x in listb if x not in lista]

def GetWordsByLetters(wordlist, characters):
    listOfWords = []
    #TODO find all the words we can created in this wordlist using these characters.
    return listOfWords

def PlotLettersByWords(wordList, characterList):
    x = [2, 4, 6]#TODO character amount in this characterlist
    y = [1, 3, 5]#TODO how many words we can make using x characters
    plt.plot(x, y)
    plt.show()

def PairedFrequencyAlphaOrder(wordlist):
    adjacencyDict = {}
    orderList = []
    for y in wordlist:
        adjacencyDict.update(CombineFrequencyDictAndList(adjacencyDict, GetAdjacentPairList(y)))
    uniqueValues = UniqueValuesFromDict(adjacencyDict)
    orderList = [CombineUniqueSecondList(orderList, GetDictKeysFromValues(adjacencyDict, x)) for x in uniqueValues]
    flatlist = [x for y in orderList for x in y]
    finlist = []
    for x in flatlist:
        if(x not in finlist):
            finlist.append(x)
    return finlist

def BasicFrequencyAlphaOrder(wordlist):
    orderList = []
    letterList = [y for x in wordlist for y in x]
    freqDict = {x:letterList.count(x) for x in letterList}
    for x,y in freqDict.items():
        print(x + ":" + str(y))
    uniqueValues = UniqueValuesFromDict(freqDict)
    orderList = [CombineUniqueSecondList(orderList, GetDictKeysFromValues(freqDict, x)) for x in uniqueValues]
    return [y for x in orderList for y in x]

def RemoveDuplicatesAndLowerFromList(wordlist):
    dupes = [x for x in lines if wordlist.count(x) > 1]
    if(len(dupes) != 0):
        print("Duplicates found in word list. Remove these:" + str(dupes))
    return list(set([x.lower() for x in lines]))

with open ('WordList - twoyearold.txt') as f:
    lines = f.read().splitlines()
    modifiedAlphabet = PairedFrequencyAlphaOrder(RemoveDuplicatesAndLowerFromList(lines))
    #print(modifiedAlphabet)
    classicAlphabet = string.ascii_lowercase[:26]
    #PlotLettersByWords(classicAlphabet)
    #PlotLettersByWords(modifiedAlphabet)





