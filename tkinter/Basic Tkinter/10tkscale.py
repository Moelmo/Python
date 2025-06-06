from tkinter import *

r = Tk()
w = Scale(r, from_=0, to=42)
w.pack()
w = Scale(r, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()