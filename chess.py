#This will be a fully functional chess game.
#It will allow for local play against another
#human or AI player.
#It will also allow direct connection play.
#Finally it will be displayed in GUI format.
from GameBoard import GameBoard
from tkinter import Tk, Label, INSERT

def main():
    global info # The top-level application window should be made into a class to avoid use of global variables

    root = Tk()
    root.title( "Internet Chess" )

    # Game Board Widget
    board = GameBoard(root)
    board.ActiveTileChangedEvent = onActiveTileChange
    board.pack(side="top", fill="both", expand=True, padx=4, pady=4)

    # Temporary "Info" Box
    info = Label(root)
    info.config( text="Welcome" )
    info.pack(side="top", fill="none", expand=False, padx=4, pady=4)

    # Enforce minimum size for window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.mainloop()

# Handler for when the GameBoard's active tile changes
def onActiveTileChange(sender, newTileRow, newTileCol):
    info.config( text="Active Tile: {}, {}".format(newTileRow, newTileCol))

if __name__ == "__main__":
    main()
