import tkinter as tk
from tkinter import *
import time

r = tk.Tk()
r.title("Kalkulator")

def klik_angka(nilai):
    widow.insert(END, nilai)

def hapus_satu():
    current = widow.get()
    widow.delete(0, END)
    widow.insert(END, current[:-1])

def hapus_semua():
    widow.delete(0, END)

def jumlah():
    try:
        hasil = eval(widow.get())
        widow.delete(0, END)
        widow.insert(END, str(hasil))
    except:
        widow.delete(0, END)
        widow.insert(END, "Error")

widow = Entry(r)
widow.grid(row=0, column=0, columnspan=5)

btn1 = tk.Button(r, text="1", width=5, command=lambda val=1: klik_angka(val))
btn2 = tk.Button(r, text="2", width=5, command=lambda val=2: klik_angka(val))
btn3 = tk.Button(r, text="3", width=5, command=lambda val=3: klik_angka(val))
btn4 = tk.Button(r, text="4", width=5, command=lambda val=4: klik_angka(val))
btn5 = tk.Button(r, text="5", width=5, command=lambda val=5: klik_angka(val))
btn6 = tk.Button(r, text="6", width=5, command=lambda val=6: klik_angka(val))
btn7 = tk.Button(r, text="7", width=5, command=lambda val=7: klik_angka(val))
btn8 = tk.Button(r, text="8", width=5, command=lambda val=8: klik_angka(val))
btn9 = tk.Button(r, text="9", width=5, command=lambda val=9: klik_angka(val))
btnh = tk.Button(r, text="C", width=5, command=hapus_semua)
btn0 = tk.Button(r, text="0", width=5, command=lambda val=0: klik_angka(val))
btnc = tk.Button(r, text="<", width=5, command=hapus_satu)
btnplus = tk.Button(r, text="+", width=5, command=lambda val="+": klik_angka(val))
btnmin = tk.Button(r, text="-", width=5, command=lambda val="-": klik_angka(val))
btnkali = tk.Button(r, text="X", width=5, command=lambda val="*": klik_angka(val))
btnbagi = tk.Button(r, text=":", width=5, command=lambda val="/": klik_angka(val))
btnjumlah = tk.Button(r, text="Jumalah", width=25, command=jumlah)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btnh.grid(row=4, column=0)
btn0.grid(row=4, column=1)
btnc.grid(row=4, column=2)
btnplus.grid(row=1, column=3)
btnmin.grid(row=2, column=3)
btnkali.grid(row=3, column=3)
btnbagi.grid(row=4, column=3)
btnjumlah.grid(row=5, column=0, columnspan=5)



# Update dulu agar ukuran widget dihitung
r.update_idletasks()

# Dapatkan ukuran aktual jendela
window_width = r.winfo_width()
window_height = r.winfo_height()

# Hitung posisi agar jendela muncul di tengah layar
screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Pindahkan ke tengah
r.geometry(f"+{x}+{y}")

r.mainloop()
