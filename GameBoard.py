from tkinter import Frame, Tk, Canvas

class GameBoard(Frame):

    def __init__(self, parent, rows=8, cols=8, size=40, color1="bisque", color2="brown"):
        
        # Assign parameters to class data members
        self.rows = rows
        self.cols = cols
        self.size = size
        self.color1 = color1
        self.color2 = color2

        # Call super
        Frame.__init__(self, parent)

        self.canvas = Canvas(self, width=cols*size, height=rows*size, bg="red", borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="none", expand=True, padx=2, pady=2)
        
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):

        offset = 0

        # Get the new size
        sizex = (event.width-1) / self.cols
        sizey = (event.height-1) / self.rows
        self.size = min(sizex, sizey)

        # Remove all previously drawn tiles
        self.canvas.delete("tile")

        # Draw new tiles
        color = self.color1
        for i in range(self.rows):
            # Alternate colors
            color = self.color1 if color == self.color2 else self.color2
            for j in range(self.cols):
                x1 = offset + j * self.size
                y1 = offset + i * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle( x1, y1, x2, y2, fill=color, width=1, tags="tile" )
                # Alternate colors
                color = self.color1 if color == self.color2 else self.color2