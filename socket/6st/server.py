import socket 
import threading

# data user
clients = []

def handle_client(client_socket, address):
    """Menangani komunikasi dengan satu client"""
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        try:
            # menerima pesan dari client
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                break

            print(f"[{address} : {msg}]")

            broadcast(msg, client_socket)
        except:
            # jika terjadi error, hapus client dari list
            print(f"[DISCONNECTED] {address} disconnected.")
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(msg, sender_socket):
    """Mengirim pesan ke semua client kecuali pengirim"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msg.decode('utf-8'))
            except:
                #jika gagal mengirim, hapus cient yang bermasalah
                clients.remove(client)
                client.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 5555))
    s.listen()
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, address = s.accept()
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket, address))

        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()