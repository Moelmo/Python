import tkinter as tk 

r = tk.Tk()
r.title("contoh grid")

l1 = tk.Label(r, text="hai")
l2 = tk.Label(r, text="aku")
l3 = tk.Label(r, text="Moelmo")

l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
l3.grid(row=1, column=0, columnspan=2)

r.mainloop()