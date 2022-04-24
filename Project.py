import random
from DNAToolKit import*
from files import*
import tkinter as tk
from tkinter import *
import os
from tkinter import *

ws = Tk()
ws.geometry('700x500')
ws.title('DNA TOOLKIT')
ws['bg']='#E6E6FA'

f = ("Times bold", 20)

def nextPage():
    ws.destroy()
    import Page_2

def prevPage():
    ws.destroy()
    import Page_3    

    
Label(ws,text="Welcome to your neighborhood friendly Toolkit\n     \nYour wide gateway to dealing with \n    \n DNA , RNA & PROTIEN ",padx=20,pady=20,bg='#967bb6',font=f).pack(expand=True, fill=BOTH)

Button(ws, text="Previous Page", font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

Button(ws,text="Next Page",font=f,command=nextPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()




