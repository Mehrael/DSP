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
        screen2(op)

def set_lists():
    index_signal1,sample_signal1=open_file()
    print(len(sample_signal1))
    return

def list_size():
    print(len(sample_signal1))


def screen2(op):
    root = Toplevel()
    root.title(op)
    root.geometry('250x150')

    btn = Button(root, text='Open Signal 1', command=lambda: set_lists())
    btn.pack(side=TOP, padx=10, pady=10)


    btn2 = Button(root, text='Open Signal 2', command=lambda: set_lists())
    btn2.pack(side=TOP, padx=20, pady=20)

    return
def screen(op):
    root = Tk()
    root.title(op)
    root.geometry('300x100')

    label = tkinter.Label(root, text="Input Value")
    label.pack(padx=5, pady=5)

    input = tkinter.Entry(root)
    input.pack(padx=5, pady=5)

    Button(root, text='Draw',).pack(padx=5, pady=5)

