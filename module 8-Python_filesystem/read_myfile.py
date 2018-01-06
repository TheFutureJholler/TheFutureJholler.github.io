# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:17:32 2018

@author: zeba
"""
#Open the file in Read mode
f=open("files/myfile.txt", "r")

#We use the mode function in the code to check that the file is in open mode. If yes, we proceed ahead
if f.mode == 'r':
    contents =f.read() #Use f.read to read file data and store it in variable content
    print(contents)