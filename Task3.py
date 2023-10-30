import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt


def screen():
    root = Toplevel()
    root.title("Quantization")
    root.geometry('300x200')

    function = IntVar(value= 0)

    tkinter.Label(root, text="Choose the input type: \nNumber of ").pack()

    Radiobutton(root, text="Bits", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)
    Radiobutton(root, text="Levels", variable=function, value=2, command=lambda: function.get()).pack(padx=5, pady=5)

    num = tkinter.Entry(root)
    num.pack(padx=5, pady=5)

    Button(root, text='Calculate', command=lambda: quan(function.get(), num.get())).pack(padx=10, pady=10)


def quan(op, num):
    if validation(op,num):
        msgbx.showinfo(message="Great")
    return

def validation(op,x):
    msg = ""
    try:
        op = int(op)
        if op == 0:
            raise ValueError
    except:
        msg +="You Must choose the input type \n"

    try:
        x = int(x)
        if x == 0 or x == NONE:
            raise ValueError
    except:
        msg += "The input Must be an Integer value and not 0"

    if msg != "" :
        msgbx.showerror(title="Error", message=msg,)
    else:
        return True