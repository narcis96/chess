import math
import chessBoard as cb
from random import choice
import copy
import chess
from Neural_Network import NeuralNetwork
class player:

	def __init__(self):
		self.gameBoard = chess.Board()
		self.layers = [[0.980387919287529, 0.6474419063404472, 0.16792691161694762, 0.5769313802043031, 0.6706039285245391, 0.6280155611233161, 0.09935413521220327, 0.40539108950651337, 0.19437617970540655, 0.541066132818385], [0.3473451298742617, 0.8501141804573936, 0.7824274160843238, 0.052648592718530285, 0.42327269978042137, 0.7016450673421375, 0.42626590505168294, 0.33359577103619875, 0.07622579086979042, 0.985727647912295], [0.88931906278011, 0.628743713922838, 0.3981540274891813, 0.468891668222183, 0.691167298136054, 0.06297249411252137, 0.8364138553623081, 0.8479942978770231, 0.32644240807468683, 0.5599095148494678], [0.9986756673045996, 0.46573288240599653, 0.461357607683318, 0.346827106267659, 0.3449875232567178, 0.9954455721205505, 0.46253991983568876, 0.29721978842083807, 0.0950957507425565, 0.03420451491888987], [0.5832844201502072, 0.2370776982800903, 0.9279835018739888, 0.5827135815362862, 0.618530862583544, 0.27904930899243185, 0.82650238979006, 0.8983562631841708, 0.4817792176426975, 0.21735943796434265], [0.15191366101282067, 0.07364579894623668, 0.93869335169828, 0.01935727967136902, 0.702977726136353, 0.7623065807489392, 0.19301101912084462, 0.6607615734264356, 0.02612338496723221, 0.8785271321760161], [0.9062570844987892, 0.2227967058097512, 0.16381440720404794, 0.5181676821854615, 0.9337316438822966, 0.5111125797385804, 0.7988188249341194, 0.5833271374111773, 0.08450548746700881, 0.9078924716631417], [0.43048413322771306, 0.11813628971949208, 0.31569316762605526, 0.4894631574029519, 0.43483676314126607, 0.7092020797311152, 0.47170672101350375, 0.26395016083936573, 0.35220847239627506, 0.24797995656383398], [0.3116708634315597, 0.0029044515964246065, 0.0993391492425112, 0.05894437485358994, 0.06880635746070796, 0.594728349028283, 0.4604875698409675, 0.8972244022860567, 0.8510384632859578, 0.15768611881618033], [0.46841518613203037, 0.1082643910672737, 0.6877236667119417, 0.5183231593413817, 0.2989809779548921, 0.6133323575487193, 0.6165556381998286, 0.24365923346260732, 0.7678036741674775, 0.37120917165465794]]
		self.nn  = NeuralNetwork(self.layers)

	def alphabeta(self, board, depth, alpha, beta, maximize):
		if board.is_checkmate():
			return -40 if maximize else 40
		elif board.is_game_over():
			return 0

		if depth == 0:
			return self.boardValue(board)

		if maximize:
			bestValue = float("-inf")
			for move in board.legal_moves:
				experimentBoard = board.copy()
				experimentBoard.push(move)
				value = self.alphabeta(experimentBoard, depth, alpha, beta, False)
				bestValue = max(bestValue, value)
				alpha = max(alpha, bestValue)
				if alpha >= beta:
					break
			return bestValue
		else:
			bestValue = float("inf")
			for move in board.legal_moves:
				experimentBoard = board.copy()
				experimentBoard.push(move)
				value = self.alphabeta(experimentBoard, depth - 1, alpha, beta, True)
				bestValue = min(bestValue, value)
				beta = min(beta, bestValue)
				if alpha >= beta:
					break
			return bestValue

		return 0

	def boardValue(self, board):
		return nn.predict2(self.board_to_row(board))

	def board_to_row(board):
		row = []
		boardString = board.fen().split()[0]
		row.append(boardString.count("P"))
		row.append(boardString.count("p"))
		row.append(boardString.count("R"))
		row.append(boardString.count("r"))
		row.append(boardString.count("N"))
		row.append(boardString.count("n"))
		row.append(boardString.count("B"))
		row.append(boardString.count("b"))
		row.append(boardString.count("Q"))
		row.append(boardString.count("q"))
		row.append(board.turn)
		return row

	def user_move(self, userMove):
		print('user : ',userMove)
		self.gameBoard.push(chess.Move.from_uci(userMove))

	def makeMove(self):
		minValue = float("inf")
		minMove = None
		for move in self.gameBoard.legal_moves:
			experimentBoard = self.gameBoard.copy()
			experimentBoard.push(move)
			value = self.alphabeta(experimentBoard,  3, float("-inf"), float("inf"), False)

			if value < minValue:
				minValue = value
				minMove = move
		print('computer : ',str(minMove))
		self.gameBoard.push(minMove)
		return minMove

	def simulateTurn(self,temp,color,guiBoard):
		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"
		
		self.myPieces = [] # location, value
		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						self.myPieces.append([[r,c],temp[r][c]])
		
		validMoves = []
		for p in self.myPieces:
			if p[1]%6 == 1:
				possibleMoves = guiBoard.detPonSpaces(temp,p[0],color)[:]
			elif p[1]%6 == 2:
				possibleMoves = guiBoard.detKnightSpaces(temp,p[0],color)[:]
			elif p[1]%6 == 3:
				possibleMoves = guiBoard.detBishopSpaces(temp,p[0],antiColor)[:]
			elif p[1]%6 == 4:
				possibleMoves = guiBoard.detRookSpaces(temp,p[0],antiColor)[:]
			elif p[1]%6 == 5:
				possibleMoves = guiBoard.detQueenSpaces(temp,p[0],antiColor)[:]
			else:
				possibleMoves = guiBoard.detKingSpaces(temp,p[0],color)[:]
				
			for m in possibleMoves:
				if p[1]%6 == 2 or p[1]%6 == 0:
					if 0 <= m[0] < 8 and  0 <= m[1] < 8 and guiBoard.turnValid(temp,p[0],m,color):
						moveGrid = [0]*8
						for i in range(len(moveGrid)):
							moveGrid[i] = temp[i][:]
						value = moveGrid[m[0]][m[1]]%6
						if guiBoard.inCheck(moveGrid,color):
							value += 3
						moveGrid[m[0]][m[1]] = p[1]; moveGrid[p[0][0]][p[0][1]] = 0
						if guiBoard.inCheck(moveGrid,antiColor):
							value += 3
						validMoves.append([moveGrid,p[0],m,value,[]])
				else:
