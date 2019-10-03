import nltk
import regex

rawText = nltk.corpus.gutenberg.raw("chesterton-ball.txt")
words = nltk.corpus.gutenberg.words("chesterton-ball.txt")
inputText = [line.strip() for line in open("in.txt", "r").readlines()]
inputText1 = [line.strip() for line in open("in1.txt", "r").readlines()]

def getWordCount(text):
    ansDict = {}
    text = regex.sub(r'<(.*?)>', r' ', text)
    text = regex.sub(r'\n', r' ', text)
    text = text.lower()
    text = regex.sub(r'\'{2,}', r' ', text)
    text = regex.sub(r'\d', r' ', text)
    text = regex.sub(r'[^\w\'\s]|_+', r' ', text)
    countWord = text.split()
    for word in countWord:
        if word in ansDict:
            ansDict[word] += 1
        else:
            ansDict[word] = 1
    return ansDict

def bigramCounting(words):
    bigram = nltk.bigrams(words)
    bigramCount = {}
    for item in bigram:
        word1 = item[0].lower()
        word2 = item[1].lower()
        if word1 in bigramCount:
            if word2 in bigramCount[word1]:
                bigramCount[word1][word2] += 1
            else: 
                bigramCount[word1][word2] = 1
        else:
            bigramCount[word1] = {}
            bigramCount[word1][word2] = 1
    return bigramCount

def getListOfStrings(wordList):
    liStr = []
    for i in range(len(wordList)-1):
        wordTuple = (wordList[i],wordList[i+1])
        liStr.append(wordTuple)
    return liStr

def getProb(inputText):
    wordList = inputText.split()
    listOfStr = getListOfStrings(wordList)
    prob = 1
    for item in listOfStr:
        try:
            thisProb = countingBigram[item[0]][item[1]]/wordCount[item[0]]
            prob *= thisProb
        except:
            prob *= 0
    return prob

def sortDictByValue(diction):
    diction = dict(sorted(diction.items(), key=lambda x: x[1], reverse=True))
    return diction

wordCount = getWordCount(rawText)
countingBigram = bigramCounting(words)
ans = {}
ans2 = {}
ansText = ""
ansText2 = ""

for item in inputText:
    ans[item.strip()] = getProb(item.strip())
for key, value in ans.items():
    ansText += key + ": " + str(value) + "\n"
open("out.txt","w").write(ansText)

countB = {}
for item in inputText1:
    ansArray = []
    temp = sortDictByValue(countingBigram[item])
    largest = temp[next(iter(countingBigram[item]))]
    countB[item] = largest
    for thing in temp:
        if temp[thing] == largest:
            ansArray.append(thing)
    ans2[item] = ansArray
for key, value in ans2.items():
    part = ""
    for item in value:
        part += item + " "
    ansText2 += key + ": " +"total is: "+str(len(ans2[key])) + " "+ part + "\n" + \
        "total bigram: " + str(countB[key]) + "\n" + "\n"
open("out2.txt","w").write(ansText2)
