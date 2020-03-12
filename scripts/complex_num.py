#!/usr/bin/python

from __future__ import division
import math

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real,self.imaginary + no.imaginary)
    def __sub__(self, no):
        return Complex(self.real - no.real,self.imaginary - no.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary , self.real*other.imaginary+self.imaginary*other.real)
    def __truediv__(self, no):
        return self.__mul__(Complex(no.real, -1*no.imaginary)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
    def mod(self):
        return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0)

    def __str__(self):
        result = "{0:.2f}{1:+.2f}i".format(self.real,self.imaginary)
        return result

if __name__ == '__main__':
    c = map(float, input().split()) #c=(2,1)
    d = map(float, input().split()) #c=(5,6)
    x = Complex(*c)
    y = Complex(*d)

    print("\n".join(map(str, [x+y, x-y,x*y,x/y,x.mod(),y.mod()])))

