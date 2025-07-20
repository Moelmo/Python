import socket
import threading

# Konfigurasi server
HOST = '127.0.0.1'
PORT = 5555

# List untuk menyimpan client yang terhubung
clients = []

# Fungsi untuk mengirim pesan ke semua client
def broadcast(pesan, pengirim_socket):
    for client in clients:
        if client != pengirim_socket:
            try:
                client.send(pesan)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Fungsi untuk handle setiap client
def handle_client(client_socket):
    while True:
        try:
            pesan = client_socket.recv(1024)
            if not pesan:
                break
            print("Pesan diterima:", pesan.decode())
            broadcast(pesan, client_socket)
        except:
            break

    client_socket.close()
    if client_socket in clients:
        clients.remove(client_socket)

# Fungsi utama untuk menerima koneksi client
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server berjalan di {HOST}:{PORT}...")

    while True:
        client_socket, addr = server.accept()
        print(f"Terhubung dengan {addr}")
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    main()
