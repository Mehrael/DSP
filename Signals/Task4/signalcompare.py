import math


# Use to test the Amplitude of DFT and IDFT
def SignalComapreAmplitude(SignalInput=[], SignalOutput=[64, 20.9050074380220, 11.3137084989848, 8.65913760233915,
                                                         8, 8.65913760233915, 11.3137084989848,
                                                         20.9050074380220]):
    if len(SignalInput) != len(SignalOutput):
        print(len(SignalInput), len(SignalOutput))
        print(SignalInput)
        print(SignalOutput)
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i] - SignalOutput[i]) > 0.001:
                print("abs(SignalInput[i]-SignalOutput[i])>0.001", i, SignalInput[i], SignalOutput[i],
                      abs(SignalInput[i] - SignalOutput[i]))
                return False
            # A = round(SignalInput[i])
            # B = round(SignalOutput[i])
            # if A != B:
            #     print("A != B", i, A, B)
            #     return False
            elif SignalInput[i]!=SignalOutput[i]:
                print("SignalInput[i] != SignalOutput[i]", i, SignalInput[i], SignalOutput[i])
            return False
        return True


def RoundPhaseShift(P):
    while P < 0:
        P += 2 * math.pi
    return float(P % (2 * math.pi))


# Use to test the PhaseShift of DFT
def SignalComaprePhaseShift(SignalInput=[],
                            SignalOutput=[0, 1.96349540849362, 2.35619449019235, 2.74889357189107, -3.14159265358979,
                                          -2.74889357189107, -2.35619449019235, -1.96349540849362]):
    if len(SignalInput) != len(SignalOutput):
        print(len(SignalInput), len(SignalOutput))
        print(SignalInput)
        print(SignalOutput)
        return False
    else:
        for i in range(len(SignalInput)):
            A = round(SignalInput[i])
            B = round(SignalOutput[i])
            if abs(A - B) > 0.0001:
                print("abs(A-B)>0.0001", A, B, abs(A - B))
                return False
            elif A != B:
                print("A != B", i, A, B)
                return False
        return True
