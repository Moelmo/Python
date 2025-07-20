import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")
        self.master.geometry("400x500")

        # GUI

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill='both', expand=True)

        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=(0,10), fill='x')
        self.entry.bind("<Return>", self.kirim_pesan)

        self.send_button = tk.Button(master, text="Kirim", command=self.kirim_pesan)
        self.send_button.pack(padx=10, pady=(0,10), fill='x')

        # socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 12345))

        # masukkan nama mu
        self.nama = tk.simpledialog.askstring("Nama", "Masukkan nama Anda:")
        if not self.nama:
            self.master.destroy()
            return
        self.client.send(f"{self.nama} telah bergabung ke chat!".encode())

        # Thread
        threading.Thread(target=self.terima_pesan, daemon=True).start()

    def tampilkan_pesan(self, pesan):
        self.chat_area.configure(state='normal')
        self.chat_area.insert('end', pesan + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.yview('end')

    def kirim_pesan(self, event=None):
        teks = self.entry.get()
        if teks:
            pesan = f"{self.nama}: {teks}"
            self.client.send(pesan.encode())
            self.entry.delete(0, 'end')

    def terima_pesan(self):
        while True:
            try:
                pesan = self.client.recv(1024).decode()
                if not pesan:
                    break
                self.tampilkan_pesan(pesan)
            except:
                break

# jalankan gui
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()