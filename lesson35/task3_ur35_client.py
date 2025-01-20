import socket


def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    print(f"[INFO] Connected to server at {server_ip}:{server_port}")

    try:
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                print("[INFO] Exiting client.")
                break
            client.sendall(message.encode('utf-8'))
            data = client.recv(1024)
            print(f"[INFO] Received from server: {data.decode('utf-8')}")
    except Exception as e:
        print(f"[ERROR] Client encountered an error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    main()
