"""
First of all, you need to type in your username.
Than you must wait for the clients to connect.
After that you can send messages to all clients.
If you want to exit the chat, you can type in /exit.
"""


import socket
import threading

connected_clients = []
client_usernames = {}

def handle_client(client_socket):
    username = None
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith("/username "):  # If the message is a username message
                username = message[10:]  # Extract the username
                client_usernames[client_socket] = username
                print(f"{username} ist dem Chat beigetreten")  # Display the username
            elif message == "/exit":
                connected_clients.remove(client_socket)
                del client_usernames[client_socket]
                client_socket.close()
                break
            else:
                print(f"{username}: {message}")  # Removed the colon after the message
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
            client.send(f"{username} {message}".encode('utf-8'))

def start_server():
    ip_address = input("Bitte geben Sie die IP-Adresse ein: ")
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip_address, 8080))  # Bindet an die angegebene IP-Adresse
        server_socket.listen(5)
        print("Server gestartet. Warte auf Verbindungen...")
    except socket.gaierror:
        print("Ungültige oder nicht erreichbare IP-Adresse. Bitte versuchen Sie es erneut.")
        return

    send_thread = threading.Thread(target=send_message)
    send_thread.start()

    while True:
        client_socket, address = server_socket.accept()
        connected_clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
start_server()
