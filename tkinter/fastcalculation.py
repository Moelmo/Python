import time
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# scirpt
def quit():
    pilihan = messagebox.askyesno("Keluar", "Anda Ingin Keluar?")
    if pilihan:
        root.destroy()

def singleplayer():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)

def sing_back():
    frame2.pack_forget()
    frame1.pack(fill="both", expand=True)

# GUI
root  = tk.Tk()
root.title("Simple Game")
root.geometry("400x300")
root.configure(bg="#1e1e2f")
root.resizable(False,False)

# frame mainmenu (frame1)

frame1 = tk.Frame(root, bg="#1e1e2f")

judul = tk.Label(frame1, text="Fast Calculation", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
judul.pack(pady=20)

btn_singleplayer = tk.Button(frame1, text="SinglePlayer", width=15, height=1, activebackground="green", activeforeground="white", command=singleplayer)
btn_singleplayer.pack(pady=5)

btn_multiplayer = tk.Button(frame1, text="MultiPlayer", width=15, height=1, activebackground="green", activeforeground="white")
btn_multiplayer.pack(pady=5)

btn_quit = tk.Button(frame1, text="Quit Dekstop", width=15, height=1, activebackground="red", activeforeground="white", command=quit)
btn_quit.pack(pady=5)

frame1.pack(fill="both", expand=True)

# ======================================
# Halaman singleplayer
frame2 = tk.Frame(root, bg="#263238")

sig_title = tk.Label(frame2, text="SinglePlayer", bg="#263238", fg="white", font=("Arial", 16, "bold"))
sig_title.pack(pady=20)

sig_quit = tk.Button(frame2, text="Back", width=15, height=1, activebackground="red", activeforeground="white", command=sing_back)
sig_quit.pack(pady=5)

root.mainloop()