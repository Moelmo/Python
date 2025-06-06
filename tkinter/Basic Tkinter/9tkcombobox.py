import tkinter as tk
from tkinter import ttk

def pilih(ev):
    pilih_item = combo_box.get()
    label.config(text="Pilih Item: " + pilih_item)

r = tk.Tk()
r.title("Combobox Example")

# buat label
label = tk.Label(r, text="Pilih Item: ")
label.pack(pady=10)

# buat jendela
combo_box = ttk.Combobox(r, values=["Aku", "Dia", "Kamu"])
combo_box.pack(pady=5)

# set default
combo_box.set("Aku")

r.mainloop()
