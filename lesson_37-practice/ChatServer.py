# server.py
import socket
import threading


HOST = '127.0.0.1'
PORT = 12345

# Store connected clients and their usernames
clients = {}

def broadcast(message, sender=None):

    for client, username in clients.items():
        if client != sender:
            client.send(message)

def handle_client(client):
    client.send(b"Welcome to the chat! Type /rename <name> to set your username.\n")
    username = f"Client{len(clients)}"
    clients[client] = username
    broadcast(f"{username} has joined the chat!\n".encode('utf-8'))

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message.startswith('/rename '):
                new_username = message.split(' ', 1)[1].strip()
                if new_username in clients.values():
                    client.send(b"Username already taken. Please choose another.\n")
                else:
                    old_username = clients[client]
                    clients[client] = new_username
                    broadcast(f"{old_username} is now known as {new_username}\n".encode('utf-8'))
            else:
                broadcast(f"{clients[client]}: {message}\n".encode('utf-8'), sender=client)
        except:
            # Remove client if connection is lost
            client.close()
            username = clients.pop(client)
            broadcast(f"{username} has left the chat.\n".encode('utf-8'))
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    start_server()
