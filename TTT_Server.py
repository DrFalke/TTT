import socket # Import socket module
import pickle # Import pickle module

# Function to check if the player has won
def make_a_move():
    while(1):
        x, y = request_coordinate()
        if(field[y][x] == " "):
            field[y][x] = player
            break
    if(check_win(x, y, player) == True):
        field[0][0] = "W"
        conn.sendall(pickle.dumps(field))

# Function to request the coordinate from the client
def request_coordinate( ):
    conn.sendall(pickle.dumps(field))
    while(1):
        try:
            (x, y) = pickle.loads(conn.recv(1024))
            break
        except:
            pass
    return (int(x), int(y))

# Function to check if the player has lost
def has_lost():
    field[0][0] = "L"
    conn.sendall(pickle.dumps(field))

# Function to check if the game is a tie
def tie():
    field[0][0] = "T"
    conn.sendall(pickle.dumps(field))

# Function to check if the player has won
def check_win(x_set, y_set, player):
    win = True
    for x in range (0, 3):
        if not field[y_set][x] == player:
            win = False
            break
    if win == True:
        return True
    win = True
    for y in range (0, 3):
        if not field[y][x_set] == player:
            win = False
    if win == True:
        return True
    if field[0][0]==player and field[1][1]==player and field[2][2]==player or field[0][2]==player and field[1][1]==player and field[2][0]==player:
        return True
    return False

# Function to print the playground
def  playgound():
    for j in range(3):
        print(" {}".format(j),end="")
    print() 
    for row in field:
        print(end="|")
        for char in row:
            print(char, end="|")
        print()

host = "127.0.0.1" # Get the local machine name
port = 8111 # Reserve a port for your service

global field # Create a global variable field
field = [[" " for i in range(3)] for j in range(3)] # Create a 3x3 playground

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
server.bind((host, port)) # Bind to the port
server.listen(1) # Now wait for client connection
print("Waiting for connection...") # Print a message
conn, addr = server.accept() # Establish connection with client
print("Connected!") # Print a message to show that the connection has been established

player = 0 # Set the player to 0
moves = 0 # Set the moves to 0
# The game loop
while(1): 
    make_a_move()
    # Check if the player has won
    if(field[0][0] == "W"):
        print("You have lost!")
        break
    moves += 1
    # Check if the game is a tie
    if moves == 5:
        tie()
        print("You have tied!")
        break
    # Check if the player has lost
    while(1):
        playgound()
        x = int(input("X: "))
        y = int(input("Y: "))
        # Check if the field is empty
        if(field[y][x] == " "):
            field[y][x] = "O"
            break
    # Check if the player has won
    if(check_win(x, y, "O") == True):
        print("You have Won!")
        has_lost()
        break