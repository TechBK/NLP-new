__author__ = 'techbk'
import os

from documentclass import DocumentClass
from document import Document
from math import log

class Pool():
    def __init__(self):
        self.__document_classes = {}
        self.__number_of_doc = 0

    def learn(self,directory,classname):
        x = DocumentClass()
        dir = os.listdir(directory)

        for file in dir:
            d = Document()
            print(directory + "/" + file)
            d.read_document(directory + "/" +  file)

            x = x + d
        self.__document_classes[classname] = x
        numberfile = len(dir)
        x.setNumberOfDocs(numberfile)

        print(x)
        self.__number_of_doc += numberfile

    def document_classes(self):
        return self.__document_classes



    def probability(self,document,dclass = ""):
        if dclass:
            d = Document()
            d.read_document(document)

            doc_class = self.__document_classes[dclass]

            Nc = doc_class.numberOfDocs()

            LogPc = log(Nc / self.__number_of_doc)

            sumLogPTkC = 0
            for word in d._bag_of_words.keys():
                if word in doc_class._bag_of_words:
                    TctK = doc_class._bag_of_words[word]
                else:
                    TctK = 0
                P_TkC= (TctK+1)/(doc_class._number_of_words + doc_class.len())

                sumLogPTkC += log(P_TkC)
            LogPc += sumLogPTkC
            return sumLogPTkC
        else:
            prob_list = []
            for dclass in self.__document_classes:
                prob = self.probability(document, dclass)
                prob_list.append([dclass,prob])
            prob_list.sort(key = lambda x: x[1], reverse = True)
            return prob_list



if __name__ == "__main__":
    DClasses = ["clinton",  "lawyer",  "math",  "medical",  "music",  "sex"]

    base = "learn/"
    p = Pool()
    for classname in DClasses:
        p.learn(base + classname, classname)



    def test():
        doc_class = p.document_classes()

        #for classname in DClasses:
        classname = "sex"
        documentclass = doc_class[classname]
        numdoc = documentclass.numberOfDocs()
        print("***************")
        print(classname)
        print("Number Of Docs", numdoc)
        print("***************")
        bag = documentclass.wordAndFreq()
        print(bag)
        #for key,value in bag.items():
           #print(key,' : ',value)

    test()