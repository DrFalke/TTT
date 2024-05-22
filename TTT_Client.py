import socket

HOST = "127.0.0.1" #localhost
PORT = 61111 #port number
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP/IP socket is created
server.connect((HOST, PORT)) #connect to the server

x_dim = 3 #x dimension
y_dim = 3 #y dimension
playgroung_list = [[" "]*y_dim for i in range(x_dim)] #playgroung list
round = 1 #round number
