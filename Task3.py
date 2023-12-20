import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from Signals.Task3.Test1.QuanTest1 import *
from Signals.Task3.Test2.QuanTest2 import *

from ImpFunctions import *

index = []
sample = []

minimum_value = None
maximum_value = None
diff = None
levels = None

interval_start = []
interval_end = []
interval_index = []
interval_midpoint = []

quantized = []
encoded = []
error = []


def screen():
    root = Toplevel()
    root.title("Quantization")
    root.geometry('300x200')

    function = IntVar(value=0)

    tkinter.Label(root, text="Choose the input type: \nNumber of ").pack()

    Radiobutton(root, text="Bits", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)
    Radiobutton(root, text="Levels", variable=function, value=2, command=lambda: function.get()).pack(padx=5, pady=5)

    num = tkinter.Entry(root)
    num.pack(padx=5, pady=5)

    Button(root, text='Calculate', command=lambda: set_signals(function.get(), num.get())).pack(padx=10, pady=10)


def set_signals(op, num):
    if validation(op, num):
        # msgbx.showinfo(message="Great")
        if op == 1:
            index[:], sample[:] = open_file('Signals/Task3/Test1/Quan1_input.txt')
        else:
            index[:], sample[:] = open_file('Signals/Task3/Test2/Quan2_input.txt')
        quan(op, num)
        create_intervals()
        quantize(op, num)
    return


def create_intervals():
    global levels
    global minimum_value
    global diff
    global maximum_value
    for i in range(levels):
        if i == 0:
            interval_start.append(minimum_value)
            interval_end.append(round(minimum_value + diff, 3))
        elif i == levels - 1:
            interval_start.append(interval_end[i - 1])
            interval_end.append(maximum_value)
        else:
            interval_start.append(interval_end[i - 1])
            interval_end.append(round(interval_start[i] + diff, 3))
        interval_midpoint.append(round((interval_start[i] + interval_end[i]) / 2, 3))
    return


def quantize(op, num):
    for x, value in enumerate(sample):
        interval = -1
        for i in range(len(interval_start)):
            if interval_start[i] < value <= interval_end[i]:
                interval = i
                break

        if interval == -1:
            for i in range(len(interval_start)):
                if interval_start[i] <= value < interval_end[i]:
                    interval = i
                    break

        quantized.append(interval_midpoint[interval])
        error.append(round(quantized[x] - value, 3))
        interval_index.append(interval + 1)
        if op == 1:
            # encoding for no. of levels
            encoded.append(bin(interval)[2:].zfill(int(num)))
        else:
            # encoding for no. of bits
            encoded.append(bin(interval)[2:].zfill(int(math.log2(float(num)))))
    if op == 1:
        QuantizationTest1('Signals/Task3/Test1/Quan1_Out.txt', encoded, quantized)
    else:
        QuantizationTest2('Signals/Task3/Test2/Quan2_Out.txt', interval_index, encoded, quantized, error)
    index.clear()
    sample.clear()
    interval_start.clear()
    interval_end.clear()
    interval_midpoint.clear()
    interval_index.clear()
    error.clear()
    encoded.clear()
    quantized.clear()
    return


def quan(op, num):
    if validation(op, num):
        global minimum_value
        minimum_value = min(sample)
        # print(minimum_value)
        global maximum_value
        maximum_value = max(sample)
        # print(maximum_value)
        delta(op, num, minimum_value, maximum_value)
    return


def delta(op, num, minval, maxval):
    global levels
    if op == 1:
        levels = 2 ** int(num)
    else:
        levels = int(num)
    global diff
    diff = (maxval - minval) / levels
    # print(diff)
    return


def validation(op, x):
    msg = ""
    try:
        op = int(op)
        if op == 0:
            raise ValueError
    except:
        msg += "You Must choose the input type \n"

    try:
        x = int(x)
        if x == 0 or x == NONE:
            raise ValueError
    except:
        msg += "The input Must be an Integer value and not 0"

    if msg != "":
        msgbx.showerror(title="Error", message=msg, )
    else:
        return True
