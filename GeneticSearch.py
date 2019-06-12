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
    for pos, x in enumerate(sequence):
        futureSequence = sequence[pos+1:]
        if(x in futureSequence):
            tempList = newList.copy()
            tempList.append(x)
            getOne = list(set(alpha) - set(tempList)-set(futureSequence))
            newList.append(getOne[0])
        else:
            newList.append(x)
    newList.reverse()
    return newList

def CreateChildrenFromParents(parent1, parent2):
    child1 = shuffle(parent1, 4)
    child2 = shuffle(parent2, 4)
    child1_5 = FixDuplicates(MixParents(parent1, parent2, 2))
    child2_5 = FixDuplicates(MixParents(parent2, parent1, 2))
    child1_4 = shuffle(parent1, 2)
    child2_4 = shuffle(parent2, 2)
    child1_3 = FixDuplicates(MixParents(parent1, parent2, 3))
    child2_3 = FixDuplicates(MixParents(parent2, parent1, 3))
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
    best = []
    children = []
    result = []
    for x in range(3):
        print("Starting Genetic Algorithm " + str(x+1))
        for generation in range(generations):
            print("Generation " + str(generation+1))
            logging.info("Starting a new generation.")
            if(len(children)==0):
                par1, par2 = alphabet(),shuffle(alphabet(), 20)
            children = CreateChildrenFromParents(par1, par2)
            children.append(best.copy()) #damages diversity
            logging.info("Children created: " + str(len(children)))
            childrenScored = sorted([(x, CalculateWholeScore(x, wordlist)) for x in children], key=takeSecond, reverse=True)
            logging.info("Child scored: " + str((childrenScored[0])[1]) + " using: " + str((childrenScored[0])[0]))
            logging.info("man score " + str(CalculateWholeScore(((childrenScored[0])[0]), wordlist)))
            bestTwo = childrenScored[:2]
            left = CalculateWholeScore(best, wordlist)
            right = CalculateWholeScore((childrenScored[0])[0], wordlist)
            if(left < right):
                best = list((bestTwo[0])[0])
            par1, par2 = (bestTwo[0])[0], (bestTwo[1])[0]
        result.append(list(best))
    return result

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    with open ('WordList - twoyearold.txt') as f:
        lines = f.read().splitlines()
        logging.info("Starting")
        Search(lines, 100)
