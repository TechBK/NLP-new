__author__ = 'techbk'

class BagOfWords(object):

    def __init__(self):
        self.__number_of_words = 0 #tong so tu trong 1 bag
        self.__bag_of_words = {}
        
    def __add__(self,other):
        """ Overloading of the "+" operator to join two BagOfWords """
        erg = BagOfWords()
        sum = erg.__bag_of_words
        for key in self.__bag_of_words:
            sum[key] = self.__bag_of_words[key]
            if key in other.__bag_of_words:
                sum[key] += other.__bag_of_words[key]
        for key in other.__bag_of_words:
            if key not in sum:
                sum[key] = other.__bag_of_words[key]
        return erg

    def add_word(self,word):
        """ A word is added in the dictionary __bag_of_words"""
        self.__number_of_words += 1
        if word in self.__bag_of_words:
            self.__bag_of_words[word] += 1
        else:
            self.__bag_of_words[word] = 1

    def bagofwords(self):
        """ Returning the dictionary, containing the words (keys) with their frequency (values)"""
        return self.__bag_of_words
