import random
 
from tkinter.filedialog import test
from DNAToolKit import*
from files import*
import tkinter as tk
from tkinter import *
import os
from tkinter import *

ws = Tk()
ws.geometry('700x500')
ws.title('DNA TOOLKIT')
ws['bg']='#967bb6'

f = ("Times bold", 20)

def nextPage():
    ws.destroy()
    

Label(ws,text="THANK YOU FOR USING OUR TOOLKIT",padx=20,pady=20,bg='#967bb6',font=f).pack(expand=True, fill=BOTH)

Button(ws,text="EXIT",font=f,command=nextPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()

