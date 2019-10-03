import nltk
from nltk.corpus import wordnet as wn
import math

def Common(syn1, syn2):
    length = 0
    for sy in syn1:
        if sy in syn2:
            length += 1
        else:
            break
    return length

def PathDistance(syn1, syn2):
    length = Common(syn1,syn2)
    dist = len(syn1) + len(syn2) - 2 * length
    return dist

def LCS(syn1, syn2):
    pos = Common(syn1,syn2)
    subsumer = syn1[pos - 1]
    ans = [pos,subsumer]
    return ans 

def PathSimilarity(syn1, syn2):
    max = 0
    for sy1 in syn1:
        for sy2 in syn2:
            dist = PathDistance(sy1, sy2)
            if max <= dist:
                max = dist
    return -math.log(max)

def Wu_Palmer(syn1,syn2):
    max = 0
    for sy1 in syn1:
        for sy2 in syn2:
            lcsAns = LCS(sy1,sy2)
            lcsDepth = lcsAns[0]
            wup = 2 * lcsDepth / (len(sy1) + len(sy2))
            if max <= wup:
                max = wup
    return max

def Leacock_Chodorow(syn1,syn2):
    max = 0
    for sy1 in syn1:
        for sy2 in syn2:
            lch = math.log(PathDistance(sy1,sy2)/(2*19))
            if max <= lch or max == 0:
                max = lch
    return max

def ProcessSynsets(syns1):
    syn1 = []
    for item in syns1:
        for path in item.hypernym_paths():
            pathI = []
            for k in path:
                pathI.append(str(k).split("'")[1])
            syn1.append(pathI)
    return syn1

def Lin(syn1,syn2):
    pass


input = inputText = [line.strip().split("-") for line in open("input.txt", "r").readlines()]
count = 0
for item in input:
    syns1 = wn.synsets(item[0])
    syns2 = wn.synsets(item[1])
    count += 1
    syn1 = ProcessSynsets(syns1)
    syn2 = ProcessSynsets(syns2)
    print(count)
    print(PathSimilarity(syn1,syn2))
    print(Wu_Palmer(syn1,syn2))
    print(Leacock_Chodorow(syn1,syn2))
    print()
