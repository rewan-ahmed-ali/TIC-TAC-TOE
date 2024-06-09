
import tkinter as tk
from tkinter import messagebox, simpledialog

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize players
        self.player1 = simpledialog.askstring("Input", "Enter name for Player 1 (X):", parent=self.root)
        self.player2 = simpledialog.askstring("Input", "Enter name for Player 2 (O):", parent=self.root)
        self.current_player_name = self.player1
        self.current_player = "X"

        self.board = [" " for _ in range(9)]
        self.buttons = [tk.Button(root, text=" ", font='Arial 20', width=5, height=2, command=lambda i=i: self.click(i)) for i in range(9)]
        
        self.status_label = tk.Label(root, text=f"{self.current_player_name}'s turn", font='Arial 15')
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.create_board()

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

    def click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"{self.current_player_name} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                # Switch players
                if self.current_player == "X":
                    self.current_player = "O"
                    self.current_player_name = self.player2
                else:
                    self.current_player = "X"
                    self.current_player_name = self.player1
                self.status_label.config(text=f"{self.current_player_name}'s turn")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.current_player_name = self.player1
        self.status_label.config(text=f"{self.current_player_name}'s turn")
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()