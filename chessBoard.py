
class chessBoard:
	grid = [0]*8
	for i in range(len(grid)):
		grid[i]=[0]*8
	viableSpaces = []
	pieces = [('Empty','No Color'),('Pawn','Black'),
			('Knight','Black'),('Bishop','Black'),('Rook','Black'),('Queen','Black'),('King','Black'),
			('Pawn','White'),('Knight','White'),('Bishop','White'),('Rook','White'),('Queen','White'),
			('King','White')]
	
	def __init__(self):
		self.grid[1] = [1]*8; self.grid[6]=[7]*8
		self.grid[0][0] = 4; self.grid[0][1] = 2; self.grid[0][2] = 3; self.grid[0][3] = 5;
		self.grid[0][4] = 6; self.grid[0][5] = 3; self.grid[0][6] = 2; self.grid[0][7] = 4;
		self.grid[7][0] = 10; self.grid[7][1] = 8; self.grid[7][2] = 9; self.grid[7][3] = 11;
		self.grid[7][4] = 12; self.grid[7][5] = 9; self.grid[7][6] = 8; self.grid[7][7] = 10;
		
