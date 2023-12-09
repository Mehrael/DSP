import math
from ImpFunctions import *
from Signals.Task8.CompareSignal import *


def denominator(N, s1, s2):
    sum1 = sum2 = 0

    for i in range(N):
        sum1 += s1[i] ** 2
        sum2 += s2[i] ** 2

    res = (1 / N) * math.sqrt(sum1 * sum2)
    return res


def correlation():
    index1, signal1 = open_file('Signals/Task8/Corr_input signal1.txt')
    index2, signal2 = open_file('Signals/Task8/Corr_input signal2.txt')
    den = denominator(len(signal1), signal1, signal2)
    corr = []
    index = []
    for i in range(len(signal1)):
        acc = 0
        for j in range(len(signal2)):
            acc += signal1[j] * signal2[j]
        corr.append((acc / len(signal1)) / den)
        temp = signal2[0]
        signal2.pop(0)
        signal2.append(temp)
        index.append(i)
    Compare_Signals('Signals/Task8/CorrOutput.txt', index, corr)
    return
