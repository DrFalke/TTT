import socket # Import socket module
import pickle # Import pickle module
import os # Import os module
# Function to print the game field
def playground(field):
    for row in field:
        print(end="|")
        for char in row:
            print(char, end="|")
        print()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
client.connect(('127.0.0.1', 8111)) # Connect to the server
# Receive the initial game field
while(1):
    try:
        data = pickle.loads(client.recv(1024))
    except:
        continue
    # Check if the game is lost
    if(data[0][0] == "L"):
        print("You have lost!")
        break
    # Check if the game is won
    elif data[0][0] == "W":
        print("You have won!")
        break
    # Check if the game is tied
    elif data[0][0] == "T":
        print("You have tied!")
        break
    # Print the game field
    cls()
    playground(data)
    x = input("X: ") # Get the x coordinate
    y = input("Y: ") # Get the y coordinate
    client.sendall(pickle.dumps((x, y))) # Send the coordinates to the server