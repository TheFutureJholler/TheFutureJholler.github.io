# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:51:02 2018

@author: zeba
"""
import tkinter as tk
from tkinter import messagebox as msg

def openSecondWindow(username,password):
    root2=tk.Tk()
    root2.geometry("400x400")
    display_label=tk.Label(root2,text="Welcome "+username)
    display_label.grid(row=1,column=1)
    submit=tk.Button(root2,text="View Menu")
    submit.grid(row=2,column=1)
    
    submit=tk.Button(root2,text="Recharge Card")
    submit.grid(row=2,column=2)
    
    root2.mainloop()

def welcomeUser():
    username = username_entry.get()
    password = password_entry.get()
    if (username=="" or password==""):
        msg.showerror("error","missing something") #error -> window heading,missing in display box
    else:
        msg.showinfo("Greeting","Welcome "+username)
        root.destroy()
        openSecondWindow(username,password)

root=tk.Tk()
root.geometry("400x400")

username_label=tk.Label(root,text="User Name") #for username label
username_label.grid(row=1,column=1) # locating username label

username_entry=tk.Entry(root) #for username input
username_entry.grid(row=1,column=2) #locating username input

password_label=tk.Label(root,text="Password")
password_label.grid(row=2,column=1)
password_entry=tk.Entry(root,show="*") #show to hide password
password_entry.grid(row=2,column=2)

submit=tk.Button(root,text="Submit",command=welcomeUser)
submit.grid(row=3,column=2)
root.mainloop()