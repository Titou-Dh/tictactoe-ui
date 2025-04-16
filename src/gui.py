import tkinter as tk
from tkinter import messagebox
from game import TicTacToe
from ai.minmax import find_best_move
from ai.alphabeta import find_best_move_ab


class TicTacToeGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.game = TicTacToe()
        self.buttons = []
        self.algorithm = tk.IntVar(value=1)

        self.pack(padx=10, pady=10)

        self.create_algorithm_selection()
        self.create_game_grid()

    def create_algorithm_selection(self):
        algo_frame = tk.Frame(self)
        algo_frame.pack(pady=10)

        tk.Label(algo_frame, text="Choose algorithm:").pack(side=tk.LEFT)
        tk.Radiobutton(
            algo_frame, text="MinMax", variable=self.algorithm, value=1
        ).pack(side=tk.LEFT)
        tk.Radiobutton(
            algo_frame, text="Alpha-Beta", variable=self.algorithm, value=2
        ).pack(side=tk.LEFT)

    def create_game_grid(self):
        grid_frame = tk.Frame(self)
        grid_frame.pack(pady=10)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    grid_frame,
                    text="",
                    font=("Helvetica", 20),
                    width=3,
                    height=1,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)

        reset_frame = tk.Frame(self)
        reset_frame.pack(pady=5)
        tk.Button(reset_frame, text="Reset Game", command=self.reset_game).pack()

    def make_move(self, row, col):
        if self.game.board[row][col] == 0:
            self.game.board[row][col] = 1
            self.game.current_player = -1
            self.update_board()

            if self.check_game_status():
                return

            self.make_ai_move()

    def make_ai_move(self):
        print("AI is Y5amem...")
        if self.algorithm.get() == 1:
            ai_row, ai_col = find_best_move(self.game)
        else:
            ai_row, ai_col = find_best_move_ab(self.game)

        self.game.board[ai_row][ai_col] = -1
        self.game.current_player = 1
        self.update_board()

        self.check_game_status()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                if self.game.board[i][j] == 1:
                    self.buttons[index].config(text="X", state=tk.DISABLED)
                elif self.game.board[i][j] == -1:
                    self.buttons[index].config(text="O", state=tk.DISABLED)
                else:
                    self.buttons[index].config(text="", state=tk.NORMAL)

    def check_game_status(self):
        if self.game.is_winner(1):
            messagebox.showinfo("Game Over", "You win!")
            self.reset_game()
            return True
        elif self.game.is_winner(-1):
            messagebox.showinfo("Game Over", "AI wins!")
            self.reset_game()
            return True
        elif self.game.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        self.game = TicTacToe()
        self.update_board()
