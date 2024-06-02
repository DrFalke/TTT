import socket
import pickle
import tkinter as tk
from tkinter import messagebox

class TicTacToeServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title('Tic-Tac-Toe Server')
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.current_player = 'O'
            self.send_board()
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.board[row][col]} wins!")
                self.reset_board()
            self.wait_for_move()

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
        self.current_player = 'X'
        self.send_board()

    def check_winner(self):
        lines = (
            [self.board[0], self.board[1], self.board[2]],
            [list(col) for col in zip(*self.board)],
            [[self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]]
        )
        for line_set in lines:
            for line in line_set:
                if line.count(line[0]) == 3 and line[0] != ' ':
                    return line[0]
        return None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f'Server listening on {self.host}:{self.port}')
        self.conn, addr = self.server_socket.accept()
        print(f'Connected by {addr}')
        self.send_board()

    def send_board(self):
        data = pickle.dumps(self.board)
        self.conn.sendall(data)
        
    def wait_for_move(self):
        while True:
            data = self.sock.recv(4096)
            move = pickle.loads(data)
            if move is not None:
                if len(move) == 2:
                    row, col = move
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        self.update_board()
                        if self.check_winner():
                            messagebox.showinfo("Game Over", "Player X wins!")
                            self.reset_board()

def on_closing(self):
    self.conn.close()
    self.server_socket.close()
    self.root.destroy()

    def start(self):
        self.root.after(100, self.start_server)
        self.root.mainloop()

if __name__ == '__main__':
    server = TicTacToeServer()
    server.start()
