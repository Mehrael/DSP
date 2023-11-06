import re
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt


def draw_signal(index, sample, text):

    fig, axs = plt.subplots(1, 2)
    fig.suptitle(text, fontsize=30)
    axs[0].set_title('Discrete Signal')
    for (i, j) in zip(index, sample):
        axs[0].plot([i, i], [0, j], color='red')

    axs[0].scatter(index, sample)
    axs[0].axhline(0, color='black', linewidth=0.5)
    axs[0].axvline(0, color='black', linewidth=0.5)
    axs[0].set_xlabel('No. of Samples')
    axs[0].set_ylabel('Amplitude')

    axs[1].plot(index, sample)
    axs[1].set_title('Continuous Signal')
    axs[1].axhline(0, color='black', linewidth=0.5)
    axs[1].axvline(0, color='black', linewidth=0.5)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Amplitude')
    plt.show()
    return


def open_file(path: object = None) -> object:
    signalType = None
    isPeriodic = None
    N = 0
    index = []
    sample = []
    if path is not None:
        file=open(path, 'r')
    else:
        file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        content = file.readlines()
        for i, x in enumerate(content):
            if i == 0 and int(x) == 0:
                signalType = 0
                continue
            elif i == 0 and int(x) == 1:
                signalType = 1
                continue
            if i == 1 and int(x) == 0:
                isPeriodic = False
                continue
            elif i == 1 and int(x) == 1:
                isPeriodic = True
                continue
            if i == 2:
                N = int(x)
                continue
            x = x.split()
            index.append(int(x[0]))
            sample.append(float(x[1]))

    # print("ImpFunctions: ", len(sample))

    return index, sample


def special_open_file(special='',path: object = None) -> object:
    signalType = None
    isPeriodic = None
    N = 0
    index = []
    sample = []
    if path is not None:
        file=open(path, 'r')
    else:
        file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        content = file.readlines()
        for i, x in enumerate(content):
            if i == 0 and int(x) == 0:
                signalType = 0
                continue
            elif i == 0 and int(x) == 1:
                signalType = 1
                continue
            if i == 1 and int(x) == 0:
                isPeriodic = False
                continue
            elif i == 1 and int(x) == 1:
                isPeriodic = True
                continue
            if i == 2:
                N = int(x)
                continue
            x = x.split(special)
            index.append(float(re.sub(r'[^\d.-]', '', x[0])))
            sample.append(float(re.sub(r'[^\d.-]', '', x[1])))

    # print("ImpFunctions: ", len(sample))

    return index, sample

def write_file(file_name, first_3_lines, list1, list2):
    with open(file_name, "w") as file:
        file.write(first_3_lines)

        for num1, num2 in zip(list1, list2):
            file.write(f"\n{num1} {num2}")

    print(f"File '{file_name}' has been created with the specified content.")