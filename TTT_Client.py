#Connection
import socket

HOST = "127.0.0.1" #localhost
PORT = 61111 #port number

#IPv4 TCP/IP socket is created and bound to the address and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1) #a maximum of 1 connection is allowed
conn, addr = server.accept() #accept connection

x_dim = 3 #x dimension
y_dim = 3 #y dimension
playgroung_list = [[" "]*y_dim for i in range(x_dim)] #playgroung list
round = 1 #round number
