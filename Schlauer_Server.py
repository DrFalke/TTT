"""
Der Server berechnet sämtliche Züge und gibt das Ergebnis an den Client zurück. 
Der Client ist nur für die Darstellung zuständig. Der Server ist der "Schlaue" und der Client der "Dumme".
"""

import socket
import pickle
import threading

class TicTacToeServer:
    def __init__(self, host='192.168.56.1', port=8080):
        self.host = host
        self.port = port
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.players = []
        self.start_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print("Server started. Waiting for players...")
        while len(self.players) < 2:
            client_socket, addr = self.server_socket.accept()
            self.players.append(client_socket)
            print(f"Player connected from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client):
        while True:
            data = client.recv(1024)
            row, col = pickle.loads(data)
            if self.make_move(row, col):
                print(f"Move made at ({row}, {col}) by {self.current_player}")
                for player in self.players:
                    player.send(pickle.dumps((self.board, self.current_player)))
                if self.check_winner():
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_board_full():
                    print("The game is a draw!")
                    break
        client.close()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

if __name__ == "__main__":
    server = TicTacToeServer()