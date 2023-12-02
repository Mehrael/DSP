import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np

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

    Button(root, text='Calculate',command=lambda: convolution()).pack(padx=10, pady=10)

def setSignal(x):
    if x == 1:
        signal_index_1[:],signal_samples_1[:] = open_file()
    else:
        signal_index_2[:],signal_samples_2[:] = open_file()

def convolution():
    print("inedx 1:",signal_index_1)
    print("samples 1:",signal_samples_1)
    print("inedx 2:",signal_index_2)
    print("samples 2:",signal_samples_2)