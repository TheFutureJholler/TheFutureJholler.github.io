# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:33:14 2017

@author: zeba
"""
a="*"
print(a*70)
wel="\tWelcome to XYZ Restaurant"
print(wel.expandtabs(20))
print(a*70)
loop=1
count=1
tot=0
tot1=0

while( loop == 1 ):
    per=int(input("enter no of persons:"))
    while(count<=per):
        print("Enter Starter for Person"+str(count)+":")
        s=int(input(": "))
        print("enter meal for person",count)
        m=int(input(": "))
        print("enter dessert for person",count)
        d=int(input(": ")) 
        tot=s+m+d
        print("total bill person "+str(count)+"is :"+str(tot))
        count=count+1
        tot1+=tot
        
    print("do you have coupon code?(Y/N)")
    c=input(":")

    if ( c is "y"):
        print("enter amount of coupon: ")
        amt=int(input(":"))
    else:
        print("no coupon code")
        amt=0
        loop=0
    tot1=tot1-amt
    print("total bill: "+ str(tot1))
    print("do you wish to continue?(Y/N)")
    c1=input(":")
    if ( c1 is "y"):
        loop=1
    else:
        loop=0
        b="Thank You :)"
        print(b.center(60,"*"))

    
    