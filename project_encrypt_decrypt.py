# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:35:35 2017

@author: zeba
"""

loop=1
ch=0
key="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
enc_key="`~A1B!C2D@F3E#G4H$I5J%K6L^M7N&O8P*Q9RS0TU_V-W+X=Y|Z\/:(;'\"<>.,)"

a="*"
print(a*50) 
c="\tEncryption & Decryption"
print(c.expandtabs(15))
print(a*50)
str1=input("Enter String: ")
print(str1)
while(loop==1):
    print("your option are:")
    print("1. Perform Encryption")
    print("2. Perform Decryption")
    print("3. Exit")
    print(len(key))
    print(len(enc_key))
    ch=int(input("enter choice: "))
    if(ch==1):
        encrypted_table="".maketrans(key,enc_key)
        enc_text=str1.translate(encrypted_table)
        print("Encrypted Text: ")
        print(enc_text)
    elif(ch==2):
        decrypted_table="".maketrans(enc_key,key)
        dec_text=enc_text.translate(decrypted_table)
        print("Decrypted Text: ")
        print(dec_text)
    else:
        loop=0          
b="Thank You :)"
print(b.center(60,"*"))