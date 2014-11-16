import random

def checkWinner(board):
	'''When run, function checks to see if the game has been won.
	Board should be input as a list of 'X', 'O', and ' ' representing the state of the board'''
	if ' ' not in board:
		return 'Cat'
	if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
		return board[0]
	if board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
		return board[3]
	if board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
		return board[6]
	if board[0] == board[3] and board[3] == board[6] and board[0] != ' ':
		return board[0]
	if board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
		return board[1]
	if board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
		return board[2]
	if board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
		return board[0]
	if board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
		return board[2]
		
def displayBoard(board):
    '''Display tic-tac-toe board.
    board is a list of 'X', 'O', and ' ' representing the state of the board'''
    
    display = board[:]
    for i in range(6):
        if display[i] is ' ':
            display[i] = '_'
    for i in range(0,9,3):
        print display[0+i] + '|' + display[1+i] + '|' + display[2+i]

def checkLegalMove(move, board):
    if move in range(9):
        if board[move] is ' ':
            return True
    return False

def mover(turn):
	if turn % 2 == 0:
		return 'o'
	else:
		return 'x'

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 1
winner = None

def easyComputer(board):
    '''Tic-tac-toe easy computer opponent.
    Receives a board and returns a random legal move.'''
    
    legal_moves = [i for i, x in enumerate(board) if x == ' ']
    return random.choice(legal_moves)

print 'Welcome to Tic Tac Toe, when you enter the number of the square you want to move in, keep in mind that spaces are numbered like you would read a book. The numbers start at 1 and end at 9.'
choice = input("Please input 1 for Human v. Human and 2 for Human v. Computer: ")
if choice == 1:
	while winner != 'x' and winner != 'o' and winner != 'Cat':
		
		displayBoard(board)
		
		move = input('Please enter the space number you would like to move in: ') - 1
		
		if checkLegalMove(move, board):
			board[move] = mover(turn)
			turn = turn + 1
		else:
			print 'Please enter a valid move'
		
		winner = checkWinner(board)
		
	print winner + " won!"
else:
	difficulty = input("Enter 1 for easy difficulty, 2 for medium, and 3 for hard: ")
	if difficulty == 1:
		while winner != 'x' and winner != 'o' and winner!= 'Cat':
			if turn % 2 != 0:
				displayBoard(board)
				
				move = input('Please enter the space number you would like to move in: ') - 1
				
				if checkLegalMove(move, board):
					board[move] = mover(turn)
					turn = turn + 1
				else:
					print 'Please enter a valid move'
					
				winner = checkWinner(board)
			else:
				move = input(easyComputer(board))
		print winner + " won!"
	if difficulty == 2:
		while winner != 'x' and winner != 'o' and winner!= 'Cat':
			if turn % 2 != 0:
				displayBoard(board)
				
				move = input('Please enter the space number you would like to move in: ') - 1
				
				if checkLegalMove(move, board):
					board[move] = mover(turn)
					turn = turn + 1
				else:
					print 'Please enter a valid move'
					
				winner = checkWinner(board)
			else:
				move = input(mediumComputer(board))
		print winner + " won!
	if difficulty == 3:
		while winner != 'x' and winner != 'o' and winner!= 'Cat':
			if turn % 2 != 0:
				displayBoard(board)
				
				move = input('Please enter the space number you would like to move in: ') - 1
				
				if checkLegalMove(move, board):
					board[move] = mover(turn)
					turn = turn + 1
				else:
					print 'Please enter a valid move'
					
				winner = checkWinner(board)
			else:
				move = input(hardComputer(board))
		print winner + " won!