import math
from ImpFunctions import *


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
