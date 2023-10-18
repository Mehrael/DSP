import tkinter
from tkinter import *
from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Input Signal')
root.geometry('300x450')
function = IntVar()

err = tkinter.Label(root, text="")
err.pack(padx=5, pady=5)

label = tkinter.Label(root, text="Function ")
label.pack()

Radiobutton(root, text="Cos()", variable=function, value=0, command=lambda: function.get()).pack(padx=5, pady=5)
Radiobutton(root, text="Sin()", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)

label = tkinter.Label(root, text="Amplitude")
label.pack(padx=5, pady=5)

amplitude = tkinter.Entry(root)
amplitude.pack(padx=5, pady=5)

label = tkinter.Label(root, text="Analog Frequency")
label.pack(padx=5, pady=5)

analog_freq = tkinter.Entry(root)
analog_freq.pack(padx=5, pady=5)

label = tkinter.Label(root, text="Sampling Frequency")
label.pack(padx=5, pady=5)

sampling_freq = tkinter.Entry(root)
sampling_freq.pack(padx=5, pady=5)

label = tkinter.Label(root, text="Phase Shift")
label.pack(padx=5, pady=5)

phase_shift = tkinter.Entry(root)
phase_shift.pack(padx=5, pady=5)

btn = Button(root, text='Draw', command=lambda:get_values())
btn.pack(padx=5, pady=5)

def get_values():
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
            y = A * np.sin(2 * np.pi * F * t + theta)
            fun_name = "Sin"
        else:
            y = A * np.cos(2 * np.pi * F * t + theta)
            fun_name = "Cos"

        # Plot the signal
        plt.figure()
        plt.scatter(t, y)
        plt.title(f'{fun_name} Wave: A={A}, theta={theta}, f={F}, fs={Fs}')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
        return


def validation():
    text_err = ""
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

# def disc():
# root = Tk()
# root.title('Input Signal')
# root.geometry('300x450')
#
#
# err = tkinter.Label(root, text="")
# err.pack(padx=5, pady=5)
#
# label = tkinter.Label(root, text="Function ")
# label.pack()
#
# Radiobutton(root, text="Cos()", variable=function, value=0, command=lambda: function.get()).pack(padx=5, pady=5)
# Radiobutton(root, text="Sin()", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)
#
# label = tkinter.Label(root, text="Amplitude")
# label.pack(padx=5, pady=5)
#
# amplitude = tkinter.Entry(root)
# amplitude.pack(padx=5, pady=5)
#
# label = tkinter.Label(root, text="Analog Frequency")
# label.pack(padx=5, pady=5)
#
# analog_freq = tkinter.Entry(root)
# analog_freq.pack(padx=5, pady=5)
#
# label = tkinter.Label(root, text="Sampling Frequency")
# label.pack(padx=5, pady=5)
#
# sampling_freq = tkinter.Entry(root)
# sampling_freq.pack(padx=5, pady=5)
#
# label = tkinter.Label(root, text="Phase Shift")
# label.pack(padx=5, pady=5)
#
# phase_shift = tkinter.Entry(root)
# phase_shift.pack(padx=5, pady=5)
#
# btn = Button(root, text='Draw', command=lambda:get_values())
# btn.pack(padx=5, pady=5)

root.mainloop()
