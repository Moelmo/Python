import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # simulasi progres
    for i in range(101):
        time.sleep(0.10)
        progress['value'] = i
        # gui update
        r.update_idletasks()
    progress.stop()

r = tk.Tk()
r.title("Progresbar")

# jendela 
progress = ttk.Progressbar(r, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# tombol buat mulai
start_btn = tk.Button(r, text="Mulai", command=start_progress)
start_btn.pack(pady=20)

r.mainloop()