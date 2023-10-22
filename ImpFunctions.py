import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual



def open_file():

    signalType = None
    isPeriodic = None
    N = 0
    index = []
    sample = []
    file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        content = file.readlines()
        for i, x in enumerate(content):
            if i == 0 and int(x) == 0:
                signalType = 0
                continue
            elif i == 0 and int(x) == 1:
                signalType = 1
                continue
            if i == 1 and int(x) == 0:
                isPeriodic = False
                continue
            elif i == 1 and int(x) == 1:
                isPeriodic = True
                continue
            if i == 2:
                N = int(x)
                continue
            x = x.split()
            index.append(int(x[0]))
            sample.append(float(x[1]))

    print("ImpFunctions: ",len(sample))

    return index, sample