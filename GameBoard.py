from tkinter import Frame, Tk, Canvas, CURRENT

class GameBoard(Frame):

    def __init__(self, parent, rows=8, cols=8, size=40, color1="bisque", color2="brown"):

        # Constant width of tile boarders
        self._BOARDER_WIDTH = 2

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

        self._canvas = Canvas(self,
            width=cols*(size+self._BOARDER_WIDTH*2),
            height=rows*(size+self._BOARDER_WIDTH*2),
            bg="red",
            borderwidth=0,
            highlightthickness=0)
        self._canvas.pack(side="top", fill="none", expand=True, padx=2, pady=2)
        
        self._canvas.bind("<Configure>", self.resize)
        self._canvas.bind("<Button-1>", self.click)
        self._canvas.bind("<Motion>", self.motion)

        self.draw()

    # Called every time the board is resized
    def resize(self, event):

        # Get the new size
        sizex = (event.width-1) / self._cols - self._BOARDER_WIDTH*2
        sizey = (event.height-1) / self._rows - self._BOARDER_WIDTH*2
        self._size = min(sizex, sizey)
        
        for i in range(self._rows):
            for j in range(self._cols):
                x1 = j * (self._size+self._BOARDER_WIDTH*2)+self._BOARDER_WIDTH
                y1 = i * (self._size+self._BOARDER_WIDTH*2)+self._BOARDER_WIDTH
                x2 = x1 + self._size
                y2 = y1 + self._size
                self._canvas.coords("({0},{1})".format(j,i), x1, y1, x2, y2)

    # Called to draw the initial board
    def draw(self):

        # Draw new tiles
        color = self._color1
        for i in range(self._rows):
            # Alternate colors
            color = self._color1 if color == self._color2 else self._color2
            for j in range(self._cols):
                x1 = j * (self._size+self._BOARDER_WIDTH*2)+self._BOARDER_WIDTH
                y1 = i * (self._size+self._BOARDER_WIDTH*2)+self._BOARDER_WIDTH
                x2 = x1 + self._size
                y2 = y1 + self._size
                self._canvas.create_rectangle( x1, y1, x2, y2, fill=color, width=self._BOARDER_WIDTH*2,
                    tags=("tile","({0},{1})".format(j,i)) )
                # Alternate colors
                color = self._color1 if color == self._color2 else self._color2

    # Motion event handler
    def motion(self, event):
        self._canvas.tag_raise(CURRENT)

    # Click event handler
    def click(self, event):

        newTileRow = int(event.y // self._size)
        newTileCol = int(event.x // self._size)

        # Debug terminal output
        print("Row:{}, Col:{}".format(newTileRow, newTileCol))

        self.changeTileColor( newTileCol, newTileRow, "pink" )

        # Trigger event, if a handler is assigned
        if self.ActiveTileChangedEvent is not None:
           self.ActiveTileChangedEvent(self, newTileCol, newTileRow)

    def changeTileColor( self, tileX, tileY, color ):
        if self._canvas.find_withtag("({0},{1})".format(tileX,tileY)):
            self._canvas.itemconfig("({0},{1})".format(tileX,tileY), outline=color)
            self._canvas.update_idletasks()
