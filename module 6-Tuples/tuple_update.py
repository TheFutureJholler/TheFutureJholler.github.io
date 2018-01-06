# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:42:47 2017

@author: zeba
"""

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples because tuple in immutable.so after update we need to store the result in new variable
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)