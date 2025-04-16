class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            return True
        return False

    def is_winner(self, player):
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[row][col] != 0 for row in range(3) for col in range(3))

    def get_empty_cells(self):
        return [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.board[row][col] == 0
        ]

    def is_game_over(self):
        return self.is_winner(1) or self.is_winner(-1) or self.is_draw()

    def print_board(self):
        symbols = {0: ".", 1: "X", -1: "O"}
        for row in self.board:
            print(" ".join(symbols[cell] for cell in row))
        print()
