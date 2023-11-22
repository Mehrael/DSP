import math
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbx
from ImpFunctions import *
import numpy as np
from Signals.Task4.signalcompare import *
import warnings
from collections import OrderedDict
from Task5 import *

# filter out all warnings
warnings.filterwarnings("ignore")
amp_to_modify = []
phase_to_modify = []
amp_modified = []
phase_modified = []
options_amp = []
options_phase = []
freq_sampling = 0


def Task4_screen():
    root = Toplevel()
    root.title("Frequency Domain")
    root.geometry('300x300')

    tkinter.Label(root, text="Sampling Frequency in Hz").pack()

    Fs = tkinter.Entry(root)
    Fs.pack(padx=5, pady=5)

    Button(root, text='DFT', command=lambda: set_signals(1, Fs.get())).pack(padx=10, pady=10)

    Button(root, text='Modify Amplitude or Phase', command=lambda: modify_screen()).pack(padx=10, pady=10)

    Button(root, text='Signal Reconstruction using IDFT', command=lambda: set_signals(2, 0)).pack(padx=10, pady=10)

    Button(root, text='DCT & Remove DC', command=lambda: Task5_screen()).pack(side=TOP, padx=10, pady=10)


def set_signals(op, Fs):
    if op == 1:  # DFT
        msg = ""
        try:
            Fs = int(Fs)
            global freq_sampling
            freq_sampling = Fs
            if Fs == 0:
                raise ValueError
        except:
            msg += "Fs Must be an Integer value and not 0"

        if msg != "":
            msgbx.showerror(title="Error", message=msg, )
            return

        index, sample = open_file('Signals/Task4/DFT/input_Signal_DFT.txt')
        # print('index: ', index)
        # print('sample: ', sample)
        I_DFT(sample, Fs, False)
        # print(dft)

    elif op == 2:  # IDFT
        amp, phase = special_open_file(',', 'Signals/Task4/IDFT/Input_Signal_IDFT_A,Phase.txt')
        # print('index: ', amp)
        # print('sample: ', phase)
        I_DFT([], 0, True, amp, phase)
    return


def I_DFT(x, Fs, flag, amp=[], phase=[]):
    N = len(x)
    sample = np.zeros(N, dtype=np.complex128)
    img = -2j

    if flag:  # IDFT
        img *= -1
        x = amp * (np.cos(phase) + 1j * np.sin(phase))
        # print(e)
        N = len(x)
        sample = np.zeros(N)
        index = np.zeros(N)

    for n in range(N):
        # print("-----------------------------")
        for k in range(N):
            sample[n] += x[k] * np.exp(img * np.pi * k * n / N)
        #     print("N: ",n," ,X[",k,"]: ",X[k])
        # print("X[",k,"]: ",X[k])
        if flag:
            index[n] = np.round(n)
            sample[n] = np.round(sample[n] / N)

    if flag:  # IDFT -> output is in the frequency domain 0 0 len
        print('index: ', index)
        print('sample: ', sample)
        first_3_lines = """0
0
""" + str(len(sample))
        write_file("Output_IDFT.txt", first_3_lines, index, sample)
    else:  # DFT -> output is in the time domain 0 1 len
        amp, phase = Amp_phase(sample)
        if SignalComapreAmplitude(amp):
            print("Amplitude Test passed successfully")
            sketch(int(Fs), amp, "Amplitude Vs Frequency")
        if SignalComaprePhaseShift(phase):
            print("Phase Test passed successfully")
            sketch(int(Fs), phase, "Phase Vs Frequency")

        first_3_lines = """0
1
""" + str(len(sample))
        write_file("Output_DFT.txt", first_3_lines, amp, phase)
    # print("-------------------")
    # print(amp, phase)
    # return X


def Amp_phase(x):
    N = len(x)
    amp = np.zeros(N)
    phase = np.zeros(N)
    phase_to_modify[:] = np.zeros(N)

    for i in range(N):
        amp[i] = math.sqrt((x[i].real ** 2) + (x[i].imag ** 2))
        # print("Phase: ", x[i].imag, "/",x[i].real)
        phase[i] = np.arctan2(x[i].imag, x[i].real)

        if x[i].real < 0 and x[i].imag == 0.0:
            phase[i] *= -1
        amp[i] = np.round(amp[i], 13)
        phase[i] = np.round(phase[i], 13)
        phase_to_modify[i] = abs(phase[i])
        # print(amp[i], phase[i])
        # print(np.around(amp[i],13))

    # print(amp)
    # print()
    # print(phase)

    amp_to_modify[:] = amp
    options_amp[:] = list(OrderedDict.fromkeys(amp_to_modify))
    print(options_amp)
    options_phase[:] = list(OrderedDict.fromkeys(phase_to_modify))
    print(options_phase)
    phase_to_modify[:] = phase

    return amp, phase


def sketch(F, yAxis, txt):
    N = len(yAxis)
    funF = (2 * np.pi * F) / N
    xAxis = np.zeros(N)
    # Ts = 1 / F
    # funF2 = (2 * np.pi) / (N * Ts)
    # print(funF, funF2)

    for i in range(N):
        xAxis[i] += funF * (1 + i)

    draw_signal(xAxis, yAxis, txt)


def modify_screen():
    if options_amp == [] and options_phase == []:
        msgbx.showerror(title="Error", message="You must get the DFT first", )
        return
    window = Toplevel()
    window.title("Modify Signal")
    window.geometry('300x400')
    chosen_amp = tkinter.DoubleVar()
    chosen_amp.set(0.0)
    chosen_phase = tkinter.DoubleVar()
    chosen_phase.set(0.0)

    tkinter.Label(window, text="Choose the amplitude point to modify:").pack()
    OptionMenu(window, chosen_amp, *options_amp).pack(side=TOP, padx=10, pady=5)
    tkinter.Label(window, text="Enter the value to modify the amplitude to: ").pack()

    amp_val = tkinter.Entry(window)
    amp_val.pack(padx=5, pady=5)

    Button(window, text='Modify Amplitude', command=lambda: modify_signal(1, amp_val.get(), chosen_amp.get())).pack(padx=10, pady=10)

    tkinter.Label(window, text="Choose the phase shift point to modify:").pack()
    OptionMenu(window, chosen_phase, *options_phase).pack(side=TOP, padx=10, pady=5)
    tkinter.Label(window, text="Enter the value to modify the phase shift to: ").pack()

    phase_val = tkinter.Entry(window)
    phase_val.pack(padx=5, pady=5)

    Button(window, text='Modify Phase',command=lambda: modify_signal(0, phase_val.get(), chosen_phase.get())).pack(padx=10, pady=10)


def modify_signal(choice, value, point):
    msg = ""
    try:
        value = float(value)
    except:
        msg += "The new value Must be a Float value"

    if msg != "":
        msgbx.showerror(title="Error", message=msg, )
        return

    if choice == 1:
        amp_modified[:] = [value if x == point else x for x in amp_to_modify]
        print('Before:', amp_to_modify)
        print('After', amp_modified)
        sketch(freq_sampling, amp_to_modify, "Amplitude Before Modification")
        sketch(freq_sampling, amp_modified, "Amplitude After Modification")
    else:
        phase_modified[:] = [value if x == point else x for x in phase_to_modify]
        phase_modified[:] = [-value if x == -point else x for x in phase_modified]
        print('Before', phase_to_modify)
        print('After', phase_modified)
        sketch(freq_sampling, phase_to_modify, "Phase Shift Before Modification")
        sketch(freq_sampling, phase_modified, "Phase Shift After Modification")
    return
