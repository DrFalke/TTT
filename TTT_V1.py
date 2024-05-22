import socket
#define the host and port
HOST = '10.10.217.136'
PORT = 8080
#variablen for a 3x3 board
x_dim = 3 
y_dim = 3
#initialise the board
spielfeld = [[" "]*y_dim for i in range(x_dim)]
#initialise the round variable
round = 1
#initialise the player variable   
player = "" 
#Definieren der Playingaktiv varaible um
playing_aktiv = True
#create a 3x3 matrix to represent the board
def playground(spielfeld):
    # Create the board string
    board_str = ""
    # Add the column numbers to the board string
    for j in range(x_dim):
        board_str += " {}".format(j)
    board_str += "\n"
    # Add the rows to the board string
    for y in range(y_dim):
        # Add the row number to the board string
        for x in range(x_dim):
            # Add the field value to the board string
            board_str += "|{}".format(spielfeld[x][y])
        # Add the row number to the board string    
        board_str += "| {}\n".format(y)
    return board_str
#function to send the playground to the client
def sending(sock, spielfeld):
    board_str = playground(spielfeld)
    # Send the board string to the client
    sock.send(board_str.encode())
#function to receive the move from the client
def receive_move(sock):
    # Receive the move from the client
    data = sock.recv(1024).decode()
    # Parse the move to get the coordinates
    x, y = map(int, data.split(','))
    return x, y
#function to get the player's move
def move():
    global playing_aktiv
    global round
    while True:
        #get the x and y coordinates from the player
        try:
            x = int(input("input x-cord ->"))
            y = int(input("input y-cord ->"))
            x = int(x)
            y = int(y)
        except ValueError:
            print("please enter a number from 0 to 2")
        #check if the player entered a number between 0 and 2
        else:
            if(0 <= x < x_dim) and (0 <= y < y_dim):
                if(spielfeld[x][y] == " "):
                    spielfeld[x][y] = player
                    round += 1
                    break
                else:
                    print("This field is already occupied!")
            else:
                print("Input is out of range!")
#check for win
def check_for_win(spielfeld):
    # Check for horizontal win
    for x in range(0, 3):
        if spielfeld[x][0] == spielfeld[x][1] == spielfeld[x][2] and spielfeld[x][0] != ' ':
            return True
    # Check for vertical win
    for y in range(0, 3):
        if spielfeld[0][y] == spielfeld[1][y] == spielfeld[2][y] and spielfeld[0][y] != ' ':
            return True
    # Check for diagonal win
    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] and spielfeld[0][0] != ' ':
        return True
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] and spielfeld[0][2] != ' ':
        return True
    else:
        return False
#check for draw
def check_for_draw(spielfeld):
    for x in range(0, 3):
        for y in range(0, 3):
            if spielfeld[x][y] == " ":
                return False
    return True
# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Waiting for connection...")
# Accept the connection
client, addr = server.accept()
print("Connected to {}".format(addr))
#send the playground to the client
sending(client, spielfeld)
#game loop
while playing_aktiv == True:
    playground(spielfeld)
    if (round % 2 == 0):
        player = "X"
    else:
        player = "O"
    move()
    if check_for_win(spielfeld):
        playground(spielfeld=spielfeld)
        print("Player {} wins!".format(player))
        print("The game took {} rounds".format(round))
        playing_aktiv = False
        sending(client, spielfeld)
    elif check_for_draw(spielfeld):
        playground(spielfeld=spielfeld)
        print("Draw!")
        print("The game took {} rounds".format(round))
        playing_aktiv = False
        sending(client, spielfeld)
print("Game Over!")
print("Thanks for playing!")