#Implementation of the NER class
import namedEntityRecognition
import getOnlineText
urlInput = "./input/urlInput.txt"
out = "./out/NEROut.txt"

got1 = getOnlineText.GOT(urlInput=urlInput)
text = got1.url_to_string()
print(text)
ner1 = namedEntityRecognition.NER(text = text, out = out)
ner1.outPut()