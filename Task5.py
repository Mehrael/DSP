import statistics
import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *

from Signals.Task5.comparesignal2 import *
N = 0
global_new_signal=[]
global_new_index=[]
def Task5_screen():
    root = Toplevel()
    root.title("DCT")
    root.geometry('300x200')

    Button(root, text='DCT', command=lambda: DCT()).pack(side=TOP, padx=10, pady=10)

    tkinter.Label(root, text="Number of samples to be saved").pack()

    n = tkinter.Entry(root)
    n.pack(padx=5, pady=5)

    Button(root, text='Save', command=lambda: save_file(n.get())).pack(side=TOP, padx=10, pady=10)

    Button(root, text='Remove DC', command=lambda: remove_dc(1)).pack(side=TOP, padx=10, pady=10)



def DCT():
    index, sample = open_file()

    global N
    N = len(sample)
    new_signal = []
    # the index is not checked in the compare signals file
    new_index = [0] * N
    for i in range(N):
        acc = 0
        for j in range(N):
            x = (math.pi/(4*N)) * ((2 * j) - 1) * ((2 * i) - 1)
            acc += sample[j] * math.cos(x)
        new_signal.append(math.sqrt(2 / N) * acc)

    global_new_signal[:] = new_signal
    global_new_index[:] = new_index

    SignalSamplesAreEqual("Signals/Task5/DCT/DCT_output.txt",new_signal)
    return new_signal, new_index


def remove_dc(domain):
    index, sample = open_file()
    if domain:
        mean = statistics.mean(sample)
        for i in range(len(sample)):
            sample[i] -= mean

    SignalSamplesAreEqual("Signals/Task5/Remove DC component/DC_component_output.txt", sample)
    return sample


def save_file(n):
    msg=""
    try:
        n = int(n)
        if n == 0:
            raise ValueError
    except:
        msg += "The number Must be an Integer value and not 0"

    if msg != "":
        msgbx.showerror(title="Error", message=msg, )
        return

    first3_line = """0
1
"""+str(n)

    write_file("Task5_output.txt",first3_line,global_new_index,global_new_signal)