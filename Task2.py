from tkinter import messagebox
from ImpFunctions import *
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

index_signal1=[]
sample_signal1=[]
index_signal2=[]
sample_signal2=[]
op = ""
def set_op(x):
    op = x
    if op=="Addition" or op=="Subtraction":
        add_sub(op)
    elif op == "Multiplication" or op == "Shifting":
        mul_shift(op)
    elif op == "Squaring" or op == "Accumulation":
        sqr_acc(op)
    elif op == "Normalization":
        norm(op)
    else:
        messagebox.showinfo("","Select an Operation please")


def set_lists():
    index_signal1,sample_signal1=open_file()
    print(len(sample_signal1))
    return

def list_size():
    print(len(sample_signal1))


def add_sub(op):
    root = Toplevel()
    root.title(op)
    root.geometry('250x150')

    btn = Button(root, text='Open Signal 1', command=lambda: set_lists())
    btn.pack(side=TOP, padx=10, pady=10)


    btn2 = Button(root, text='Open Signal 2', command=lambda: set_lists())
    btn2.pack(side=TOP, padx=20, pady=20)

    return
def mul_shift(op):
    root = Tk()
    root.title(op)
    root.geometry('300x100')

    label = tkinter.Label(root, text="Constant Value")
    label.pack(padx=5, pady=5)

    input = tkinter.Entry(root)
    input.pack(padx=5, pady=5)

    Button(root, text='Draw',).pack(padx=5, pady=5)

def sqr_acc(op):
    root = Tk()
    root.title(op)
    root.geometry('300x100')

    Button(root, text='Open Signal').pack(side=TOP, padx=10, pady=10)

    Button(root, text='Draw',).pack(padx=5, pady=5)

def norm(op):
    root = Tk()
    root.title(op)
    root.geometry('300x200')
    choice = IntVar()

    Button(root, text='Open Signal').pack(side=TOP, padx=10, pady=10)

    label = tkinter.Label(root, text="Choose range: ")
    label.pack()

    Radiobutton(root, text="-1 to 1", variable=choice, value=1, command=lambda: choice.get()).pack(padx=5, pady=5)
    Radiobutton(root, text="0 to 1", variable=choice, value=2, command=lambda: choice.get()).pack(padx=5, pady=5)

    Button(root, text='Draw',).pack(padx=5, pady=5)

