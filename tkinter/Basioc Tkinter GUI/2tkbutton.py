import tkinter as tk

r = tk.Tk()
r.title("Button")
button = tk.Button(r, text="Stop", width=25, command=r.destroy)
button.pack()
r.mainloop()
