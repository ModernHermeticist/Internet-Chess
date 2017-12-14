from tkinter import Frame, Tk, Canvas

class GameBoard(Frame):

    def __init__(self, parent, rows=8, cols=8, size=40, color1="bisque", color2="brown"):

        # Event for when the active tile is changed
        self.ActiveTileChangedEvent = None
        
        # Assign parameters to class data members
        self._rows = rows
        self._cols = cols
        self._size = size
        self._color1 = color1
        self._color2 = color2

        # Call super
        Frame.__init__(self, parent)

        self._canvas = Canvas(self, width=cols*size, height=rows*size, bg="red", borderwidth=0, highlightthickness=0)
        self._canvas.pack(side="top", fill="none", expand=True, padx=2, pady=2)
        
        self._canvas.bind("<Configure>", self.refresh)
        self._canvas.bind("<Button-1>", self.click)

    # Called every time the board needs to be redrawn (resized)
    def refresh(self, event):

        # Get the new size
        sizex = (event.width-1) / self._cols
        sizey = (event.height-1) / self._rows
        self._size = min(sizex, sizey)

        # Remove all previously drawn tiles
        self._canvas.delete("tile")

        # Draw new tiles
        color = self._color1
        for i in range(self._rows):
            # Alternate colors
            color = self._color1 if color == self._color2 else self._color2
            for j in range(self._cols):
                x1 = j * self._size
                y1 = i * self._size
                x2 = x1 + self._size
                y2 = y1 + self._size
                self._canvas.create_rectangle( x1, y1, x2, y2, fill=color, width=1, tags="tile" )
                # Alternate colors
                color = self._color1 if color == self._color2 else self._color2

    # Click event handler
    def click(self, event):

        newTileRow = int(event.y // self._size)
        newTileCol = int(event.x // self._size)

        # Debug terminal output
        print("Row:{}, Col:{}".format(newTileRow, newTileCol))

        # Trigger event, if a handler is assigned
        if self.ActiveTileChangedEvent is not None:
           self.ActiveTileChangedEvent(self, newTileRow, newTileCol)
