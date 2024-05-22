import socket

HOST = "127.0.0.1" #localhost
PORT = 61111 #port number
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP/IP socket is created
server.connect((HOST, PORT)) #connect to the server

x_dim = 3 #x dimension
y_dim = 3 #y dimension
playgroung_list = [[" "]*y_dim for i in range(x_dim)] #playgroung list
round = 1 #round number

#playgroung function
def playgroung():
    for j in range(x_dim):
        print(" {}".format(j),end="")
    print() 
    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(playgroung_list[x][y]),end="")
        print("|",y)

#check for win
def check_for_win():
    # Check for horizontal win
    for x in range(0, 3):
        if playgroung_list[x][0] == playgroung_list[x][1] == playgroung_list[x][2] and playgroung_list[x][0] != ' ':
            return True
    # Check for vertical win
    for y in range(0, 3):
        if playgroung_list[0][y] == playgroung_list[1][y] == playgroung_list[2][y] and playgroung_list[0][y] != ' ':
            return True
    # Check for diagonal win
    if playgroung_list[0][0] == playgroung_list[1][1] == playgroung_list[2][2] and playgroung_list[0][0] != ' ':
        return True
    if playgroung_list[0][2] == playgroung_list[1][1] == playgroung_list[2][0] and playgroung_list[0][2] != ' ':
        return True
    else:
        return False
#check for draw
def check_for_draw():
    for x in range(0, 3):
        for y in range(0, 3):
            if playgroung_list[x][y] == " ":
                return False
    return True