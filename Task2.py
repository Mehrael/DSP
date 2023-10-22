import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

op = ""
def set_op(x):
    op = x
    screen(op)

def screen(op):
    root = Tk()
    root.title(op)
    root.geometry('300x100')

    label = tkinter.Label(root, text="Input Value")
    label.pack(padx=5, pady=5)

    input = tkinter.Entry(root)
    input.pack(padx=5, pady=5)

    Button(root, text='Draw',).pack(padx=5, pady=5)

