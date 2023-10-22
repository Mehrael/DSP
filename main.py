from Task1 import *

root = Tk()
root.title('Main Screen')
root.geometry('300x450')


btn= Button(root, text='Discrete & Continuous Signals',command=lambda :part1())
btn.pack(side=TOP,padx=10,pady=10 )

btn2=Button(root,text='Discrete Signal',command=lambda :part2())
btn2.pack(side=TOP, padx=20, pady=20)

mainloop()