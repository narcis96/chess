import Tkinter as tk
from Tkinter import *
import chessBoard as cb
import player as com
WIDTH = 874
HEIGHT = 778
RESURSE = 'resurse/'
class App:
	board = cb.chessBoard()
	missingPiecesBlack = []
	itemClicked = False
	colors = ['White','Black']
	missingPiecesWhite = []
	t = 0
	comOp = False
	
	def __init__(self,master):
		self.Master=master
		master.title("Chess")
		self.canvas = Canvas(self.Master)
		self.pieces = [tk.PhotoImage(file = RESURSE + 'SquareWhite.gif'),tk.PhotoImage(file=RESURSE +'PawnBlack.gif'),tk.PhotoImage(file=RESURSE+'KnightBlack.gif'),tk.PhotoImage(file=RESURSE+'BishopBlack.gif'), tk.PhotoImage(file=RESURSE+'RookBlack.gif'),tk.PhotoImage(file=RESURSE+'QueenBlack.gif'),tk.PhotoImage(file=RESURSE+'KingBlack.gif'),tk.PhotoImage(file=RESURSE+'PawnWhite.gif'), tk.PhotoImage(file=RESURSE+'KnightWhite.gif'),tk.PhotoImage(file=RESURSE+'BishopWhite.gif'),tk.PhotoImage(file=RESURSE+'RookWhite.gif'),tk.PhotoImage(file=RESURSE+'QueenWhite.gif'), tk.PhotoImage(file=RESURSE+'KingWhite.gif')]
		self.activePieces = [tk.PhotoImage(file=RESURSE+'SquareWhite.gif'),tk.PhotoImage(file=RESURSE+'PawnBlackAct.gif'),tk.PhotoImage(file=RESURSE+'KnightBlackAct.gif'), tk.PhotoImage(file=RESURSE+'BishopBlackAct.gif'), tk.PhotoImage(file=RESURSE+'RookBlackAct.gif'),tk.PhotoImage(file=RESURSE+'QueenBlackAct.gif'),tk.PhotoImage(file=RESURSE+'KingBlackAct.gif'), tk.PhotoImage(file=RESURSE+'PawnWhiteAct.gif'), tk.PhotoImage(file=RESURSE+'KnightWhiteAct.gif'),tk.PhotoImage(file=RESURSE+'BishopWhiteAct.gif'),tk.PhotoImage(file=RESURSE+'RookWhiteAct.gif'), tk.PhotoImage(file=RESURSE+'QueenWhiteAct.gif'), tk.PhotoImage(file=RESURSE+'KingWhiteAct.gif')]
		self.emptySpaces = [tk.PhotoImage(file=RESURSE+'SquareWhite.gif'),tk.PhotoImage(file=RESURSE+'SquareGrey.gif'),tk.PhotoImage(file=RESURSE+'SquareActive.gif'), tk.PhotoImage(file=RESURSE+'SquareClicked.gif')]
		self.frame = Frame(master); self.frame.grid()
		self.play = Label(self.frame, text = "Single player (against computer) or two players?")
		self.play.grid(row=0, column =0, columnspan = 6)
		self.YesButton = Button(self.frame, text = "Single Player", command = self.Yes)
		root.bind('<Return>', (lambda e, YesButton=self.YesButton: self.YesButton.invoke()))
		self.YesButton.grid(row=1,column=0)
		self.NoButton = Button(self.frame, text='Two Players', command=self.No)
		self.NoButton.grid(row=1,column =1)
		
	def Yes(self):
		self.comOp = True
		self.computer = com.player()
		self.frame.destroy()
		self.startGame()
		
	def No(self):
		self.frame.destroy()
		self.startGame()
		
	def startGame(self):
		self.Master.minsize(WIDTH,HEIGHT)
		self.canvas.config(height=HEIGHT,width=WIDTH,bg = 'black')
		self.canvas.pack()
		self.Master.update()
		self.displayBoard()
		
	def displayBoard(self):
		for i in range(8):
			for j in range(8):
				lH = 10 + 96*j
				lW = 10 + 96*i
				self.canvas.create_image(lW,lH,image=self.emptySpaces[(i+j)%2],anchor=NW,activeimage = self.emptySpaces[2])
		for r in range(8):
			for c in range(8):
				lW = 10 + 96*c
				lH = 10 + 96*r
				if self.board.grid[r][c] != 0:
					self.canvas.create_image(lW,lH,image=self.pieces[self.board.grid[r][c]],anchor=NW,activeimage = self.activePieces[self.board.grid[r][c]])
		for k in range(12):
			lH = 10 + 61*k
			self.canvas.create_image(HEIGHT + 1,lH,image=self.emptySpaces[0],anchor=NW)
		for l in range(len(self.missingPiecesBlack)):
			lH = 10 + 96*l
			self.canvas.create_image(HEIGHT + 1,lH,image=self.pieces[self.missingPiecesBlack[l]],anchor=NW)
		for n in range(len(self.missingPiecesWhite)):
			lH = 394 + 96*n
			self.canvas.create_image(HEIGHT + 1,lH,image=self.pieces[self.missingPiecesWhite[n]],anchor=NW)
		self.Master.update()
	
	def callback(self,event):
		color = self.colors[self.t%2]
		if self.itemClicked == False:
			for r in range(len(self.board.grid)):
				for c in range(len(self.board.grid[r])):
					lH = 10 + 96*r
					lW = 10 + 96*c
					if event.x in range(lW,lW+90) and event.y in range(lH,lH+90) and self.board.grid[r][c] != 0 and self.board.pieces[self.board.grid[r][c]][1] == color:
						self.canvas.create_image(lW,lH,image=self.emptySpaces[3],anchor=NW)
						self.canvas.create_image(lW,lH,image=self.pieces[self.board.grid[r][c]],anchor=NW)
						self.itemClicked = True
						self.curPos = [r,c]
		else:
			for r in range(len(self.board.grid)):
				for c in range(len(self.board.grid[r])):
					lH = 10 + 96*r
					lW = 10 + 96*c
					if event.x in range(lW,lW+90) and event.y in range(lH,lH+90):
						if r == self.curPos[0] and c == self.curPos[1]:
							self.canvas.create_image(lW,lH,image=self.emptySpaces[(r+c)%2],anchor=NW)
							self.canvas.create_image(lW,lH,image=self.pieces[self.board.grid[r][c]],anchor=NW,activeimage = self.activePieces[self.board.grid[r][c]])
							self.itemClicked = False
						else:
							self.finPos = [r,c]
							if self.board.turnValid(self.board.grid,self.curPos,self.finPos,color):
								self.itemClicked = False
								self.t += 1
								#Add to missing pieces list ---------------------------------------------------
								if self.board.grid[self.finPos[0]][self.finPos[1]]%6 > 1 and color == 'White':
									self.missingPiecesBlack.append(self.board.grid[self.finPos[0]][self.finPos[1]])
									if len(self.missingPiecesBlack) > 4:
										self.missingPiecesBlack.remove(min(self.missingPiecesBlack))
								elif self.board.grid[self.finPos[0]][self.finPos[1]]%6 > 1 and color == 'Black':
									self.missingPiecesWhite.append(self.board.grid[self.finPos[0]][self.finPos[1]])
									if len(self.missingPiecesWhite) > 4:
										self.missingPiecesWhite.remove(min(self.missingPiecesWhite))
								# --------------------------------------------------------------
								self.board.grid[self.finPos[0]][self.finPos[1]] = self.board.grid[self.curPos[0]][self.curPos[1]]
								self.board.grid[self.curPos[0]][self.curPos[1]] = 0
								#Pawn promotion -----------------------------------------------------------
								if (self.board.grid[self.finPos[0]][self.finPos[1]] == 1 and r == 7) or (self.board.grid[self.finPos[0]][self.finPos[1]] == 7 and r == 0):
									if color == 'White' and len(self.missingPiecesWhite) > 0:
										self.board.grid[self.finPos[0]][self.finPos[1]] = max(self.missingPiecesWhite)
										self.missingPiecesWhite.remove(max(self.missingPiecesWhite))
									elif color == "Black" and len(self.missingPiecesBlack) > 0:
										self.board.grid[self.finPos[0]][self.finPos[1]] = max(self.missingPiecesBlack)
										self.missingPiecesBlack.remove(max(self.missingPiecesBlack))
								# -----------------------------------------------------------
								self.canvas.delete(ALL)
								self.displayBoard()
							if self.comOp == True and self.t%2 == 1:
								color = self.colors[self.t%2]
								choice = self.computer.makeMove(self.board,color)
								#Add to missing pieces list ---------------------------------------------------
								if self.board.grid[choice[2][0]][choice[2][1]]%6 > 1 and color == 'Black':
									self.missingPiecesWhite.append(self.board.grid[choice[2][0]][choice[2][1]])
									if len(self.missingPiecesWhite) > 4:
										self.missingPiecesWhite.remove(min(self.missingPiecesWhite))
								elif self.board.grid[choice[2][0]][choice[2][1]]%6 > 1 and color == 'White':
									self.missingPiecesBlack.append(self.board.grid[choice[2][0]][choice[2][1]])
									if len(self.missingPiecesBlack) > 4:
										self.missingPiecesBlack.remove(min(self.missingPiecesBlack))
								# -----------------------------------------------------------
								self.board.grid[choice[2][0]][choice[2][1]] = self.board.grid[choice[1][0]][choice[1][1]]
								self.board.grid[choice[1][0]][choice[1][1]] = 0
								#Pawn promotion -----------------------------------------------------------
								if (self.board.grid[choice[2][0]][choice[2][1]] == 1 and r == 7) or (self.board.grid[choice[2][0]][choice[2][1]] == 7 and r == 0):
									if color == 'Black' and len(self.missingPiecesBlack) > 0:
										self.board.grid[choice[2][0]][choice[2][1]] = max(self.missingPiecesBlack)
										self.missingPiecesBlack.remove(max(self.missingPiecesBlack))
									elif color == "White" and len(self.missingPiecesWhite) > 0:
										self.board.grid[choice[2][0]][choice[2][1]] = max(self.missingPiecesWhite)
										self.missingPiecesWhite.remove(max(self.missingPiecesWhite))
								# -----------------------------------------------------------
#								print()
#								print(choice[1],choice[2],choice[3])
#								print()
								self.t += 1
								self.canvas.delete(ALL)
								self.displayBoard()
			self.Master.update()

if __name__ == '__main__':		
	root = tk.Tk()
	app = App(root)
	app.canvas.bind("<Button-1>", app.callback)
	root.mainloop()