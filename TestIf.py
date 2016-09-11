import six.moves.cPickle as pickle
import gzip
import os
import sys
import timeit
from compiler.symbols import Scope

var = 1
c=0
d=0
if var==0:
    c=1
    d=2
e=3

print(c)
print(d)
print(e)

"""
Testing result:
0
0
3
which means that the it is the structure of the code controlling the "if" scope,
which I think also applies for other scopes, like for, while...
"""

