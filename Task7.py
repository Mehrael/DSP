import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
from Signals.Task6.Convolution.ConvTest import *

signal_index_1 = []
signal_index_2 = []
signal_samples_1 = []
signal_samples_2 = []


def Task7_screen():
    root = Toplevel()
    root.title("Convolution")
    root.geometry('250x150')

    Button(root, text='Signal 1', command=lambda: setSignal(1)).pack(padx=10, pady=10)

    Button(root, text='Signal 2', command=lambda: setSignal(2)).pack(padx=10, pady=10)

    Button(root, text='Calculate', command=lambda: convolution()).pack(padx=10, pady=10)


def setSignal(x):
    if x == 1:
        signal_index_1[:], signal_samples_1[:] = open_file()
    else:
        signal_index_2[:], signal_samples_2[:] = open_file()


def get_boundaries():
    min_bound = min(signal_index_1) + min(signal_index_2)
    max_bound = max(signal_index_1) + max(signal_index_2)
    return min_bound, max_bound


def convolution():
    conv_index = []
    conv_sample = []
    start, end = get_boundaries()
    for n in range(start, end + 1):
        acc = 0
        for k in range(min(signal_index_1), end+1):
            if k not in signal_index_1:
                break
            elif (n - k) not in signal_index_2:
                continue
            else:
                i1 = signal_index_1.index(k)
                i2 = signal_index_2.index(n - k)
                acc += signal_samples_1[i1] * signal_samples_2[i2]

                print('Indices:', i1, '  ', i2)

        conv_index.append(n)
        conv_sample.append(acc)
    ConvTest(conv_index, conv_sample)
    print('Index:', conv_index)
    print('Sample:', conv_sample)
    return
