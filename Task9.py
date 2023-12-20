import numpy as np
from ImpFunctions import *
from Signals.Task9.Convolution.ConvTest import ConvTest
from Signals.Task9.FastCorrelation.CompareSignal import Compare_Signals


def fast_convolution():
    from Task4 import I_DFT as DFT_IDFT
    index1, sample1 = open_file("Signals/Task9/Convolution/Input_conv_Sig1.txt")
    index2, sample2 = open_file("Signals/Task9/Convolution/Input_conv_Sig2.txt")

    N1 = len(sample1)
    N2 = len(sample2)

    N = N1 + N2 - 1

    index1, sample1= padding(N, N1,index1,sample1)
    index2, sample2= padding(N, N2,index2,sample2)

    sample1 = DFT_IDFT(sample1, 0, False, 9)
    sample2 = DFT_IDFT(sample2, 0, False, 9)

    conv_signal = sample1 * sample2

    result = DFT_IDFT(conv_signal, 0, True, 9)

    ConvTest(index1, result)

def padding(N, lst_size, index, sample):

    for i in range(lst_size, N):
        index.append(index[-1] + 1)

    sample = sample + [0.0] * (N - lst_size)

    return index, sample
def fast_correlation():
    from Task4 import I_DFT as DFT_IDFT
    index1, sample1 = open_file("Signals/Task9/FastCorrelation/Corr_input signal1.txt")
    index2, sample2 = open_file("Signals/Task9/FastCorrelation/Corr_input signal2.txt")

    N = len(sample1)
    N2 = len(sample2)

    sample1 = DFT_IDFT(sample1, 0, False, 9)
    sample2 = DFT_IDFT(sample2, 0, False, 9)

    conj = np.zeros(N, dtype=np.complex128)
    for i in range(N):
        conj[i] = sample1[i].real - 1j * sample1[i].imag

    mul = conj * sample2

    res = DFT_IDFT(mul, 0, True, 9)

    if N == N2: # Cross Correlation
        res /= N
    # else it's already Auto Correlation

    Compare_Signals("Signals/Task9/FastCorrelation/Corr_Output.txt", index1, res)
