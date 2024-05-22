import socket

HOST = '10.10.217.136' #local host
PORT = 8080 #port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object
server.bind((HOST, PORT)) #bind to the port
server.listen(1) #wait for client connection
conn, addr = server.accept() #accept the connection


x_dim = 3 #x dimension of the board 
y_dim = 3 #y dimension of the board
playground_list = [[" "]*y_dim for i in range(x_dim)] #playground list
round = 1 #round counter   
#playground function
def playground(playground_list):
    for j in range(x_dim):
        print(" {}".format(j),end="")
    print() 
    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(playground_list[x][y]),end="")
        print("|",y)

#check for win
def check_for_win(playground_list):
    # Check for horizontal win
    for x in range(0, 3):
        if playground_list[x][0] == playground_list[x][1] == playground_list[x][2] and playground_list[x][0] != ' ':
            return True
    # Check for vertical win
    for y in range(0, 3):
        if playground_list[0][y] == playground_list[1][y] == playground_list[2][y] and playground_list[0][y] != ' ':
            return True
    # Check for diagonal win
    if playground_list[0][0] == playground_list[1][1] == playground_list[2][2] and playground_list[0][0] != ' ':
        return True
    if playground_list[0][2] == playground_list[1][1] == playground_list[2][0] and playground_list[0][2] != ' ':
        return True
    else:
        return False
#check for draw
def check_for_draw(playground_list):
    for x in range(0, 3):
        for y in range(0, 3):
            if playground_list[x][y] == " ":
                return False
    return True

#game loop
while playing_aktiv == True:
    playground(playground_list)
    if (round % 2 == 0):
        player = "X"
    else:
        player = "O"
    move()
    if check_for_win(playground_list):
        playground(playground_list=playground_list)
        print("Player {} wins!".format(player))
        print("The game took {} rounds".format(round))
        playing_aktiv = False
        sending(client, playground_list)
    elif check_for_draw(playground_list):
        playground(playground_list=playground_list)
        print("Draw!")
        print("The game took {} rounds".format(round))
        playing_aktiv = False
        sending(client, playground_list)
print("Game Over!")
print("Thanks for playing!")