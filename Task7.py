from ImpFunctions import *
from Signals.Task6.Convolution.ConvTest import *


def get_boundaries(signal_index_1, signal_index_2):
    min_bound = min(signal_index_1) + min(signal_index_2)
    max_bound = max(signal_index_1) + max(signal_index_2)
    return min_bound, max_bound


def convolution():
    signal_index_1, signal_samples_1 = open_file('Signals/Task6/Convolution/Input_conv_Sig1.txt')
    signal_index_2, signal_samples_2 = open_file('Signals/Task6/Convolution/Input_conv_Sig2.txt')
    conv_index = []
    conv_sample = []
    start, end = get_boundaries(signal_index_1, signal_index_2)
    for n in range(start, end + 1):
        acc = 0
        for k in range(min(signal_index_1), end + 1):
            if k not in signal_index_1:
                break
            elif (n - k) not in signal_index_2:
                continue
            else:
                i1 = signal_index_1.index(k)
                i2 = signal_index_2.index(n - k)
                acc += signal_samples_1[i1] * signal_samples_2[i2]

        conv_index.append(n)
        conv_sample.append(acc)
    ConvTest(conv_index, conv_sample)
