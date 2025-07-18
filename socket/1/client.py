import socket 

# crate socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# kondisi server
client_socket.connect(('localhost', 12345))

# Terima data
data = client_socket.recv(1024)
print("Dari server:", data.decode())

# kirim balasan
client_socket.sendall(b"Halo juga dari client!")

# tutup koneksi
client_socket.close()