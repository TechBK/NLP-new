__author__ = 'techbk'

from document import Document


class DocumentClass(Document):
    def __init__(self):
        Document.__init__(self)
        self.__number_of_docs = 0

    def __add__(self, other):
        doc_class = DocumentClass()

        doc_class._bag_of_words = {k: self._bag_of_words.get(k, 0) + other._bag_of_words.get(k, 0)
                                    for k in self._bag_of_words.keys() | other._bag_of_words.keys()}
        doc_class.__number_of_words = self._number_of_words + self._number_of_words
        # doc_class.__number_of_docs = self.__number_of_docs + self.__number_of_docs

        return doc_class

    def numberOfDocs(self):
        return self.__number_of_docs

    def setNumberOfDocs(self, number):
        self.__number_of_docs = number


if __name__ == "__main__":
    d = DocumentClass()
    d.read_document("learn/clinton/clinton5.txt")
    print(d)
    print(type(d))
    f = DocumentClass()
    f.read_document("learn/clinton/clinton5.txt")
    print(f)
    print(type(f))
    x = d + f
    print(type(x))

    print(x)
