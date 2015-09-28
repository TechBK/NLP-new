import re


__author__ = 'techbk'


class Document(object):

    def __init__(self):
        self._number_of_words = 0  # tong so tu trong 1 bag
        self._bag_of_words = {}

    #def __add__(self, other):
        #""" Overloading of the "+" operator to join two BagOfWords """
        #erg = Document()
        #erg._bag_of_words = {k: self._bag_of_words.get(k, 0) + other._bag_of_words.get(k, 0)
        #                      for k in self._bag_of_words.keys() | other._bag_of_words.keys()}
        #erg.__number_of_words = self.__number_of_words + self.__number_of_words
        #
        #return erg

    def read_document(self, filename):

        try:
            text = open(filename, "r", encoding='utf-8').read()
        except UnicodeDecodeError:
            text = open(filename, "r", encoding='latin-1').read()
        text = text.lower()
        words = re.split("[^\wäöüÄÖÜß]*", text)  # what re module?

        # self._number_of_words = 0
        # take word into bag

        for word in words:
            if word != '':
                # self._words_and_freq.add_word(word)
                self.add_word(word)

    def add_word(self, word):
        """ A word is added in the dictionary __bag_of_words"""
        self._number_of_words += 1
        if word in self._bag_of_words:
            self._bag_of_words[word] += 1
        else:
            self._bag_of_words[word] = 1

    #def numberOfWordInBag(self):
        #""" Returning Number Of Word In Bag"""
        #return self._number_of_words

    def len(self):
        """ Returning len of bag of word. It mean number of defirent words"""

        return len(self._bag_of_words)

    def __str__(self):

        return "Number: " + str(self._number_of_words) + "\nBag:" + str(self._bag_of_words)

if __name__ == "__main__":
    d = Document()
    d.read_document("learn/clinton/clinton5.txt")
    print(d)
    print(type(d))
    f = Document()
    f.read_document("learn/clinton/clinton4.txt")
    print(f)
    print(type(f))

    #print(d + f)
