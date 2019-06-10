import string
import logging, sys
from random import randint
from Evaluator import MatchWordsFromLetters, CalculateWholeScore

def shuffle(sequence, shakes):
    for x in range(shakes):
        fromIndex, toIndex = randint(0,25), randint(0,25)
        while(toIndex == fromIndex):
            toIndex = randint(0,25)
        sequence[fromIndex], sequence[toIndex] = sequence[toIndex], sequence[fromIndex]
    return sequence

def alphabet():
    return list(string.ascii_lowercase[:26])

def CreateChildren():
    child1, child2, child3 = shuffle(alphabet(), 5),shuffle(alphabet(), 5),shuffle(alphabet(), 5)
    return [child1, child2, child3]

def MixParents(parent1, parent2, sliceIndex):
    child = list(parent1)
    for pos, character in enumerate(parent2):
        if(int(pos/sliceIndex)%2==0):
            child[pos] = character
    return child

def FixDuplicates(sequence):
    alpha = alphabet()
    newList = []
    sequence.reverse()
    #print("SeqCount:" + str(len(sequence)))
    for pos, x in enumerate(sequence):
        #print("For loop: Pos:"  + str(pos) + " val:" + x)
        futureSequence = sequence[pos+1:]
        #print("NewCount:" + str(len(newList)))
        if(x in futureSequence):
            tempList = newList.copy()
            tempList.append(x)
            getOne = list(set(alpha) - set(tempList)-set(futureSequence))
            #print("Remainders: " + str(getOne))
            #print("Dupe found. Replacing with: " + getOne[0] + " at pos: " + str(pos))
            newList.append(getOne[0])
        else:
            newList.append(x)
    newList.reverse()
    #print(newList)
    #count = [x for x in newList if newList.count(x)>1]
    #print(str(count))
    #print("SeqCount:" + str(len(sequence)))
    return newList

def CreateChildrenFromParents(parent1, parent2):
    child1 = shuffle(parent1, 5)
    child2 = shuffle(parent2, 5)
    child1_5 = FixDuplicates(MixParents(parent1, parent2, 2))
    child2_5 = FixDuplicates(MixParents(parent2, parent1, 2))
    child1_4 = shuffle(parent1, 2)
    child2_4 = shuffle(parent2, 2)
    child1_3 = FixDuplicates(MixParents(parent1, parent2, 3))
    child2_3 = FixDuplicates(MixParents(parent2, parent1, 3))
    #secretaryChild = FixDuplicates(MixParents((shuffle(alphabet(), 20)), parent1, 3))
    #milkmanChild = FixDuplicates(MixParents((shuffle(alphabet(), 20)), parent2, 5))
    secretaryChild = shuffle(alphabet(),15)
    milkmanChild = shuffle(alphabet(),15)
    return [child1,
            child2,
            child1_5,
            child2_5, 
            child1_4, 
            child2_4, 
            child1_3, 
            child2_3, 
            secretaryChild, 
            milkmanChild
            ]

def takeSecond(tup):
    return tup[1]

def Search(wordlist, generations):
    par1, par2 = [], []
    bestParent1 = []
    bestParent2 = []
    best = []
    children = []
    for generation in range(generations):
        logging.info("Starting a new generation.")
        print("best is:" + str(CalculateWholeScore(best, wordlist)))
        if(len(children)==0):
            par1, par2 = alphabet(),shuffle(alphabet(), 20)
        children = CreateChildrenFromParents(par1, par2)
        #children.append(best.copy()) #damages diversity
        logging.info("Children created: " + str(len(children)))
        childrenScored = sorted([(x, CalculateWholeScore(x, wordlist)) for x in children], key=takeSecond, reverse=True)
        logging.info("Child scored: " + str((childrenScored[0])[1]) + " using: " + str((childrenScored[0])[0]))
        logging.info("man score " + str(CalculateWholeScore(((childrenScored[0])[0]), wordlist)))
        bestTwo = childrenScored[:2]
        left = CalculateWholeScore(best, wordlist)
        right = CalculateWholeScore((childrenScored[0])[0], wordlist)
        if(left < right):
            print("enter")
            print("overwrite: " + str(left) + " with:" + str(right))
            best = list((bestTwo[0])[0])
            bestParent1 = par1.copy()
            bestParent2 = par2.copy()
        par1, par2 = (bestTwo[0])[0], (bestTwo[1])[0]
        #if(CalculateWholeScore(best, wordlist) < CalculateWholeScore(par1, wordlist)):
        #    best = par1

    print("Best score overall: " + str(CalculateWholeScore(best, wordlist)) + " using: " + str(best))
    print("Parent1: " + str(CalculateWholeScore(bestParent1, wordlist)) + " using: " + str(bestParent1))
    print("Parent2: " + str(CalculateWholeScore(bestParent2, wordlist)) + " using: " + str(bestParent2))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    with open ('WordList - twoyearold.txt') as f:
        lines = f.read().splitlines()
        logging.info("Starting")
        Search(lines, 500)

        #par1, par2 = alphabet(),shuffle(alphabet(), 20)
        #print(par1)
        #print(par2)
