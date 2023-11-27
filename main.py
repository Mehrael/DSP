from Task1 import *
from Task2 import *
from Task3 import *
from Task4 import *
from Task6 import *

root = Tk()
root.title('Main Screen')
root.geometry('300x450')
arth_op = StringVar()

Button(root, text='Discrete & Continuous Signals', command=lambda: part1()).pack(side=TOP, padx=10, pady=10)

Button(root, text='Discrete Signal', command=lambda: part2()).pack(side=TOP, padx=10, pady=10)

options = [
    "Select an Operation",
    "Addition",
    "Subtraction",
    "Multiplication",
    "Squaring",
    "Shifting",
    "Normalization",
    "Accumulation"
]

OptionMenu(root, arth_op, *options).pack(side=TOP, padx=10, pady=5)

Button(root, text='Signals with Arithmatic Operations', command=lambda: set_op(arth_op.get())).pack(side=TOP, padx=10, pady=10)

Button(root, text='Quantization', command=lambda: screen()).pack(side=TOP, padx=10, pady=10)

Button(root, text='Frequency Domain', command=lambda: Task4_screen()).pack(side=TOP, padx=10, pady=10)

Button(root, text='Time Domain', command=lambda: Task6_screen()).pack(side=TOP, padx=10, pady=10)


mainloop()
# print(len(sample_signal[0]))
# print(len(sample))
# print(min(sample))
# print("Sample:")
# print(sample)
# print('Interval Start:')
# print(interval_start)
# print('Interval End:')
# print(interval_end)
# print('Interval Midpoint:')
# print(interval_midpoint)
# print('-------------------------------')
# print('Quantized Signal:')
# print(quantized)
# print('Encoded index:')
# print(encoded)
# print('Interval Index:')
# print(interval_index)
# print('Error:')
# print(error)