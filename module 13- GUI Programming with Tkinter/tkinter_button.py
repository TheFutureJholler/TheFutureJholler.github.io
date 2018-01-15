# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:49:40 2018

@author: zeba
"""
"""
The Button widget is used to add buttons in a Python application. 
These buttons can display text or images that convey the purpose of the buttons. 
You can attach a function or a method to a button, which is called automatically when you click the button. 

Syntax: w = Button ( master, option=value, ... )

Parameters: 
    master: This represents the parent window.
    options: There are many options for this widget. These options can be used as key-value pairs separated by commas
"""
import tkinter as  tk
from tkinter import messagebox as msg
root = tk.Tk()
def hello():
    msg.showinfo("Hello", "Hello World")
    root.destroy()
B1 = tk.Button(root, text = "Hello", command = hello)
label = tk.Label(root,text="Hello World!")
B1.pack()
label.pack()
root.mainloop()