import socket
import pickle
import tkinter as tk
from tkinter import messagebox

class TicTacToeClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.create_gui()
        self.connect_to_server()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title('Tic-Tac-Toe Client')
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.wait_for_move()

    def wait_for_move(self):
        while True:
            data = self.client_socket.recv(1024)
            self.board = pickle.loads(data)
            self.update_board()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.board[i][j])

    def on_button_click(self, row, col):
        self.client_socket.send(pickle.dumps((row, col)))

    def on_closing(self):
        self.client_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    client = TicTacToeClient()
    client.root.mainloop()