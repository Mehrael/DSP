import numpy as np
from Task7 import *
from Signals.Task9.Convolution.ConvTest import ConvTest

def fast_convolution():
    index1, sample1 = open_file("Signals/Task9/Convolution/Input_conv_Sig1.txt")
    index2, sample2 = open_file("Signals/Task9/Convolution/Input_conv_Sig2.txt")

    N1 = len(sample1)
    N2 = len(sample2)

    N = N1 + N2 - 1

    sample1 = sample1 + [0.0] * (N - N1)
    sample2 = sample2 + [0.0] * (N - N2)

    sample1 = DFT(sample1)
    sample2 = DFT(sample2)

    conv_signal = sample1 * sample2

    result = IDFT(conv_signal)

    ConvTest(index1,result)

def DFT(x):
    N = len(x)
    sample = np.zeros(N, dtype=np.complex128)

    for n in range(N):
        for k in range(N):
            sample[n] += x[k] * np.exp(-2j * np.pi * k * n / N)

    return sample

def IDFT(x):
    N = len(x)
    sample = np.zeros(N)

    for n in range(N):
        for k in range(N):
            sample[n] += x[k] * np.exp(2j * np.pi * k * n / N)
        sample[n] = sample[n] / N

    return sample
def fast_correlation():
    return
