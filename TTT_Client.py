import socket

HOST = "127.0.0.1" #localhost
PORT = 61111 #port number
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP/IP socket is created
server.connect((HOST, PORT)) #connect to the server

x_dim = 3 #x dimension
y_dim = 3 #y dimension
playground_list = [[" "]*y_dim for i in range(x_dim)] #playground list
round = 1 #round number

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
        print("It's player {} turn".format(player))
        data = server.recv(1024)
        if not data:
            break
        x = int(data)
        print("The other player has chosen the x-cord -", str(data).strip("b''"))
        if not data:
            break
        data = server.recv(1024)
        y = int(data)
        print("The other player has chosen the x-cord -", str(data).strip("b''"))
                
    else:
        player = "O"
        print("It's players {} turn!".format(player))
        data = input("input x-cord ->")
        x = int(data)
        server.sendall(data.encode())
        data = input("input y-cord ->")
        y = int(data)
        server.sendall(data.encode())
    #check the input 
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
            #check for draw
            elif (check_for_draw()):
                print("The game is a draw!")
                break
        else:
            print("Filde is already taken!")
    else:
        print("Input is out of range!")
    