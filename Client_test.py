import socket
 
host = '10.10.217.98'
port = 8080
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host , port))
print("Connected to the server")
 
while True:
    # Receive data from the server
    reply = client.recv(1024).decode()
 
    # Print the received data (playground)
    print("Playground:")
    print(reply)
 
    x = int(input("input x-cord ->"))
    y = int(input("input y-cord ->"))
 
    message = f"{x},{y}"
    client.send(message.encode())
