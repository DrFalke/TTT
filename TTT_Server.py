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
def playground():
    for j in range(x_dim):
        print(" {}".format(j),end="")
    print() 
    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(playground_list[x][y]),end="")
        print("|",y)

#check for win
def check_for_win():
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
def check_for_draw():
    for x in range(0, 3):
        for y in range(0, 3):
            if playground_list[x][y] == " ":
                return False
    return True

#game loop
while (round <= 9):
    playground()
    if (round % 2 == 0):
        player = "X"
        print("it's player {} turn!".format(player))
        data = input("input the x-cord ->")
        x = int(data)
        data = bytes(data, 'utf-8')
        conn.sendall(data)
        data = input("input the y-cord ->")
        y = int(data)
        data = bytes(data, 'utf-8')
        conn.sendall(data)
    else:
        player = "O"
        print("players {} turn!".format(player))
        data = conn.recv(1024)
        print("The other player has chosen the x-cord -", repr(data).strip("b''"))
        x = int(data)
        data = conn.recv(1024)
        print("The other player has chosen the y-cord -", repr(data).strip("b''"))
        y = int(data)

    #prove if the input is in the range of the playground
    if (0 <= x < x_dim) and (0 <= y < y_dim):
        if (playground_list[x][y] == " "):
            #fild is free
            playground_list[x][y] = player
            round += 1
            #check for win
            if(check_for_win()):
                print("Player {} has won the Game!".format(player))
                playground()
                break
            elif(check_for_draw()):
                print("The game is a draw!")
                playground()
                break                   
        else:
            print("Fild already taken!")
    else:
        print("The input is out of range!")