# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:22:23 2017

@author: iram
"""
loop=1
ch=0
while(loop==1):
    a="Understanding String"
    print(a.center(60,"*"))
    
    print("\nyour option are:")
    print("1. Toggle Case String\n2. Split and Join String\n3. Reverse String\n4. Repeat String")
    print("5. Update String \n6. Count Words or Character\n7. Find() \n8. Index()\n9. isalnum()")
    print("10. isalpha\n11. isdigit()\n12. Exit")
    ch=int(input("Enter Choice: "))
    if(ch==1):
        def swap_case(str):
            return str.swapcase()
        str = input("Enter a String: ")
        result = swap_case(str)
        print(result)
    elif(ch==2):
        def split_and_join(line):
            line = line.split(" ")
            #print(line)
            line = "-".join(line)
            return line
        line = input("Enter a line: ")
        result = split_and_join(line)
        print(result)
    elif(ch==3):
        str1 = input("Enter a String: ")
        print("Reverse Output: ")
        print(str1[::-1])
        print("Printing even characters: ")
        print(str1[::2])
    elif(ch==4):
        c=input("Enter a String: ")
        print(c*10)
    elif(ch==5): 
        d="Hello Good Morning"
        print(d)
        #d=input("Enter a String: ")
        d=d[0:6]+"python! "+d[6:]
        print(d)
    elif(ch==6):
        str2=input("Enter String: ")
        str3=input("Enter words or character to be counted: ")
        print(str2.count(str3))
    elif(ch==7): 
        print("find() returns the starting index of the input word and return -1 if word not present")
        str4=input("Enter String: ")
        str5=input("Enter word to be found: ")
        print(str4.find(str5))
    elif(ch==8): 
        print("index() returns the starting index of the input word and return error if word not present")
        str4=input("Enter String: ")
        str5=input("Enter word to be found: ")
        print(str4.index(str5))
    elif(ch==9):
        print("isalnum() give true for alpha-numeric and false for special char")
        w="hello"
        print(w)
        print(w.isalnum())
        x="hello123"
        print(x)
        print(x.isalnum())
        y="1234"
        print(y)
        print(y.isalnum())
        z="abc@gamil.com"
        print(z)
        print(z.isalnum())
    elif(ch==10):
        print("isalpha() give true for alpha and false for numeric and special char")
        w="hello"
        print(w)
        print(w.isalpha())
        x="hello123"
        print(x)
        print(x.isalpha())
        y="1234"
        print(y)
        print(y.isalpha())
        z="abc@gamil.com"
        print(z)
        print(z.isalpha())
    elif(ch==11):
        print("isdigit() give true for numeric and false for alpha and special char")
        w="hello"
        print(w)
        print(w.isdigit())
        x="hello123"
        print(x)
        print(x.isdigit())
        y="1234"
        print(y)
        print(y.isdigit())
        z="abc@gamil.com"
        print(z)
        print(z.isdigit())
    else:
        loop=0        
b="Thank You :)"
print(b.center(60,"*"))
        
