import sys

inFile = sys.argv[1]
outFile = sys.argv[2]
jpDict = []
finalArray = []

inFileRead = [line.strip() for line in open(inFile, "r", encoding="UTF-8").readlines()]

dictFile = "./japanese_wordlist.txt"
dictionary = open(dictFile,"r", encoding = "UTF-8")
jpDict=[line.strip() for line in dictionary.readlines()]

def maxMatch(text,dictionary):
    lineAns = ""
    end = len(text)
    while len(text)>0:
        word = text[0:end]
        if word in dictionary or end == 1:
            lineAns += word + " "
            text = text[end:]
            end = len(text)
        else:
            end = end - 1
    return lineAns

ansText = ""
for line in inFileRead:
    lineAns = maxMatch(line, jpDict)
    ansText += lineAns + "\n"

with open(outFile,"w") as result: 
    result.write(ansText)
