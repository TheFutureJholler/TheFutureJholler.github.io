#import tkinter as tk
#root=tk.Tk()
#root.mainloop()

#import tkinter as tk
#root=tk.Tk()
#b1=tk. Button(root)
#b1.grid(row=1,column=1)
#root.mainloop()

import tkinter as tk
from tkinter import messagebox as msg
def openSecondPanel(username,password):
    def secondPanel():
        print(name_entry.get())
    root2=tk.Tk()
    root2.geometry("400x400")
    name_label=tk.Label(root2,text="Name")
    name_label.grid(row=1,column=1)


    name_entry=tk.Entry(root2) 
    name_entry.grid(row=1,column=2)

    
    email_label=tk.Label(root2, text="Email")
    email_label.grid(row=2,column=1)

    email_entry=tk.Entry(root2) 
    email_entry.grid(row=2,column=2)

    contact_label=tk.Label(root2, text="Contact")
    contact_label.grid(row=3,column=1)

    contact_entry=tk.Entry(root2) 
    contact_entry.grid(row=3,column=2)
    submit=tk.Button(root2,text="Login",command=secondPanel)
    submit.grid(row=4,column=2)
    root2.mainloop()


def showSomeThing():
    
    
    
    username=username_entry.get()
    password=password_entry.get()
    if username=="" or password=="":
        msg.showerror("error","missing some thing")
    else:
        msg.showinfo("greeting","welcome"+username)
        root.destroy()
        openSecondPanel(username,password)
    
root=tk.Tk()
root.geometry("400x400")
username_label=tk.Label(root,text="UserName")
username_label.grid(row=1,column=1)
username_entry=tk.Entry(root)
username_entry.grid(row=1,column=2)

password_label=tk.Label(root,text="Password")
password_label.grid(row=2,column=1)
password_entry=tk.Entry(root,show="*")
password_entry.grid(row=2,column=2)

submit=tk.Button(root,text="Submit",command=showSomeThing)
submit.grid(row=3,column=2)
root.mainloop()

