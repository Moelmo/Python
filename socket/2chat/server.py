import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Menunggu koneksi dari client...")
conn, addr = server.accept()
print(f"Terhubung dengan {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "exit":
        print("Client keluar.")
        break
    print("Client: ", data)

    # kirim balsan ke client
    balasan  = input("Server: ")
    conn.sendall(balasan.encode())
    if balasan.lower() == "exit":
        break

conn.close()
server.close()