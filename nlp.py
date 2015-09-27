__author__ = 'techbk'
import  os
from pool import Pool


DClasses = ["clinton",  "lawyer",  "math",  "medical",  "music",  "sex"]

base = "learn/"
p = Pool()
for classname in DClasses:
    p.learn(base + classname, classname)



base = "test/"
for classname in DClasses:
    dir = os.listdir(base + classname)
    for file in dir:
        res = p.probability(base + classname + "/" + file)
        print(classname + ": " + file + ": " + str(res))
