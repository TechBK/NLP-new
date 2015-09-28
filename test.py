__author__ = 'techbk'

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

#x.update(y)
z = {k: x.get(k,0) + y.get(k,0) for k in x.keys() | y.keys()}

##x[k] = x.get(k, 0)  + v

for k, v in y.items():
    x[k] = x.get(k, 0) + v

print(x)
print(z)