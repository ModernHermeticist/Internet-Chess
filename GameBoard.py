from tkinter import Frame, Tk, Canvas, CURRENT

class GameBoard(Frame):

    def __init__(self, parent, rows=8, cols=8, size=40, color1="bisque", color2="brown"):

        # Constant width of tile boarders
        self._BOARDER_WIDTH = 10
        self._C_BOARDER = self._BOARDER_WIDTH*1.5-0.5

        # Event for when the active tile is changed
        self.ActiveTileChangedEvent = None
        
        self._activeTile = 0

        # Assign parameters to class data members
        self._rows = rows
        self._cols = cols
        self._size = size
        self._color1 = color1
        self._color2 = color2

        # Call super
        Frame.__init__(self, parent)

        self._cWidth = self._C_BOARDER + cols * ( size + self._BOARDER_WIDTH )
        self._cHeight = self._C_BOARDER + rows * ( size + self._BOARDER_WIDTH )

        self._canvas = Canvas(self,
            width = self._cWidth + self._BOARDER_WIDTH/2,
            height = self._cHeight + self._BOARDER_WIDTH/2,
            bg = "red", # red was chosen because it sticks out if the chess board does not cover the whole area
            borderwidth = 0,
            highlightthickness = 0)
        self._canvas.pack(side="top", fill="none", expand=True, padx=2, pady=2)
        
        self._canvas.bind("<Configure>", self.resize)
        self._canvas.bind("<Button-1>", self.click)
        self._canvas.bind("<Motion>", self.motion)

        self.draw()

    # Called every time the board is resized
    def resize(self, event):

        # Get the new size
        sizex = (event.width-self._BOARDER_WIDTH*2) / self._cols - self._BOARDER_WIDTH
        sizey = (event.height-self._BOARDER_WIDTH*2) / self._rows - self._BOARDER_WIDTH
        self._size = min(sizex, sizey)
        
        for i in range(self._rows):
            for j in range(self._cols):
                x1 = self._C_BOARDER + j * (self._size+self._BOARDER_WIDTH)
                y1 = self._C_BOARDER + i * (self._size+self._BOARDER_WIDTH)
                x2 = x1 + self._size
                y2 = y1 + self._size
                self._canvas.coords("({},{})".format(j,i), x1, y1, x2, y2)

    # Called to draw the initial board
    def draw(self):

        # Create a boarder around the tiles
        self._canvas.create_rectangle( self._BOARDER_WIDTH/2-0.5, self._BOARDER_WIDTH/2-0.5, self._cWidth, self._cHeight, width=self._BOARDER_WIDTH )

        # Draw new tiles
        color = self._color1
        for i in range(self._rows):
            # Alternate colors
            color = self._color1 if color == self._color2 else self._color2
            for j in range(self._cols):
                x1 = self._C_BOARDER + j * (self._size+self._BOARDER_WIDTH)
                y1 = self._C_BOARDER + i * (self._size+self._BOARDER_WIDTH)
                x2 = x1 + self._size
                y2 = y1 + self._size
                self._canvas.create_rectangle( x1, y1, x2, y2, fill=color, width=self._BOARDER_WIDTH,
                    tags=("tile","({},{})".format(j,i)) )
                # Alternate colors
                color = self._color1 if color == self._color2 else self._color2

    # Motion event handler
    def motion(self, event):
        both = list(filter(lambda x:x in self._canvas.find_withtag(CURRENT), self._canvas.find_withtag("tile")))
        #both = list(set(self._canvas.find_withtag(CURRENT)).intersection(set(self._canvas.find_withtag("tile"))))
        if len(both):
            tile = both[0]
            if not tile == self._activeTile: # if it is a new tile
                self.changeTileColor(self._activeTile, "black")
                #self._canvas.dtag("hover", "hover") # removes the hover tag from old tile
                #self._canvas.addtag_withtag("hover", tile) # add the hover tag to new tile
                self._activeTile = tile
                self._canvas.itemconfig(tile, outline="orange")

    # Click event handler
    def click(self, event):

        '''# Boundaries for the tile area
        minX = self._BOARDER_WIDTH
        maxX = self._BOARDER_WIDTH + self._cols * (self._size+self._BOARDER_WIDTH)
        minY = self._BOARDER_WIDTH
        maxY = self._BOARDER_WIDTH + self._rows * (self._size+self._BOARDER_WIDTH)

        # Ensure that the click happens in the tile area
        if y < minY or y >= maxY or \
           x < minX or x >= maxX:
            return'''

        col, row = self.xyToColRow(event.x, event.y)

        # Debug terminal output
        print("Row:{}, Col:{}".format(row, col))

        # Ensure that the click happens in the tile area
        if row < 0 or row >= self._rows or \
           col < 0 or col >= self._cols:
            return

        self.colRowChangeTileColor( col, row, "pink" )

        # Trigger event, if a handler is assigned
        if self.ActiveTileChangedEvent is not None:
           self.ActiveTileChangedEvent(self, col, row)

    def changeTileColor( self, tag, color ):
        if self._canvas.find_withtag(tag):
            self._canvas.itemconfig(tag, outline=color)
            self._canvas.update_idletasks()

    def colRowChangeTileColor( self, col, row, color ):
        tag = "({},{})".format( col, row )
        self.changeTileColor( tag, color )

    # Convert x, y into tile coordinates
    def xyToColRow( self, x, y ):
        col = int((x-self._BOARDER_WIDTH) // (self._size+self._BOARDER_WIDTH))
        row = int((y-self._BOARDER_WIDTH) // (self._size+self._BOARDER_WIDTH))
        return col, row 