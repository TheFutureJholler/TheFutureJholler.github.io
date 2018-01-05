# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:42:35 2018

@author: zeba
"""

#create a .text files (myfile.txt) by using the code
f= open("files/myfile.txt","w+")

#Using the write function to enter data into the file.
f.write("hello world\t"*100)

#This will close the instance of the file myfile.txt stored
f.close()
