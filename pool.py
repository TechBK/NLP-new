__author__ = 'techbk'
import os

from documentclass import DocumentClass
from document import Document

class Pool():
    def __init__(self):
        self.__document_classes = {}

    def learn(self,directory,classname):
        x = DocumentClass()
        dir = os.listdir(directory)

        for file in dir:
            d = Document()
            print(directory + "/" + file)
            d.read_document(directory + "/" +  file)
            x = x + d
        self.__document_classes[classname] = x
        print(len(dir))
        x.setNumberOfDocs(len(dir))

    def document_classes(self):
        return self.__document_classes




if __name__ == "__main__":
    DClasses = ["clinton",  "lawyer",  "math",  "medical",  "music",  "sex"]

    base = "learn/"
    p = Pool()
    for classname in DClasses:
        p.learn(base + classname, classname)




    doc_class = p.document_classes()
    #print(doc_class)
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