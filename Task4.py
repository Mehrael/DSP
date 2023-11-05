import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
from Signals.Task4.signalcompare import *

index = []
sample = []
def Task4_screen():
    root = Toplevel()
    root.title("Frequency Domain")
    root.geometry('300x200')

    tkinter.Label(root, text="Sampling Frequency in Hz").pack()

    Fs = tkinter.Entry(root)
    Fs.pack(padx=5, pady=5)

    Button(root, text='DFT', command=lambda: set_signals(1,Fs.get())).pack(padx=10, pady=10)

    Button(root, text='Modify Amplitude or Phase',
           # command=lambda: set_signals(function.get(), num.get())
           ).pack(padx=10, pady=10)

    Button(root, text='Signal Reconstruction using IDFT',
           # command=lambda: set_signals(function.get(), num.get())
           ).pack(padx=10, pady=10)


def set_signals(op,Fs):
    if op == 1:
        index[:], sample[:] = open_file('Signals/Task4/DFT/input_Signal_DFT.txt')
        # print('index: ', index)
        # print('sample: ', sample)
        DFT(sample,Fs)
        # print(dft)
    return

def DFT(x,Fs):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)

    for k in range(N):
        # print("-----------------------------")
        for n in range(N):
            X[k] += x[n] * round(np.exp(-2j * np.pi * k * n / N), 13)
        #     print("N: ",n," ,X[",k,"]: ",X[k])
        # print("X[",k,"]: ",X[k])
    amp, phase = Amp_phase(X)
    sketch(int(Fs),amp,"Amplitude Vs Frequency")
    sketch(int(Fs),phase,"Phase Vs Frequency")
    # print("-------------------")
    # print(amp, phase)
    # return X

def Amp_phase(x):
    N = len(x)
    amp = np.zeros(N)
    phase = np.zeros(N)

    for i in range(N):
        amp[i] = np.sqrt(np.square(x[i].real) + np.square(x[i].imag))
        # print("Phase: ", x[i].imag, "/",x[i].real)
        phase[i] = np.arctan2(x[i].imag, x[i].real)

        if x[i].real < 0 and x[i].imag == 0.0:
            phase[i] *= -1
        # print(amp[i], phase[i])


    # print(amp)
    # print()
    # print(phase)
    # if DFTSignalComapreAmplitude(amp):
    #     print("Amplitude Test Passed")
    # else:
    #     print("Amplitude Test Failed")
    return amp, phase

def sketch(F, yAxis,txt):
    N = len(yAxis)
    funF = (2 * np.pi * F) / N
    xAxis = np.zeros(N)
    # Ts = 1 / F
    # funF2 = (2 * np.pi) / (N * Ts)
    # print(funF, funF2)

    for i in range(N):
        xAxis[i] += funF*(1+i)

    draw_signal(xAxis,yAxis,txt)