# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:57:38 2017

@author: zeba
"""
a="*"
print(a*50) 
c="\twelcome to lottery system"
print(c.expandtabs(15))
print(a*50)
import random
loop=1
choice=0
while loop==1:
    nm=input("enter name: ")
    age=int(input("enter age: "))
    if(age<=17):
        print("sorry can not proceed")
    else:
        x=int(input("press 1 to generate ticket"))
        if(x==1):
            print("ticket generated successfully")
            t_no=random.randrange(1,200000)
            print("Ticket no:"+str(t_no))
        else:
            break
        y=int(input("press 1 to get win amount: "))
        if(y==1):
            if(1<=t_no<=100):
                print("win amount: 1 cr")
            elif(101<=t_no<=500):
                print("win amount: 50 lac")
            elif(501<=t_no<=10000):
                print("win amount: 1 lac")
            elif(10001<=t_no<=100000):
                print("win amount: 10000")
            elif(100000<=t_no<=200000):
                print("win amount: 100")
            else:
                ("win amount: 5")
    c1=input("Do you wish to continue? [Y/N] ")
    if ( c1 is "y"):
        loop=1
    else:
        loop=0
        b="Thank You :)"
        print(b.center(60,"*"))