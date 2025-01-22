import socket
from multiprocessing import Process


def handle_client(client_socket, address):
    print(f"[INFO] Connection established with {address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[INFO] Received from {address}: {data.decode('utf-8')}")
            client_socket.sendall(data)
    except Exception as e:
        print(f"[ERROR] Connection with {address} closed due to error: {e}")
    finally:
        print(f"[INFO] Closing connection with {address}")
        client_socket.close()


def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"[INFO] Server listening on {server_ip}:{server_port}")

    try:
        while True:
            client_socket, address = server.accept()
            process = Process(target=handle_client, args=(client_socket, address))
            process.start()
            client_socket.close()
    except KeyboardInterrupt:
        print("\n[INFO] Server shutting down.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
