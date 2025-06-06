import tkinter as tk

r = tk.Tk()
r.title("Tombol Pack")

# bikin tombol
btn1 = tk.Button(r, text="Tombo1")
btn2 = tk.Button(r, text="Tombo2")
btn3 = tk.Button(r, text="Tombo3")

# munculakn btn

btn1.pack()
btn2.pack()
btn3.pack()

r.mainloop()