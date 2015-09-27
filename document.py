__author__ = 'techbk'
import re
from bagofword import BagOfWords

class Document(object):

    def __init__(self):
        self._words_and_freq = BagOfWords()
        #self._vocabulary = BagOfWords()

    def read_document(self,filename):

        try:
            text = open(filename,"r", encoding='utf-8').read()
        except UnicodeDecodeError:
            text = open(filename,"r", encoding='latin-1').read()
        text = text.lower()
        words = re.split("[^\wäöüÄÖÜß]*",text) # what re module?

        #self._number_of_words = 0
        #take word into bag

        for word in words:
            if word != '':
                self._words_and_freq.add_word(word)

    def __str__(self):
        return str(self._words_and_freq)

    def wordAndFreq(self):
        return  self._words_and_freq.bagofwords()

if __name__ == "__main__":
    d = Document()
    d.read_document("learn/clinton/clinton5.txt")
    print(d)