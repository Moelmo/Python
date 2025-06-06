from tkinter import *

top = Tk()
mb = Menubutton (top, text="MOELMO")
mb.grid()
mb.menu = Menu (mb, tearoff=0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton (label = "kontak", variable= cVar)
mb.menu.add_checkbutton (label = "tentang",variable= aVar)
mb.pack()
top.mainloop()