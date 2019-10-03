import namedEntityRecognition
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import getOnlineText
import re

class RE:
    text = ""
    out = ""
    ner = namedEntityRecognition.NER(text = "", out = None) 
    ps = PorterStemmer()
    
    def __init__(self, ner, out = None):
        self.ner = ner
        self.text = ner.text
        if out != None:
            self.out = out
        else:
            self.out = ""
        
    def orderDict(self, dictionary):
        dictionary = dict(sorted(dictionary.items()))
        dictionary = dict(
            sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        return dictionary

    def sortResult(self,result):
        sortedResult = {}
        for key, value in result.items():
            sortedResult[key] = len(value)
        sortedResult = self.orderDict(sortedResult)
        for key, value in sortedResult.items():
            sortedResult[key] = result[key]
        return sortedResult
        
    def tagSentence(self, text):
        final = []
        verb = ""
        result = {}
        tagged = self.ner.tagWords(text)
        ans = self.ner.getEntity(tagged)
        if len(ans) == 1:
            return []
        first = next(iter(ans))
        last = ans.popitem()[0]
        text = text.replace(first, " ")
        text = text.replace(last, " ")
        processed = [word for word in text.split()]
        for item in processed:
            token = nltk.word_tokenize(item)
            posTag = nltk.pos_tag(token)
            result[posTag[0][0]] = posTag[0][1]
        for key,value in result.items():
            if "VB" in value:
                verb = self.ps.stem(key)
            else:
                continue
        final = [first, verb, last]
        return final

    def getRelations(self):
        result = {}
        finText = self.ner.toSent()
        for sent in finText:
            final = self.tagSentence(sent)
            if final != [] and final[1] != "":
                verb = final[1]
                if verb in result:
                    result[verb].append(final)
                else:
                    result[verb] = [final]
            else:
                continue
        return result
    
    def output(self):
        ansStr = []
        result = self.getRelations()
        final = self.sortResult(result)
        for key in final:
            for item in final[key]:
                ansStr.append(item[0] + ": " + item[1] + " --> " + item[2])
        try:
            with open(self.out, 'w') as file:
                file.write("\n".join(ansStr))
        except:
            print("Sorry you did not provide a output location.")