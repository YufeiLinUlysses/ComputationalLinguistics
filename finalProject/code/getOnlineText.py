from bs4 import BeautifulSoup
import requests
import re

class GOT:

    urlInput = ""
    getUrl = []

    def __init__(self, urlInput):
        self.urlInput = urlInput
        self.getUrl = [url for url in open(urlInput,"r").readlines()][0]

    def url_to_string(self):
            res = requests.get(self.getUrl)
            html = res.text
            soup = BeautifulSoup(html, 'html5lib')
            for script in soup(["script", "style", 'aside']):
                script.extract()
            return "  ".join(re.split(r'[\n\t]+', soup.get_text()))