#					moveGrid = [0]*8
#					for i in range(len(moveGrid)):
#						moveGrid[i] = temp[i][:]
					moveGrid = copy.deepcopy(temp)
					value = moveGrid[m[0]][m[1]]%6
					if guiBoard.inCheck(moveGrid,color):
						value += 3
					moveGrid[m[0]][m[1]] = p[1]; moveGrid[p[0][0]][p[0][1]] = 0
					if not guiBoard.inCheck(moveGrid,color):
						if guiBoard.inCheck(moveGrid,antiColor):
							value += 3
						if p[1]%6 == 1 and (m[0] == 8 or m[0] == 0):
							value += 5
						validMoves.append([moveGrid,p[0],m,value,[]])
		return validMoves

	def makeMove2(self,guiBoard,color):
		#		temp = [0]*8
#		for i in range(len(temp)):
#			temp[i]=guiBoard.grid[i][:]
		temp = copy.deepcopy(guiBoard.grid)
		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"
			
		first = self.simulateTurn(temp,color,guiBoard)[:]
		for fmove in first:
			fmove[4] = self.simulateTurn(fmove[0],antiColor,guiBoard)[:]
			for smove in fmove[4]:
				smove[4] = self.simulateTurn(smove[0],color,guiBoard)[:]
		
		for f in first:
			maxVal2 = -100
			for g in f[4]:
				maxVal3 = 0
				for h in g[4]:
					if h[3] > maxVal3:
						maxVal3 = h[3]
				g[3] = g[3] - maxVal3
				if g[3] > maxVal2:
					maxVal2 = g[3]
			f[3] = f[3] - maxVal2
		
		bestMoves = []
		maxValue = 0
		for v in first:
			if v[3] > maxValue:
				bestMoves = []
				bestMoves.append(v)
				maxValue = v[3]
			elif v[3] == maxValue:
				bestMoves.append(v)
#		for b in bestMoves:
#			print(b[1],b[2],b[3])
		try:
			return choice(bestMoves)
		except:
			return choice(first)
					
				