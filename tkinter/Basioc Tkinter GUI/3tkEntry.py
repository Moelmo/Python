from tkinter import *

r = Tk()
Label(r, text="Nama depan").grid(row=0)
Label(r, text="Nama belakang").grid(row=1)
e1 = Entry(r)
e2 = Entry(r)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()