import tkinter.messagebox as msgbx
from Signals.Task6.Shifting_and_Folding.Shift_Fold_Signal import *
from Signals.Task6.Derivative.DerivativeSignal import *
from Task4 import *


def Task6_screen():
    root = Toplevel()
    root.title("Time Domain")
    root.geometry('300x450')

    tkinter.Label(root, text="Window Size").pack()

    win_size = tkinter.Entry(root)
    win_size.pack(padx=5, pady=5)

    tkinter.Label(root, text="Choose a signal").pack()

    testCase = IntVar(value=0)
    Radiobutton(root, text="Signal 1", variable=testCase, value=1, command=lambda: testCase.get()).pack(padx=5, pady=5)
    Radiobutton(root, text="Signal 2", variable=testCase, value=2, command=lambda: testCase.get()).pack(padx=5, pady=5)

    Button(root, text='Smoothing', command=lambda: Smoothing(win_size.get(), testCase.get())).pack(side=TOP, padx=10,
                                                                                                   pady=10)

    Button(root, text='Sharpening', command=lambda: Sharpening()).pack(padx=10, pady=10)

    fold = BooleanVar(value=False)
    Radiobutton(root, text="Fold ?", variable=fold, value=True, command=lambda: fold.get()).pack(padx=10, pady=10)

    tkinter.Label(root, text="Shifting value").pack()

    val = tkinter.Entry(root)
    val.pack(padx=5, pady=5)

    Button(root, text='Shifting & Folding', command=lambda: shifting_and_folding(val.get(), fold.get())).pack(padx=10,
                                                                                                              pady=10)

    Button(root, text='Remove DC', command=lambda: Remove_DC()).pack(padx=10, pady=10)


def folding(index, sample):
    output_index = index
    output_sample = sample[::-1]
    Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_fold.txt', output_index, output_sample)
    return output_index, output_sample


def shifting(k, index, sample):
    # k = -1 * k
    output_index = [x + k for x in index]
    output_sample = sample
    return output_index, output_sample


def shifting_and_folding(k, flag):
    msg = ""
    try:
        k = int(k)
    except:
        msg += "The number Must be an Integer value"

    if msg != "":
        msgbx.showerror(title="Error", message=msg, )
        return

    index, sample = open_file('Signals/Task6/Shifting_and_Folding/input_fold.txt')

    draw_signal(index, sample, "Before")

    if flag:
        index, sample = folding(index, sample)
    output_index, output_sample = shifting(k, index, sample)

    if k == 500:
        Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_ShifFoldedby500.txt', output_index, output_sample)
    elif k == -500:
        Shift_Fold_Signal('Signals/Task6/Shifting_and_Folding/Output_ShiftFoldedby-500.txt', output_index,
                          output_sample)

    draw_signal(index, sample, "After")

    return output_index, output_sample


def firstDerivative(x):
    N = len(x)
    y = [x[0]]  # Initialize y with the first element of x

    for n in range(1, N - 1):
        y_n = x[n] - x[n - 1]
        y.append(y_n)

    return y


def secondDerivative(x):
    N = len(x) - 2
    y = [0] * N

    for n in range(1, N):
        y[n] = x[n + 1] - 2 * x[n] + x[n - 1]

    return y


def Sharpening():
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0,
         21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0,
         39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0,
         57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0,
         75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0,
         93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0]

    # first derivative y(n) = x(n) - x(n-1)
    # first_derivative = np.diff(x, n=1)
    # print("First Derivative: ",first_derivative)

    # second derivative y(n) = x(n+1) - 2*x(n) + x(n-1)
    # second_derivative = np.diff(x, n=2)
    # print("Second Derivative: ",second_derivative)

    # first derivative y(n) = x(n) - x(n-1)
    first_derivative = firstDerivative(x)
    # print("First Derivative: ",first_derivative)

    # second derivative y(n) = x(n+1) - 2*x(n) + x(n-1)
    second_derivative = secondDerivative(x)
    # print("Second Derivative: ",second_derivative)

    DerivativeSignal(first_derivative, second_derivative)

    # Plot the input signal and its derivatives
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(x, marker='o')
    plt.title('Input Signal')

    plt.subplot(3, 1, 2)
    plt.plot(first_derivative, marker='o', color='orange')
    plt.title('First Derivative')

    plt.subplot(3, 1, 3)
    plt.plot(second_derivative, marker='o', color='green')
    plt.title('Second Derivative')

    plt.tight_layout()
    plt.show()


def moving_average(x, window_size):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[window_size:].astype(float) - cumsum[:-window_size].astype(float)) / window_size


def Smoothing(win_size, testCase):
    msg = ""
    try:
        win_size = int(win_size)
        if win_size == 0 or win_size % 2 == 0:
            raise ValueError
    except:
        msg += "The number Must be an Odd value and not 0"

    try:
        testCase = int(testCase)
        if testCase == 0:
            raise ValueError
    except:
        msg += "\nPlease select a signal"

    if msg != "":
        msgbx.showerror(title="Error", message=msg, )
        return

    if testCase == 1:  # Test 1:
        index, sample = open_file('Signals/Task2/input signals/Signal1.txt')
        # print(sample)
        output = moving_average(sample, win_size)
        # print(output)
        file_name = 'Signals/Task6/Moving Average/OutMovAvgTest1.txt'

    elif testCase == 2:
        index, sample = open_file('Signals/Task2/input signals/Signal2.txt')
        # print(sample)
        output = moving_average(sample, win_size)
        # print(output)
        file_name = 'Signals/Task6/Moving Average/OutMovAvgTest2.txt'

    SignalSamplesAreEqual(file_name, output)


def Remove_DC():
    index, sample = open_file('Signals/Task5/Remove DC component/DC_component_input.txt')
    # print("Samples: ",sample)
    amp, phase = I_DFT(sample, 0, False, 6)
    amp[0] = 0
    phase[0] = 0
    # print("Amp: ",amp)
    # print("Phase: ",phase)
    new_index, new_sample = I_DFT([], 0, True,6,amp, phase)
    # print("New Samples: ",new_sample)

    SignalSamplesAreEqual('Signals/Task5/Remove DC component/DC_component_output.txt', new_sample)
