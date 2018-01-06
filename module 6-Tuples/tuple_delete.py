# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:38:37 2017

@author: zeba
"""

tup = ('physics', 'chemistry', 1997, 2000);

print(tup)
del tup
print ("After deleting tup : ")
print(tup)
'''This produces the following result. Note an exception raised, 
this is because after del tup tuple does not exist any more '''
