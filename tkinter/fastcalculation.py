import time
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# global data
name = "Moelmo"
score = 0
high_score = 0 
last_score = 0
dificulty = None #default
hitung_mundur = 0

# scirpt
def quit():
    pilihan = messagebox.askyesno("Keluar", "Anda Ingin Keluar?")
    if pilihan:
        root.destroy()

def singleplayer():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)

def singleplayer_mode():
    frame2.pack_forget()
    singleplayer_mode.pack(fill="both", expand=True)
    hitung_mundur()

def hitung_mundur():
    global hitung_mundur
    hitung_mundur = 3
    # time.sleep(1)
    # while hitung_mundur == 0:
    #     hitung_mundur =- 1

    sing_hitung_mulai.pack(pady=1)

def sing_back():
    frame2.pack_forget()
    frame1.pack(fill="both", expand=True)

def setting():
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)

def quit_sing():
    frame3.pack_forget()
    singleplayer_mode.pack_forget()
    frame2.pack(fill="both", expand=True)

def multiplayer():
    messagebox.showwarning("Not Implemented", "Multiplayer mode is not implemented yet.")

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

btn_multiplayer = tk.Button(frame1, text="MultiPlayer", width=15, height=1, activebackground="green", activeforeground="white", command=multiplayer)
btn_multiplayer.pack(pady=5)

btn_quit = tk.Button(frame1, text="Quit Dekstop", width=15, height=1, activebackground="red", activeforeground="white", command=quit)
btn_quit.pack(pady=5)

frame1.pack(fill="both", expand=True)

# =================================
# setting frame
frame3 = tk.Frame(root, bg="#4a4a57")
judul_setting = tk.Label(frame3, text="Setting", font=("Arial", 16, "bold"), bg="#4a4a57", fg="white")
judul_setting.pack(pady=20)

btn_quit_setting = tk.Button(frame3, text="Back", width=15, height=1, activebackground="red", activeforeground="white", command=quit_sing)
btn_quit_setting.pack(pady=20)

# ======================================
# Halaman singleplayer and stats
frame2 = tk.Frame(root, bg="#263238")
sig_title = tk.Label(frame2, text="SinglePlayer", bg="#263238", fg="white", font=("Arial", 16, "bold"))
sig_title.pack(pady=20)

sig_name = tk.Label(frame2, text=f"{name}", bg="#263238", fg="white", font=("Arial", 10, "bold"))
sig_name.pack(pady=1)

# scoreboard
sig_stats = tk.Label(frame2, text=f"Score : {score}\nDificulty: {dificulty}", bd=2, relief="groove", width=15, bg="white", font=("Arial", 8))
sig_stats.pack(pady=1)

start_sig = tk.Button(frame2, text="Start", width=15, height=1, activebackground="green", activeforeground="white", command=singleplayer_mode)
start_sig.pack(pady=1)

# setting
sig_setting = tk.Button(frame2, text="Setting", width=15, height=1, activebackground="green", activeforeground="white", command=setting)
sig_setting.pack(pady=1)

sig_quit = tk.Button(frame2, text="Back", width=15, height=1, activebackground="red", activeforeground="white", command=sing_back)
sig_quit.pack(pady=5)

# mulai game singleplayer mode
singleplayer_mode = tk.Frame(root, bg="#B9B9B9")

sing_mode_judul = tk.Label(singleplayer_mode, text="Fast Calculate", font=("Arial", 15, "bold"), background="#B9B9B9")
sing_mode_judul.pack(pady=20)

sing_hitung_mulai = tk.Label(singleplayer_mode, text=f"{hitung_mundur}", font=("Arial", 25, "bold"), background="#B9B9B9")

sing_mode_quit = tk.Button(singleplayer_mode, text="Back", width=15, height=1, activebackground="red", activeforeground="white", command=quit_sing)
sing_mode_quit.pack(pady=5)


root.mainloop()