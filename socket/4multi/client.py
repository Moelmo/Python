import socket
import threading

def terima_pesan(cliet):
    while True:
        try:
            pesan = client.recv(1024)
            if not pesan:
                break
            print("\n" + pesan.decode())
        except:
            break

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

nama = input("Masukkan nama Anda: ")
client.send(f"{nama} telah begabung ke chat!".encode())

threading.Thread(target=terima_pesan, args=(client,), daemon=True).start()

while True:
    teks = input()
    if teks.lower() == "exit":
        client.send(f"{nama} keluar dari chat.".encode())
        break
    client.send(f"{nama}: {teks}".encode())

client.close()