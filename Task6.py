import statistics
import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
from Signals.Task6.Shifting_and_Folding.Shift_Fold_Signal import *
def Task6_screen():
    root = Toplevel()
    root.title("Shifting and Folding")
    root.geometry('300x200')
    function = IntVar()
    Radiobutton(root, text="Fold ?", variable=function, value=1, command=lambda: function.get()).pack(padx=5, pady=5)
    # Button(root,text='Choose Input File',command= lambda:open_file())


def folding(index, sample):
    output_index = index
    output_sample = sample[::-1]
    # Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_fold.txt', output_index, output_sample)
    return output_index, output_sample


def shifting(k, index, sample):
    # k = -1 * k
    output_index = [x + k for x in index]
    output_sample = sample
    return output_index, output_sample


def shifting_and_folding(k, index, sample):
    foldedindex,foldedsample=folding(index,sample)
    output_index,output_sample=shifting(k,foldedindex,foldedsample)
    if k ==500:
        Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_ShifFoldedby500.txt',output_index,output_sample)
    else:
        Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_ShiftFoldedby-500.txt',output_index,output_sample)
    return output_index,output_sample
