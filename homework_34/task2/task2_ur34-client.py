import socket

def start_client_tcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("Message: ")
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print(f"Echo from server: {response.decode()}")

if __name__ == "__main__":
    start_client_tcp("127.0.0.1", 65432)
