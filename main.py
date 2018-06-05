import tkinter as tk
from tkinter import *
import chessBoard as cb
import chessCom as com
WIDTH = 874
HEIGHT = 778
class App:
	board = cb.chessBoard()
	t = 0
	itemClicked = False
	comOp = False
	colors = ['White','Black']
	missingPiecesBlack = []
	missingPiecesWhite = []
	
	def __init__(self,master):
		self.Master=master
		master.title("Chess")
		self.canvas = Canvas(self.Master)
		
		
	def Yes(self):
		self.comOp = True
		self.computer = com.chessCom()
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
				lW = 10 + 96*i
				lH = 10 + 96*j
				self.canvas.create_image(lW,lH,image=self.emptySpaces[(i+j)%2],anchor=NW,activeimage = self.emptySpaces[2])
		for r in range(8):
			for c in range(8):
				lH = 10 + 96*r
				lW = 10 + 96*c
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
		
if __name__ == '__main__':		
	root = tk.Tk()
	app = App(root)
