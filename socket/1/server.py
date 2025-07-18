import socket

# membuat socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind ke ip port
server_socket.bind(('localhost', 12345))

# Tunggu terhubung
server_socket.listen(1)
print("Menunggu koneksi dari client")

# Terima koneksi
client_socket, client_address = server_socket.accept()
print(f"Terhubung dengan {client_address}")

# kirim dan terima data
client_socket.sendall(b"Hallo dari server!")

# close
client_socket.close()
server_socket.close()