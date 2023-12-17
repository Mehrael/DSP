import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
from Task4 import *


def fast_convolution():
    index1, sample1 = open_file("Signals/Task9/Convolution/Input_conv_Sig1.txt")
    index2, sample2 = open_file("Signals/Task9/Convolution/Input_conv_Sig2.txt")

    N1 = len(sample1)
    N2 = len(sample2)

    padding_val = N1 + N2 - 1

    padded_sample1 = sample1 + [0.0] * (padding_val - N1)
    padded_sample2 = sample2 + [0.0] * (padding_val - N2)

    amp1, phase1 = I_DFT(padded_sample1,0,False)
    amp2, phase2 = I_DFT(padded_sample2,0,False)

    # ToDo:
    #  padding index lists
    #  use convolution function
    #  apply IDFT

def fast_correlation():
    return
