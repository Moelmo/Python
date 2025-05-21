import tkinter as tk
from tkinter import messagebox

# Data produk (bisa diganti sesuai kebutuhan)
produk = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Es Teh": 5000,
    "Jus Alpukat": 10000
}

keranjang = {}

def tambah_produk(nama):
    if nama in keranjang:
        keranjang[nama] += 1
    else:
        keranjang[nama] = 1
    tampilkan_keranjang()

def tampilkan_keranjang():
    text_keranjang.delete("1.0", tk.END)
    total = 0
    for nama, jumlah in keranjang.items():
        harga = produk[nama] * jumlah
        total += harga
        text_keranjang.insert(tk.END, f"{nama} x{jumlah} = Rp{harga}\n")
    text_keranjang.insert(tk.END, f"\nTotal: Rp{total}")
    label_total.config(text=f"Total: Rp{total}")
    entry_bayar.delete(0, tk.END)
    label_kembalian.config(text="Kembalian: Rp0")

def hitung_kembalian():
    try:
        bayar = int(entry_bayar.get())
        total = sum(produk[nama] * jumlah for nama, jumlah in keranjang.items())
        if bayar < total:
            messagebox.showwarning("Kurang!", "Uang tidak cukup!")
        else:
            kembalian = bayar - total
            label_kembalian.config(text=f"Kembalian: Rp{kembalian}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah uang yang valid!")

def reset():
    keranjang.clear()
    tampilkan_keranjang()
    label_kembalian.config(text="Kembalian: Rp0")

# GUI
window = tk.Tk()
window.title("Aplikasi Kasir Sederhana")
window.geometry("500x500")

frame_produk = tk.LabelFrame(window, text="Daftar Produk", padx=10, pady=10)
frame_produk.pack(padx=10, pady=10, fill="x")

for nama, harga in produk.items():
    btn = tk.Button(frame_produk, text=f"{nama} - Rp{harga}", command=lambda n=nama: tambah_produk(n))
    btn.pack(fill="x", pady=2)

frame_keranjang = tk.LabelFrame(window, text="Keranjang", padx=10, pady=10)
frame_keranjang.pack(padx=10, pady=10, fill="both", expand=True)

text_keranjang = tk.Text(frame_keranjang, height=10)
text_keranjang.pack(fill="both")

label_total = tk.Label(window, text="Total: Rp0", font=("Arial", 12, "bold"))
label_total.pack()

frame_bayar = tk.Frame(window)
frame_bayar.pack(pady=10)

tk.Label(frame_bayar, text="Uang Bayar: Rp").pack(side="left")
entry_bayar = tk.Entry(frame_bayar)
entry_bayar.pack(side="left")

btn_hitung = tk.Button(window, text="Hitung Kembalian", command=hitung_kembalian)
btn_hitung.pack(pady=5)

label_kembalian = tk.Label(window, text="Kembalian: Rp0", font=("Arial", 12, "bold"))
label_kembalian.pack()

btn_reset = tk.Button(window, text="Reset", command=reset)
btn_reset.pack(pady=5)

window.mainloop()
