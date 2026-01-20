'''
Module: a file containing code you want to include in your program
        use 'imoport' to include a module (built-in or your own)
        useful to break up a large program reusable seprate files.

'''

import math
print(math.e ** 2)

import math as m
print(m.e ** 2)

from math import e
print(e ** 2)

import example

result = example.pi
print(result)
sqr = example.sqaure(2)
print(sqr)