import  socket


def ceaser(message, shift, language):
    coded = ""
    if language == "eng":
        alphabet = 26
    else:
        alphabet = 33

    for char in message:
        if char.isalpha(): #checks if char is a letter
            if char.isupper(): #checks if char is a BIG
                coded += chr((ord(char) + shift - 65) % alphabet + 65)
            else: #checks if a char is small
                coded += chr((ord(char) + shift - 97) % alphabet + 97)
        else:
            coded += char
    return coded


def start_server_tcp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: # TCP
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Socket listening on {host}:{port}")

        connection, addr = server_socket.accept()
        with connection:
            print(f"Connected with Client({addr})")
            while True:
                data = connection.recv(1024)
                try:
                    original_message, shift, language = data.decode().split("|")
                    shift = int(shift)  # Convert shift back to integer
                except ValueError:
                    connection.sendall("Invalid data received.".encode())
                    continue
                if not original_message:
                    break
                coded_message = ceaser(original_message, shift, language)
                print(f"receive {original_message} from {addr}")
                connection.sendall(f"Server response {original_message} -> {coded_message}".encode())


if __name__ == "__main__":
    start_server_tcp()