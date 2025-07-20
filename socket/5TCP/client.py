import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def client_connect():
    global attemp 
    attemp = 0
    while True:
        try:
            s.connect(('localhost', 12345))
            print("Berhasil terhubung dengan server")
            client()
        except:
            if attemp < 5:
                print("Gagal terhubung dengan server....")
                attemp += 1
                time.sleep(1)
                print("Mencoba terhubung dengan server...")
            else:
                print("Gagal terhubung dengan server....")
                break

def client():
    global attemp
    while True:
        msg = input("Kirim : ")
        s.send(msg.encode())
        if msg.lower() == "exit":
            print("Terputus dari server")
            attemp  = 6
            break
        reply = s.recv(1024).decode()
        print("Server : ", reply)

client_connect()
s.close()