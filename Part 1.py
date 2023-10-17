from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt


root =Tk()
root.title('Drawing Signals')
root.geometry('250x150')

signalType=None
isPeriodic=None
N=0
index=[]
sampleAmp=[]

def open_file():
    file=askopenfile(mode='r',filetypes=[('Text files','*.txt')])
    if file is not None:
        content=file.readlines()
        for i,x in enumerate(content):
            print(x)
            if i==0 and int(x) == 0:
               signalType=0
               continue
            elif i==0 and int(x)==1:
                signalType=1
                continue
            if i==1 and int(x)==0:
                isPeriodic=False
                continue
            elif i==1 and int(x)==1:
                isPeriodic=True
                continue
            if i==2:
                N=int(x)
                continue
            x=x.split()
            index.append(int(x[0]))
            sampleAmp.append(float(x[1]))

def draw_signal():
    fig, axs = plt.subplots(1, 2)

    axs[0].set_title('Discrete Signal')
    for (i, j) in zip(index, sampleAmp):
        axs[0].plot([i, i], [0, j], color='red')
    axs[0].scatter(index,sampleAmp)
    axs[0].axhline(0, color='black',linewidth=0.5)
    axs[0].axvline(0, color='black',linewidth=0.5)
    axs[0].set_xlabel('No. of Samples')
    axs[0].set_ylabel('Amplitude')

    axs[1].plot(index, sampleAmp)
    axs[1].set_title('Continuous Signal')
    axs[1].axhline(0, color='black',linewidth=0.5)
    axs[1].axvline(0, color='black',linewidth=0.5)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Amplitude')
    plt.show()
    return


btn= Button(root, text='Open', command=lambda:open_file())
btn.pack(side=TOP,padx=10,pady=10 )

btn2=Button(root,text='Draw Signal', command=lambda:draw_signal())
btn2.pack(side=TOP, padx=20, pady=20)

mainloop()