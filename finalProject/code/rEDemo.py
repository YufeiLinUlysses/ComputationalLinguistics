import namedEntityRecognition
import getOnlineText
import relationExtraction

urlInput = "./input/urlInput.txt"
out = "./out/REOut.txt"

got1 = getOnlineText.GOT(urlInput=urlInput)
text = got1.url_to_string()
ner = namedEntityRecognition.NER(text=text, out=None)
re1 = relationExtraction.RE(ner = ner, out = out)
re1.output()
