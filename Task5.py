from ImpFunctions import *
import math
import statistics
import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
from Signals.Task4.signalcompare import *
import warnings
from collections import OrderedDict
N = 0

def Task5_screen():
    root = Toplevel()
    root.title("DCT")
    root.geometry('300x200')

    tkinter.Label(root, text="Number of samples to be saved").pack()

    Fs = tkinter.Entry(root)
    Fs.pack(padx=5, pady=5)

    Button(root, text='DCT', command=lambda: DCT()).pack(side=TOP, padx=10, pady=10)

def DCT():
    index, sample = open_file()

    global N
    N = len(sample)
    new_signal = []
    # the index is not checked in the compare signals file
    new_index = [0] * N
    for i in range(N):
        acc = 0
        for j in range(N):
            x = math.pi * ((2 * j) - 1) * ((2 * i) - 1)
            acc += sample[j] * math.cos(x)
        new_signal.append(math.sqrt(2 / N) * acc)
    return new_signal, new_index


def remove_dc(domain, sample, index):
    if domain:
        mean = statistics.mean(sample)
        for i in range(len(sample)):
            sample[i] -= mean
    return sample
