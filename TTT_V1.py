#variablen for a 3x3 Matrix
x_dim = 3 
y_dim = 3
#initialize the playground
spielfeld = [[" "]*y_dim for i in range(x_dim)]
#initialize the round counter
round = 1
# Define the variable "player" to keep track of whose turn it is 
player = "" 
# Define the variable "playing_aktiv" to keep track of whether the game is still active
playing_aktiv = True
#create a 3x3 matrix to represent the board
def playground(spielfeld):
    for j in range(x_dim):
        print(" {}".format(j),end='')
    print()
    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(spielfeld[x][y]),end='')
        print("|",y)
    return spielfeld
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
        print("Das spiel hat {} runden gedauert".format(round))
        playing_aktiv = False
    elif check_for_draw(spielfeld):
        playground(spielfeld=spielfeld)
        print("Unentschieden!")
        print("Das spiel hat {} runden gedauert".format(round))
        playing_aktiv = False

print("Game Over!")