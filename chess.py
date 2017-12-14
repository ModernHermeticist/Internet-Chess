#This will be a fully functional chess game.
#It will allow for local play against another
#human or AI player.
#It will also allow direct connection play.
#Finally it will be displayed in GUI format.
from GameBoard import GameBoard
from tkinter import Tk

def main():
    root = Tk()
    root.title( "Internet Chess" )
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand=True, padx=4, pady=4)
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()


if __name__ == "__main__":
    main()
