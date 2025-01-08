import socket

def start_client_tcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        original_message = input("Message: ")
        shift = input("Write a shift(only integers that are positive): ")
        if not shift.isdigit():
            raise ValueError("Shift must be an integer.")
        language = input("Pick language... (eng or ukr): ")
        if language.lower() != "eng" and language.lower() != "ukr":
            raise ValueError("Language must be eng or ukr.")
        data = f"{original_message}|{shift}|{language.lower()}"
        client_socket.sendall(data.encode())
        response = client_socket.recv(1024)
        print(f"Echo from server: {response.decode()}")


if __name__ == "__main__":
    start_client_tcp("127.0.0.1", 65432)