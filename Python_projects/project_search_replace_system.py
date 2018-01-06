# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:04:45 2017

@author: zeba
"""
a="*"
print(a*50) 
c="\tWelcome to Search & Replace System"
print(c.expandtabs(15))
print(a*50)
loop=1
para=""
recent_search=[]
recent_replace=[]
para=input("enter para: ")
while(True):
    print("1.Search/n2.Replace/n3.Recent Search/n4.Recent Replace/n5.Exit")
    choice=int(input("Enter choice: "))
    if(choice==1):
        search_word=input("Enter search word: ")
        index=para.find(search_word)
        print("your word "+search_word+" is present at "+str(index))
        recent_search.append(search_word)
    elif(choice==2):
        old_word=input("Enter existing word to be replaced: ")
        new_word=input("Enter new word to be replaced: ")
        para=para.replace(old_word,new_word)
        print("Your new para: ", para)
        recent_replace.append(old_word)
    elif(choice==3):
        print(recent_search[::-1])
    elif(choice==4):
        print(recent_replace[::-1])
    else:
        b="Thank You :)"
        print(b.center(60,"*"))
        break
