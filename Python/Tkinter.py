# *    Copyright (c) 2022, <Prakash Gatiyala>
# *    All rights reserved
# This is a Python program using the Tkinter library which includes GUI.
# Replit link: https://replit.com/@PrakashGatiyala/Tkinter?v=1

from tkinter import * 
var = Tk()
name = Label(var,text = "Name", fg = "green")
name.grid(row = 0, column = 0) 
entry1 = Entry(var).grid(row = 0, column = 1)  

password = Label(var,text = "Password", fg = "blue").grid(row = 1, column = 0) 
entry2 = Entry(var).grid(row = 1, column = 1)  

submit = Button(var, text = "Submit", fg = "black").grid(row = 4, 
column=0)  

var.geometry('400x250')
var.mainloop() 