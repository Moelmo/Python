import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))

print('Menunggu terhubung dengan client...')
s.listen(1)
conn, addr = s.accept()
print(f"Terkoneksi dengan {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Client Kelaur")
        break
    print("Dari Client: ", data)
    reply = input("Balas : ")
    conn.send(reply.encode())

conn.close()