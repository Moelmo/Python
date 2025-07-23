import socket
import threading

def recive_msg(client_socket):
    """Menerima pesan dari server"""
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("[ERROR] Disconnected from server.")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # thread untuk menerima pesan
    recive_thread = threading.Thread(target=recive_msg, args=(client,))
    recive_thread.start()

    while True:
        msg = input("")
        if msg.lower() == "q":
            client.close()
            break
        client.send(msg.encode('utf-8'))

if __name__ == "__main__":
    print("[CLIENT] Connection to server")
    start_client()