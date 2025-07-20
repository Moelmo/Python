# Server TCP Dasar
import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
conn, addr = s.accept()
print(f"Terkoneksi dari {addr}")
data = conn.recv(1024).decode()
print("Dari client: ", data)
conn.close()