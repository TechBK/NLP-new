
__author__ = 'techbk'

class A(int):
    def __init__(self,a):
        int.__init__(self)
        self.a = a

    def __add__(self,other):

        x = A( super(A,self).__add__(other))
        x.a =1
        return x

x = A(1)
print(x, x.a)
y = A(2)

#print(x)

z = x + y
print(z)
print(z)