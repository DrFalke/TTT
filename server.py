import socket
import threading

connected_clients = []

def handle_client(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "/exit":
                connected_clients.remove(client_socket)
                client_socket.close()
                break
            else:
                print(f"Nachricht erhalten von {username}: {message}")
                for client in connected_clients:
                    if client != client_socket:
                        client.send(f"{username}: {message}".encode('utf-8'))
        except:
            client_socket.close()
            break

def send_message():
    username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
    while True:
        message = input()
        for client in connected_clients:
            client.send(f"{username}: {message}".encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.56.1', 8080))  # Bind to all available interfaces
    server_socket.listen(5)
    print("Server gestartet. Warte auf Verbindungen...")

    send_thread = threading.Thread(target=send_message)
    send_thread.start()

    while True:
        client_socket, address = server_socket.accept()
        connected_clients.append(client_socket)
        print(f"Neue Verbindung von {address[0]}:{address[1]}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()