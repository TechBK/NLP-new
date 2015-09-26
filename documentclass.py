__author__ = 'techbk'

from document import Document

class DocumentClass(Document):

    def _init__(self):
        Document.__init__(self)
        self._number_of_docs = 0

    def __add__(self, other):

        res = DocumentClass()
        res._words_and_freq = self._words_and_freq + other._words_and_freq
        return res

    def numberOfDocs(self):
        return self._number_of_docs

    def setNumberOfDocs(self, number):
        self._number_of_docs = number


