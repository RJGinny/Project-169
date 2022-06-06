#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:45:03 2022

@author: riddhiekajain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:09:44 2022

@author: riddhiekajain
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("Classes")

GUI_element=["Label", "Button", "Dropdown"]
dropdown=ttk.Combobox(root, state="readonly", values=GUI_element)
dropdown.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label = Label(root, text = "A new label has been created using class", fg="red")
        label.pack()
        
    def createButton(self):
        btn = Button(root, text =" Button", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def createDropdown(self):
        value=[1, 2, 3, 4]
        class_dropdown=ttk.Combobox(root, state="readonly", values=value)
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        element=dropdown.get()
        if(element=="Label"):
            self.createLabel()
        elif(element=="Button"):
            self.createButton()
        elif(element=="Dropdown"):
            self.createDropdown()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text =" create element", command= obj_of_CreateElements.choose)

btn.pack(padx=20, pady= 10)

root.mainloop()