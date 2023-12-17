import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
import warnings
from collections import OrderedDict
from Task7 import *
from Signals.Task9.Convolution.ConvTest import ConvTest

def fast_convolution():
    from Task4 import I_DFT as DFT_IDFT
    index1, sample1 = open_file("Signals/Task9/Convolution/Input_conv_Sig1.txt")
    index2, sample2 = open_file("Signals/Task9/Convolution/Input_conv_Sig2.txt")

    print("Index 1: ",index1)
    print("Sample 1: ",sample1)
    print()
    print("Index 2: ",index2)
    print("Sample 2: ",sample2)
    print()

    N1 = len(sample1)
    N2 = len(sample2)

    padding_val = N1 + N2 - 1

    index1, sample1= padding(padding_val, N1,index1,sample1)
    index2, sample2= padding(padding_val, N2,index2,sample2)

    print("Padded Index 1: ", index1)
    print("Padded Sample 1: ", sample1)
    print()
    print("Padded Index 2: ", index2)
    print("Padded Sample 2: ", sample2)
    print()

    amp1, phase1 = DFT_IDFT(sample1,0,False,[],[])
    amp2, phase2 = DFT_IDFT(sample2,0,False,[],[])

    print("Amp 1: ", amp1)
    print("Phase 1: ", phase1)
    print()
    print("Amp 2: ", amp2)
    print("Phase 2: ", phase2)
    print()

    conv_index_amp, conv_amp = convolution(index1,amp1,index2,amp2)
    conv_index_phase, conv_phase = convolution(index1,phase1,index2,phase2)

    print("Conv Amp: ", conv_amp)
    print()
    print("Conv Phase: ", conv_phase)
    print()

    restored_index, restored_sample = DFT_IDFT([],0,True,conv_amp,conv_phase)

    print("Restored Index",restored_index)
    print("Restored Sample",restored_sample)
    print()

    ConvTest(restored_index,restored_sample)

def padding(N, lst_size, index, sample):

    for i in range(lst_size, N):
        index.append(index[-1] + 1)

    sample = sample + [0.0] * (N - lst_size)

    return index, sample

def fast_correlation():
    return
