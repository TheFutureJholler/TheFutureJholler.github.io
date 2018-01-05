# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:08:38 2018

@author: zeba
"""
loop=1
ch=0
ch1=0
a="*"
print(a*50) 
c="\tUnderstanding Exception in Python"
print(c.expandtabs(15))
print(a*50)
while(loop==1):
    print("your option are:")
    print("1. TRY...EXCEPT Block")
    print("2. TRY...EXCEPT...ELSE Block")
    print("3. TRY...FINALLY Block")
    print("4. Exit")
    ch=int(input("enter choice: "))
    if(ch==1):
        print("1) Without Exception\t2) With Exception")
        ch1=int(input("enter choice: ")) 
        if(ch1==1):
           values = [1,2,3]
           for x in values:
               print (x, values[x]) 
        else:
            values = [1,2,3,4]
            try:
                for x in values:
                    print (x, values[x])
            except IndexError as e:
                print ( "Exception:" )
                print ( e )
    elif(ch==2):
        print("1) Without ELSE\t2) With ELSE")
        ch1=int(input("enter choice: ")) 
        if(ch1==1):
            values = [1,2,3]
            x=5
            try:
                y = values[x]
            except:
                print("Exception occured!")
            else:
                print("Normal",y)
        else:
            values = [1,2,3]
            x=2
            try:
                y = values[x]
            except:
                print("Exception occured!")
            else:
                print("Normal",y)
    elif(ch==3):
        print("1) FINALLY with Exception\t2) FINALLY Without Exception")
        ch1=int(input("enter choice: ")) 
        if(ch1==1):
            values = [1,2,3]
            x=5
            try:
                y = values[x]
            except:
                print("Exception occured!")
            finally:
                print("All Done")
        else:
            values = [1,2,3]
            x=2
            try:
                y = values[x]
            except:
                print("Exception occured!")
            else:
                print("All Done")
    else:    
        loop=0          
b="Thank You :)"
print(b.center(60,"*"))