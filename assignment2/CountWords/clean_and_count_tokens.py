import regex
import sys

file_name = sys.argv[1]
out_file_name = sys.argv[2]
ansDict = {}
ansText = "Number of Distinct Words in the Texts\n"

with open(file_name, 'r', encoding='UTF-8') as open_book:
    with open(out_file_name, 'w') as open_out_book:
        text = open_book.read()
        text = regex.sub(r'<(.*?)>', r' ', text)
        text = regex.sub(r'\n',r' ',text)
        text = text.lower()
        text = regex.sub(r'\'{2,}',r' ',text)
        text = regex.sub(r'\d',r' ',text)
        text = regex.sub(r'[^\w\'\s]|_+', r' ', text)
        countWord = text.split()
        for word in countWord:
            if word in ansDict:
                ansDict[word] += 1
            else:
                ansDict[word] = 1
        ansDict = dict(sorted(ansDict.items()))
        ansDict = dict(sorted(ansDict.items(), key=lambda x: x[1], reverse = True))
        for key, value in ansDict.items():
            ansText += key + ": " + str(value) + "\n"
        open_out_book.write(ansText)
