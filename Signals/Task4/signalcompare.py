import math


# Use to test the Amplitude of DFT and IDFT
def DFTSignalComapreAmplitude(SignalInput=[], SignalOutput=[64, 20.9050074380220, 11.3137084989848, 8.65913760233915,
                                                            8, 8.65913760233915, 11.3137084989848,
                                                            20.9050074380220]):
    if len(SignalInput) != len(SignalInput):
        print("len(SignalInput) != len(SignalInput)")
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i] - SignalOutput[i]) > 0.001:
                print("abs(SignalInput[i] - SignalOutput[i]) > 0.001", i)
                return False
            elif SignalInput[i] != SignalOutput[i]:
                print("SignalInput[i] != SignalOutput[i]", i, SignalInput[i] , SignalOutput[i])
                return False
        return True


def IDFTSignalComapreAmplitude(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i] - SignalOutput[i]) > 0.001:
                return False
            elif SignalInput[i] != SignalOutput[i]:
                return False
        return True


def RoundPhaseShift(P):
    while P < 0:
        P += 2 * math.pi
    return float(P % (2 * math.pi))


# Use to test the PhaseShift of DFT
def SignalComaprePhaseShift(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            A = round(SignalInput[i])
            B = round(SignalOutput[i])
            if abs(A - B) > 0.0001:
                return False
            elif A != B:
                return False
        return True
