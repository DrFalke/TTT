"""
First of all, you have to type in the IP address of the server you want to connect to.
Then you have to type in your username.
If you want to exit the chat, you can type in "/exit".
Thats it, you are now connected to the server and can send messages! :) 
"""

import socket
import threading
import time  # Import the time module

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = input("Bitte geben Sie die Server-IP ein: "), 8080
    client_socket.connect(server_address)

    username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
    time.sleep(1)  # Wait for 1 second before sending the username
    client_socket.send(f"/username {username}".encode('utf-8'))  # Send the username with a special prefix

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message == "/exit":
            client_socket.send(message.encode('utf-8'))
            client_socket.close()
            break
        else:
            client_socket.send(message.encode('utf-8'))

start_client()