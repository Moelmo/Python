import socket
import threading

# data user
clients = []

def broadcast(pesan, pengirim):
    for client in clients:
        if client != pengirim:
            try:
                client.send(pesan)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            pesan = client.recv(1024)
            if not pesan:
                break
            print(f"Pesan diterima: {pesan.decode()}")
            broadcast(pesan, client)
        except:
            break

    print("Client terputus.")
    clients.remove(client)
    client.close()    

# setup socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

print("Server aktif. Menunggu client...")

while True:
    client_socket, addr = server.accept()
    print(f"Client terhubung dari {addr}")
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()