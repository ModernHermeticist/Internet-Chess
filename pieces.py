#piece needs a name, available moves
#board will generate the pieces...and keep track of them?
#piece placement will occur when the board calls the pieces

class whitePawn:

	hasMoved = False

	def __init__(self):
		self.symbol = 'P'

	def move(self):
		if !self.hasMoved:
			pass


def main():

	p = whitePawn()
	print(p.hasMoved)

main()
