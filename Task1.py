import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import numpy as np
import matplotlib.pyplot as plt
from comparesignals import SignalSamplesAreEqual

signalType = None
isPeriodic = None
N = 0
index = []
sampleAmp = []
SinFile = "Signals/Sin_Cos/SinOutput.txt"
CosFile = "Signals/Sin_Cos/CosOutput.txt"


def part1():
    root = Toplevel()
    root.title('Drawing Signals')
    root.geometry('250x150')

    btn = Button(root, text='Open', command=lambda: open_file())
    btn.pack(side=TOP, padx=10, pady=10)

    btn2 = Button(root, text='Draw Signal', command=lambda: draw_signal())
    btn2.pack(side=TOP, padx=20, pady=20)

    def open_file():
        file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
        if file is not None:
            content = file.readlines()
            for i, x in enumerate(content):
                print(x)
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
                sampleAmp.append(float(x[1]))

    def draw_signal():
        fig, axs = plt.subplots(1, 2)

        axs[0].set_title('Discrete Signal')
        for (i, j) in zip(index, sampleAmp):
            axs[0].plot([i, i], [0, j], color='red')
        axs[0].scatter(index, sampleAmp)
        axs[0].axhline(0, color='black', linewidth=0.5)
        axs[0].axvline(0, color='black', linewidth=0.5)
        axs[0].set_xlabel('No. of Samples')
        axs[0].set_ylabel('Amplitude')

        axs[1].plot(index, sampleAmp)
        axs[1].set_title('Continuous Signal')
        axs[1].axhline(0, color='black', linewidth=0.5)
        axs[1].axvline(0, color='black', linewidth=0.5)
        axs[1].set_xlabel('Time')
        axs[1].set_ylabel('Amplitude')
        plt.show()
        return


def part2():
    window = Toplevel()
    window.title('Input Signal')
    window.geometry('300x450')
    function = IntVar()

    err = tkinter.Label(window, text="")
    err.pack(padx=5, pady=5)

    label = tkinter.Label(window, text="Function ")
    label.pack()

    Radiobutton(window, text="Cos()", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)
    Radiobutton(window, text="Sin()", variable=function, value=2, command=lambda: function.get()).pack(padx=5, pady=5)

    label = tkinter.Label(window, text="Amplitude")
    label.pack(padx=5, pady=5)

    amplitude = tkinter.Entry(window)
    amplitude.pack(padx=5, pady=5)

    label = tkinter.Label(window, text="Analog Frequency")
    label.pack(padx=5, pady=5)

    analog_freq = tkinter.Entry(window)
    analog_freq.pack(padx=5, pady=5)

    label = tkinter.Label(window, text="Sampling Frequency")
    label.pack(padx=5, pady=5)

    sampling_freq = tkinter.Entry(window)
    sampling_freq.pack(padx=5, pady=5)

    label = tkinter.Label(window, text="Phase Shift")
    label.pack(padx=5, pady=5)

    phase_shift = tkinter.Entry(window)
    phase_shift.pack(padx=5, pady=5)

    btn = Button(window, text='Draw', command=lambda: draw_signals())
    btn.pack(padx=5, pady=5)

    def draw_signals():
        if validation():
            fun = function.get()
            A = int(amplitude.get())
            F = int(analog_freq.get())
            Fs = int(sampling_freq.get())
            theta = float(phase_shift.get())

            # T = 1.0 / F
            Ts = 1.0 / Fs
            t = np.arange(0, 1, Ts)

            if fun == 1:
                y = A * np.cos(2 * np.pi * F * t + theta)
                fun_name = "Cos"
                file_name = CosFile
            elif fun == 2:
                y = A * np.sin(2 * np.pi * F * t + theta)
                fun_name = "Sin"
                file_name = SinFile

            # Plot the signal
            fig, axs = plt.subplots(1, 2)
            axs[0].set_title('Discrete Signal')
            axs[0].set_title('Discrete Signal')

            axs[0].scatter(t, y)
            axs[0].axhline(0, color='black', linewidth=0.5)
            axs[0].axvline(0, color='black', linewidth=0.5)
            axs[0].set_xlabel('No. of Samples')
            axs[0].set_ylabel('Amplitude')

            axs[1].plot(t, y)
            axs[1].set_title('Continuous Signal')
            axs[1].axhline(0, color='black', linewidth=0.5)
            axs[1].axvline(0, color='black', linewidth=0.5)
            axs[1].set_xlabel('Time')
            axs[1].set_ylabel('Amplitude')
            plt.show()

            SignalSamplesAreEqual(file_name, len(y), y)
            return

    def validation():
        text_err = ""
        try:
            x = function.get()
            if x == 0:
                raise ValueError
        except ValueError:
            text_err += "You must choose a function\n"

        try:
            x = int(amplitude.get())
            if x == 0 or x == NONE:
                raise ValueError
        except ValueError:
            text_err += "The Amplitude Must be an Integer value and not 0\n"

        try:
            x = int(analog_freq.get())
            if x == 0 or x == NONE:
                raise ValueError
        except ValueError:
            text_err += "The Analog Frequency Must be an Integer\n"

        try:
            x = int(sampling_freq.get())
            if x == 0 or x == NONE:
                raise ValueError
        except ValueError:
            text_err += "The Sampling Frequency Must be an Integer\n"

        try:
            float(phase_shift.get())
        except ValueError:
            text_err += "The Phase Shift Must be a Decimal number\n"

        err.config(text=text_err)
        if text_err == "":
            return True
        else:
            return False
