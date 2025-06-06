from tkinter import *

r = Tk()
scrollbar = Scrollbar(r)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(r, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, "This is line number" + str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()