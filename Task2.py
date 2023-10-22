from tkinter import messagebox
from ImpFunctions import *
import tkinter
from tkinter import *
from tkinter.ttk import *
from itertools import zip_longest
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

index_signal1=[]
sample_signal1=[]

index_signal2=[]
sample_signal2=[]

index_result=[]
sample_result=[]
op = ""
def set_op(x):
    op = x
    if op=="Addition" or op=="Subtraction":
        add_sub(op)
        # print("Set Op fun Signal1 : ",len(sample_signal1))
        # print("Set Op fun Signal2 : ",len(sample_signal2))
    elif op == "Multiplication" or op == "Shifting":
        mul_shift(op)
    elif op == "Squaring" or op == "Accumulation":
        sqr_acc(op)
    elif op == "Normalization":
        norm(op)
    else:
        messagebox.showinfo("","Select an Operation please")


def set_signal1():
    index_signal1[:],sample_signal1[:]=open_file()
    # print("Set Signal1: ",len(sample_signal1))
    return
def set_signal2(op):
    index_signal2[:],sample_signal2[:]=open_file()
    # print("Set Signal2: ",len(sample_signal2))
    if len(sample_signal1)!=len(sample_signal2) and op=="Addition":
        pairs = zip_longest(sample_signal1, sample_signal2, fillvalue=0)
        sample_result[:] = [a + b for a, b in pairs]
    if op=="Addition":
        sample_result[:] = [a + b for a, b in zip(sample_signal1, sample_signal2)]
    if len(sample_signal1)!=len(sample_signal2) and op=="Subtraction":
        pairs = zip_longest(sample_signal1, sample_signal2, fillvalue=0)
        sample_result[:] = [a - b for a, b in pairs]
    if op=="Subtraction":
        sample_result[:] = [a - b for a, b in zip(sample_signal1, sample_signal2)]
    return

# def list_size():
#     print(len())


def add_sub(op):
    root = Toplevel()
    root.title(op)
    root.geometry('250x150')

    btn = Button(root, text='Open Signal 1', command=lambda:set_signal1())
    btn.pack(side=TOP, padx=10, pady=10)

    btn2 = Button(root, text='Open Signal 2', command=lambda: set_signal2(op))
    btn2.pack(side=TOP, padx=20, pady=20)
    # print("Add Sub fun: ",len(sample_signal1))
    # print("Add Sub fun: ",len(sample_signal2))

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

