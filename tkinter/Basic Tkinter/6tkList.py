from tkinter import *

r = Tk()
Lb = Listbox(r)
Lb.insert(1, "Python")
Lb.insert(2, "JavaScript")
Lb.insert(3, "C++")
Lb.insert(4, "PHP")
Lb.pack()
r.mainloop()