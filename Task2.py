from tkinter import messagebox
from ImpFunctions import *
import tkinter
from tkinter import *
from tkinter.ttk import *
from itertools import zip_longest
import numpy as np
from comparesignals import SignalSamplesAreEqual

index_signal1 = []
sample_signal1 = []

index_signal2 = []
sample_signal2 = []

index_result = []
sample_result = []

index_signal = list(list())
sample_signal = list(list())
# const=None
op = ""


def set_op(x):
    op = x
    if op == "Addition" or op == "Subtraction":
        if op == "Addition":
            add()
        else:
            add_sub(op)
        # print("Set Op fun Signal1 : ",len(sample_signal1))
        # print("Set Op fun Signal2 : ",len(sample_signal2))
    elif op == "Multiplication" or op == "Shifting":
        mul_shift(op)
    elif op == "Squaring" or op == "Accumulation":
        sqr_acc(op)
    elif op == "Normalization":
        norm(op)
    else:
        messagebox.showinfo("", "Select an Operation please")


def add():
    root = Toplevel()
    root.title(op)
    root.geometry('300x150')

    label = tkinter.Label(root, text="Constant Value")
    label.pack(padx=5, pady=5)

    textbox = tkinter.Entry(root)
    textbox.pack(padx=5, pady=5)

    btn = Button(root, text='Proceed', command=lambda: create_buttons(textbox))
    btn.pack(side=TOP, padx=10, pady=10)
    return


def create_buttons(n):
    root = Tk()
    root.geometry('300x150')
    for i in range(int(n.get())):
        button = Button(root, text=f"Signal {i + 1}", command=lambda: set_signal())
        button.pack()
    Button(root, text='Calculate', command=lambda: calc()).pack()
    root.mainloop()


def row_with_max_length(lst):
    return max(range(len(lst)), key=lambda index: len(lst[index]))


def calc():
    x = row_with_max_length(index_signal)
    index_result[:] = index_signal[x]

    local_sample_result = [0] * len(sample_signal[x])

    for sample in sample_signal:
        if len(sample) < len(local_sample_result):
            sample = list(sample) + [0] * (len(local_sample_result) - len(sample))
        local_sample_result = [a + b for a, b in zip(local_sample_result, sample)]

    sample_result[:]=local_sample_result

    draw_signal(index_result, sample_result, "Resultant Signal")
    # for i in range(len(sample_signal)-1):
    #     if len(sample_signal[i]) != len(sample_signal[i+1]):
    #         pairs = zip_longest(sample_signal[i], sample_signal[i+1], fillvalue=0)
    #         sample_result[:] = [a + b for a, b in pairs]
    #     else:
    #         sample_result[:] = [a + b for a, b in zip(sample_signal[i], sample_signal[i+1])]
    return


def set_signal1():
    index_signal1[:], sample_signal1[:] = open_file()
    # print("Set Signal1: ",len(sample_signal1))
    return


def set_signal():
    index, sample = open_file()
    index_signal.append(index)
    sample_signal.append(sample)
    # print("Set Signal1: ",len(sample_signal1))
    return


def set_signal2():
    index_signal2[:], sample_signal2[:] = open_file()
    # print("Set Signal2: ",len(sample_signal2))
    return


