from tkinter import Tk
from gui import TicTacToeGUI


def main():
    root = Tk()
    root.title("Tic Tac Toe")
    game_gui = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
