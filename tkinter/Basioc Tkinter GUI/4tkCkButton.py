from tkinter import *

r = Tk()
var1 = IntVar()
Checkbutton(r, text="lanang", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(r, text="Cwk", variable=var2).grid(row=1, sticky=W)

tes1 = IntVar()
Checkbutton(r, text="tes1", variable=tes1).grid(row=3, sticky=W)
tes2 = IntVar()
Checkbutton(r, text="tes2", variable=tes2).grid(row=4, sticky=W)
mainloop()