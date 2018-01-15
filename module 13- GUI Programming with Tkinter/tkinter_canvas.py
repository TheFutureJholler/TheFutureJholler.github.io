
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:57:26 2018

@author: zeba
"""
"""
The Canvas is a rectangular area intended for drawing pictures or other complex layouts. 
You can place graphics, text, widgets, or frames on a Canvas.  
arc . Creates an arc item.


"""

#import tkinter as tk
#root=tk.Tk()
#
#c = tk.Canvas(root,bg="blue",width=500, height=500)#to draw canvas 
##to draw something on canvas
#coord = 10, 50, 240, 210 
#arc = c.create_arc(coord, start=0, extent=150, fill="red")
#
#c.grid()#to place canvas
#root.mainloop()

#########################################################################

import tkinter as tk
root=tk.Tk()

c = tk.Canvas(root,bg="blue",width=500, height=500)#to draw canvas 
#to draw something on canvas
#filename = PhotoImage(file="sunshine.gif")
line = c.create_line(20,20,250,250, fill="red")
oval=c.create_oval(50,50,20,20)
polygon=c.create_polygon(150,250,210,310,250,250)
c.grid()#to place canvas
root.mainloop()

#######################################################################
