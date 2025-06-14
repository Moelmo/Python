import random
import tkinter as tk

r = tk.Tk()
r.title("Game tambah tambahan")

# widget global 
soal_label = tk.Label(r)
hasil_label = tk.Label(r)
jawaban = tk.Entry(r, width=20)
framejawaban = tk.Frame(r)

# global variable
hasilb = 0
score = 0
B = 0
S = 0

def jumlahkan(nilai):
    global hasilb, score, B, S
    jawaban.delete(0, tk.END)
    if int(nilai) == hasilb:
        jawaban.insert(0, "Benar")
        score += 1
        B += 1
    else:
        jawaban.insert(0, "Salah")
        score -= 1
        S += 1
    r.after(800, reset)

def reset():
    global hasilb, score, B, S
    a = random.randint(1,10)
    b = random.randint(1,10)
    a1 = random.randint(1,10)
    b1 = random.randint(1,10)

    hasilb = a + b 
    pilihan = [str(hasilb), str(a + a1), str(b + b1)]
    random.shuffle(pilihan)
    soal_label.config(text=f"{a} + {b} = ...")
    hasil_label.config(text=f"Score : {score} | B/S : [{B}/{S}]")
    jawaban.delete(0, tk.END)

    for widget in framejawaban.winfo_children():
        widget.destroy()

    for p in pilihan:
        btn = tk.Button(framejawaban, text=p, width=5, command=lambda val=p: jumlahkan(val))
        btn.pack(side="left", padx=5)

# UI
tk.Label(r,text="Game tambah tambahan pilihan ganda").pack(pady=10)
tk.Label(r, text="Soal :  pilihlah jawaban yang benar").pack()
hasil_label.pack(padx=5)
soal_label.pack(padx=5)

jawaban.pack(pady=5)
framejawaban.pack(padx=10)

reset()
r.mainloop()