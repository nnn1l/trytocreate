import socket
import threading

def handle_tcp_client(client_socket, client_addr):
    print(f"Connected with {client_addr}")
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received {data.decode()} from {client_addr}")
            client_socket.sendall(f"Server response: {data.decode()}".encode())

def start_server_tcp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Socket listening on {host}:{port}")
        while True:
            client_socket, client_addr = server_socket.accept()
            threading.Thread(target=handle_tcp_client, args=(client_socket, client_addr)).start()

if __name__ == "__main__":
    start_server_tcp()