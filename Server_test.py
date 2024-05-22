import socket

HOST = "10.10.218.64"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST, PORT))
server.listen(1)

print("Server läuft und wartet auf Verbindung")

client, address = server.accept()
print(f"Es konnte mit {address} eine Verbindung aufgebaut werden")

while True:
    message = client.recv(1024).decode()
    if message == "exit":
        break
    print(f"Client: {message}")
    reply = input("Server: ")
    client.send(reply.encode())

client.close()
server.close()
