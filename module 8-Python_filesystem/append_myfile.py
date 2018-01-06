# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:57:56 2018

@author: zeba
"""
#This will open the file in append mode.
f=open("files/myfile.txt","a")

#Using the write function to enter data into the file.
f.write(" hello python\t"*100)

#This will close the instance of the file myfile.txt stored
f.close()