def winner(board):
	'''When run, function checks to see if the game has been won.
	Board should be input as a list of 'X', 'O', and ' ' representing the state of the board'''
	if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
		return board[0]
	if board[3] == board[4] and board[4] == board[5] and board[3] != " ":
		return board[3]
	if board[6] == board[7] and board[7] == board[8] and board[6] != " ":
		return board[6]
	if board[0] == board[3] and board[3] == board[6] and board[0] != " ":
		return board[0]
	if board[1] == board[4] and board[4] == board[7] and board[1] != " ":
		return board[1]
	if board[2] == board[5] and board[5] == board[8] and board[2] != " ":
		return board[2]
	if board[0] == board[4] and board[4] == board[8] and board[0] != " ":
		return board[0]
	if board[2] == board[4] and board[4] == board[6] and board[2] != " ":
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
