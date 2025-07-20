import socket
import threading

def terima_pesan(client):
    while True:
        try:
            data = client.recv(1024).decode()
            if not data or data.lower() == "exit":
                print("\nServer Keluar")
                break
            print("\nServer: ", data)
        except:
            break

def kirim_pesan(client):
    while True:
        try:
            pesan = input("Client: ")
            client.sendall(pesan.encode())
            if pesan.lower() == "exit":
                break
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

threading.Thread(target=terima_pesan, args=(client,)).start()
threading.Thread(target=kirim_pesan, args=(client,)).start()