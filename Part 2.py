import tkinter
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Input Signal')
root.geometry('300x450')

function = IntVar()

def get_values():
    if validation():
        fun = function.get()
        A = amplitude.get()
        analog = analog_freq.get()
        sampling = sampling_freq.get()
        shift = phase_shift.get()
        return fun, A, analog, sampling, shift


def validation():
    text_err = ""
    try:
        int(amplitude.get())
    except ValueError:
        text_err += "The Amplitude Must be an Integer\n"

    try:
        int(analog_freq.get())
    except ValueError:
        text_err += "The Analog Frequency Must be an Integer\n"

    try:
        int(sampling_freq.get())
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

btn = Button(root, text='Draw', command=get_values)
btn.pack(padx=5, pady=5)

root.mainloop()
