import tkinter as tk 

r = tk.Tk()
r.title("Color options in tkinter")

# tambah button
btn = tk.Button(r, text="Pencet aku", activebackground="aqua", activeforeground="white")
btn.pack()

# crate label tambah bg
label = tk.Label(r, text="Hallo Moelmo", bg="lightgray", fg="black")
label.pack()

# tambah entry jendela pilih warna
e = tk.Entry(r, selectbackground="lightblue", selectforeground="lightblue")
e.pack()

r.mainloop()