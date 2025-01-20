# client.py
import socket
import threading

HOST = '127.0.0.1'  # Server address
PORT = 12345        # Server port

def receive_messages(client):
    """Receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def send_messages(client):
    while True:
        message = input()
        client.send(message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    threading.Thread(target=receive_messages, args=(client,)).start()
    threading.Thread(target=send_messages, args=(client,)).start()

if __name__ == "__main__":
    start_client()
