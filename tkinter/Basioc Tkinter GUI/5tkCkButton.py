from tkinter import *

r = Tk()
v = IntVar()
Radiobutton(r, text="ASWD", variable=v, value=1).pack(anchor=W)
Radiobutton(r, text="AKMS", variable=v, value=2).pack(anchor=W)
mainloop()