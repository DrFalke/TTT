import socket
import pickle

def make_a_move():
    while(1):
        x, y = request_coordinate()
        if(field[y][x] == " "):
            field[y][x] = player
            break
    if(check_win(x, y, player) == True):
        field[0][0] = "W"
        conn.sendall(pickle.dumps(field))

def request_coordinate( ):
    conn.sendall(pickle.dumps(field))
    while(1):
        try:
            (x, y) = pickle.loads(conn.recv(1024))
            break
        except:
            pass
    return (int(x), int(y))

def has_lost():
    field[0][0] = "L"
    conn.sendall(pickle.dumps(field))

def tie():
    field[0][0] = "T"
    conn.sendall(pickle.dumps(field))

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

def  playgound():
    for j in range(3):
        print(" {}".format(j),end="")
    print() 
    for row in field:
        print(end="|")
        for char in row:
            print(char, end="|")
        print()

host = "127.0.0.1"
port = 8111

global field
field = [[" " for i in range(3)] for j in range(3)]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Waiting for connection...")
conn, addr = server.accept()
print("Connected!")

player = 0
moves = 0
while(1):
    make_a_move()
    if(field[0][0] == "W"):
        print("You have lost!")
        break
    moves += 1
    if moves == 5:
        tie()
        print("You have tied!")
        break
    while(1):
        playgound()
        x = int(input("X: "))
        y = int(input("Y: "))
        if(field[y][x] == " "):
            field[y][x] = "O"
            break
    if(check_win(x, y, "O") == True):
        print("You have Won!")
        has_lost()
        break