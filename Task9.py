import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
import warnings
from collections import OrderedDict



def fast_convolution():
    from Task4 import I_DFT as DFT_IDFT
    index1, sample1 = open_file("Signals/Task9/Convolution/Input_conv_Sig1.txt")
    index2, sample2 = open_file("Signals/Task9/Convolution/Input_conv_Sig2.txt")

    N1 = len(sample1)
    N2 = len(sample2)

    padding_val = N1 + N2 - 1

    index1, sample1= padding(padding_val, N1,index1,sample1)
    index2, sample2= padding(padding_val, N2,index2,sample2)

    amp1, phase1 = DFT_IDFT(sample1,0,False,[],[])
    amp2, phase2 = DFT_IDFT(sample2,0,False,[],[])


    # ToDo:
    #  Nsh3'al al DFT
    #  use convolution function
    #  apply IDFT

def padding(N, lst_size, index, sample):

    for i in range(lst_size, N):
        index.append(index[-1] + 1)

    sample = sample + [0.0] * (N - lst_size)

    return index, sample
def fast_correlation():
    return
