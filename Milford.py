import numpy as numpy

class Milford:
    r=0
    g=0
    b=0
    h=0
    s=0
    v=0

    def neural(self, r ,g ,b ,h ,s ,v):
            print(r," ",g," ",b," ",h," ",s," ",v)
            

    def __init__(self, r,g,b,h,s,v):
        self.r = r
        self.g = g
        self.b = b
        self.h = h
        self.s = s
        self.v = v
        self.neural(r,g,b,h,s,v)
    