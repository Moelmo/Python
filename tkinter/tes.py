import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Game Stats")
root.geometry("300x200")

# Membuat frame untuk kotak stats
frame_stats = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10, bg="white")
frame_stats.pack(pady=20)

# Label judul
label_title = tk.Label(frame_stats, text="Stats", font=("Arial", 14, "bold"), bg="white")
label_title.pack(anchor="w")

# Label score
label_score = tk.Label(frame_stats, text="Score: 0", font=("Arial", 12), bg="white")
label_score.pack(anchor="w", pady=5)

# Bisa ditambahkan statistik lainnya
label_health = tk.Label(frame_stats, text="Health: 100%", font=("Arial", 12), bg="white")
label_health.pack(anchor="w", pady=5)

root.mainloop()
