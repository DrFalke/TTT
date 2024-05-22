import socket
# define the ipaddress and the port number
host = '10.10.218.64'
port = 8080
# create a socket at client side using TCP/IP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host , port))
print("Connected to the server")
# receive data from the server
while True:
    # Receive data from the server
    reply = client.recv(1024).decode()

    #just for testing 
    # Print the received data (playground)
    print("Playground:")
    print(reply)
    # Ask the user to input the x and y coordinates
    x = int(input("input x-cord ->"))
    y = int(input("input y-cord ->"))
    # Send the coordinates to the server
    message = f"{x},{y}"
    client.send(message.encode())

