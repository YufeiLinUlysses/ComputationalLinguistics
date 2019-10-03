from bs4 import BeautifulSoup
import requests
import re
import nltk

class NER: 
    text = ""
    out = ""

    def __init__(self, text = None, out = None):
        self.text = text
        if out == None:
            out = ""
        else:
            self.out = out 

    def orderDict(self, dictionary):
        dictionary = dict(sorted(dictionary.items()))
        dictionary = dict(
            sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        return dictionary

    def isEntity(self,word):
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]*$", word):
                return True
        elif re.match(r"^[A-Z]+$", word):
            return True
        elif re.match(r"^[A-Z][a-z]+$", word):
            return True
        elif re.match(r"^([A-Z]\.){1,}$", word):
            return True
        elif re.match(r"^[a-zA-Z0-9]+\-[a-zA-Z0-9]+$", word):
            return True
        elif re.match(r"^[a-z]+\d+$", word):
            return True
        else:
            return False

    def toSent(self):
        finText = nltk.sent_tokenize(self.text)
        result = []
        for item in finText:
            clean = re.sub(r"[,;@#?!&$]+\ *", " ", item)
            check = clean.split(" ")[0]
            if self.isEntity(check):
                result.append(clean)
            else:
                try:
                    result[-1] += " " + clean
                except:
                    result.append(clean)           
        return result
    
    def tagWords(self, sent):
        result = []
        tag = []
        mark = 0
        processed = [word for word in sent.split()]
        for word in processed:
            if self.isEntity(word):
                ans = ("I", "B")[mark == 0]
                tag.append(ans)
                mark += 1
            else:
                tag.append("O")
                mark = 0
        result = [processed,tag]
        return result 

    def getEntity(self, taggedSent):
        result = {}
        entity = []
        for i in range(len(taggedSent[0])):
            if taggedSent[1][i] == "B":
                entity.append(taggedSent[0][i])
            elif taggedSent[1][i] == "I":
                entity[-1] += " " + taggedSent[0][i]
            else:
                continue
        for item in entity:
            if item in result:
                continue
            else:
                result[item] = entity.count(item)
        return result

    def totalCount(self):
        result = {}
        processed = self.toSent()
        for item in processed:
            tagged = self.tagWords(item)
            ans = self.getEntity(tagged)
            for key, value in ans.items():
                if key in result:
                    result[key] += value
                else:
                    result[key] = value
        return result

    def outPut(self):
        ansStr = []
        totalCount = self.totalCount()
        finish = self.orderDict(totalCount)
        for key,value in finish.items():
            ansStr.append(key + ": " + str(value))
        try: 
            with open(self.out, 'w') as file:
                file.write("\n".join(ansStr))
        except:
            print("Sorry you did not provide a output location.")