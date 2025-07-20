import socket
import threading

def terima_pesan(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or data.lower() == "exit":
                print("Client keluar.")
                break
            print("\nClient: ", data)
        except:
            break

def kirim_pesan(conn):
    while True:
        try:
            pesan =  input("Server :")
            conn.sendall(pesan.encode())
            if pesan.lower() == "exit":
                break
        except:
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Menunggu koneksi dari client...")
conn, addr = server.accept()
print(f"Terhubung dengan {addr}")

threading.Thread(target=terima_pesan, args=(conn,)).start()
threading.Thread(target=kirim_pesan, args=(conn,)).start()