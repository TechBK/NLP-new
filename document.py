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
        #words = re.split("[^\w]*",text)
        self._number_of_words = 0
        #take word into bag
        for word in words:
            self._words_and_freq.add_word(word)



    def wordAndFreq(self):
        return  self._words_and_freq.bagofwords()