# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:48:49 2017

@author: zeba
"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

'''This produces the following result. 
Note that an exception is raised because after del dict dictionary does not exist any more − '''