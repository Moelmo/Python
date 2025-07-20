import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

while True:
    # kirim pesan ke server
    pesan = input("Client2: ")
    client.sendall(pesan.encode())
    if pesan.lower() == "exit":
        break

    # terima balsan dari server
    data = client.recv(1024).decode()
    if data.lower() == "exit":
        print("Server keluar.")
        break
    print("Server:", data)

client.close()