def calculate(op, entrybox):
    if op == "Addition" or op == "Subtraction":
        if len(sample_signal[0]) != len(sample_signal[1]) and op == "Addition":
            pairs = zip_longest(sample_signal[0], sample_signal[1], fillvalue=0)
            sample_result[:] = [a + b for a, b in pairs]
            if len(sample_signal1) >= len(sample_signal2):
                index_result[:] = index_signal[0]
            else:
                index_result[:] = index_signal[1]
        if op == "Addition":
            sample_result[:] = [a + b for a, b in zip(sample_signal[0], sample_signal[1])]
            index_result[:] = index_signal[1]
        if len(sample_signal1) != len(sample_signal2) and op == "Subtraction":
            pairs = zip_longest(sample_signal1, sample_signal2, fillvalue=0)
            sample_result[:] = [a - b for a, b in pairs]
            if len(sample_signal1) >= len(sample_signal2):
                index_result[:] = index_signal1
            else:
                index_result[:] = index_signal2
        if op == "Subtraction":
            sample_result[:] = [a - b for a, b in zip(sample_signal2, sample_signal1)]
            index_result[:] = index_signal2
        SignalSamplesAreEqual("Signals/Task2/output signals/Signal1+signal2.txt", len(sample_result), sample_result)
        # SignalSamplesAreEqual("Signals/Task2/output signals/signal1+signal3.txt",len(sample_result),sample_result)
        # SignalSamplesAreEqual("Signals/Task2/output signals/signal1-signal2.txt",len(sample_result),sample_result)
        # SignalSamplesAreEqual("Signals/Task2/output signals/signal1-signal3.txt",len(sample_result),sample_result)

    elif op == "Multiplication":
        const = int(entrybox.get())
        sample_result[:] = [sample * const for sample in sample_signal1]
        index_result[:] = index_signal1
        # SignalSamplesAreEqual("Signals/Task2/output signals/MultiplySignalByConstant-Signal1 - by 5.txt",len(sample_result),sample_result)
        # SignalSamplesAreEqual("Signals/Task2/output signals/MultiplySignalByConstant-signal2 - by 10.txt",len(sample_result),sample_result)

    elif op == "Shifting":
        const = int(entrybox.get())
        index_result[:] = [index + const for index in index_signal1]
        sample_result[:] = sample_signal1
        # SignalSamplesAreEqual("Signals/Task2/output signals/output shifting by add 500.txt",len(sample_result),sample_result)
        SignalSamplesAreEqual("Signals/Task2/output signals/output shifting by minus 500.txt", len(sample_result),
                              sample_result)

    elif op == "Normalization":
        minimum = min(sample_signal1)
        maximum = max(sample_signal1)
        choice = int(entrybox.get())
        if choice == 1:
            sample_result[:] = (2 * ((np.array(sample_signal1) - minimum) / (maximum - minimum)) - 1).tolist()
        elif choice == 2:
            sample_result[:] = ((np.array(sample_signal1) - minimum) / (maximum - minimum)).tolist()
        index_result[:] = index_signal1
        # SignalSamplesAreEqual("Signals/Task2/output signals/normalize of signal 1 -- output.txt",len(sample_result),sample_result)
        # SignalSamplesAreEqual("Signals/Task2/output signals/normlize signal 2 -- output.txt",len(sample_result),sample_result)


    elif op == "Squaring":
        sample_result[:] = np.square(sample_signal1)
        index_result[:] = index_signal1
        # SignalSamplesAreEqual("Signals/Task2/output signals/Output squaring signal 1.txt",len(sample_result),sample_result)

    elif op == "Accumulation":
        sample_result[:] = np.cumsum(sample_signal1)
        index_result[:] = index_signal1
        # SignalSamplesAreEqual("Signals/Task2/output signals/output accumulation for signal1.txt",len(sample_result),sample_result)

    draw_signal(index_signal[0], sample_signal[0], "Signal 1")

    if op == "Addition" or op == "Subtraction":
        draw_signal(index_signal[1], sample_signal[1], "Signal 2")

    draw_signal(index_result, sample_result, "Resultant Signal")
    return


def add_sub(op):
    root = Toplevel()
    root.title(op)
    root.geometry('250x150')

    btn = Button(root, text='Open Signal 1', command=lambda: set_signal())
    btn.pack(side=TOP, padx=10, pady=10)

    btn2 = Button(root, text='Open Signal 2', command=lambda: set_signal())
    btn2.pack(side=TOP, padx=20, pady=20)

    Button(root, text='Calculate', command=lambda: calculate(op, NONE)).pack()
    # print("Add Sub fun: ",len(sample_signal1))
    # print("Add Sub fun: ",len(sample_signal2))

    return


def mul_shift(op):
    root = Toplevel()
    root.title(op)
    root.geometry('300x150')

    btn = Button(root, text='Open Signal File', command=lambda: set_signal1())
    btn.pack(side=TOP, padx=10, pady=10)

    label = tkinter.Label(root, text="Constant Value")
    label.pack(padx=5, pady=5)

    input = tkinter.Entry(root)
    input.pack(padx=5, pady=5)

    Button(root, text='Calculate', command=lambda: calculate(op, input)).pack(padx=5, pady=5)


def sqr_acc(op):
    root = Toplevel()
    root.title(op)
    root.geometry('300x100')

    Button(root, text='Open Signal', command=lambda: set_signal1()).pack(side=TOP, padx=10, pady=10)

    Button(root, text='Calculate', command=lambda: calculate(op, 0)).pack(padx=5, pady=5)


def norm(op):
    root = Toplevel()
    root.title(op)
    root.geometry('300x200')
    choice = IntVar()

    Button(root, text='Open Signal', command=lambda: set_signal1()).pack(side=TOP, padx=10, pady=10)

    label = tkinter.Label(root, text="Choose range: ")
    label.pack()

    Radiobutton(root, text="-1 to 1", variable=choice, value=1, command=lambda: choice.get()).pack(padx=5, pady=5)
    Radiobutton(root, text="0 to 1", variable=choice, value=2, command=lambda: choice.get()).pack(padx=5, pady=5)

    Button(root, text='Calculate', command=lambda: calculate(op, choice)).pack(padx=5, pady=5)
