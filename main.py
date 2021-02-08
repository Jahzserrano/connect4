import random


# This function draw the board on the console
def drawBoard(board):
    print()
    print(f"|{board[0][0]}|{board[0][1]}|{board[0][2]}|{board[0][3]}|{board[0][4]}|{board[0][5]}|{board[0][6]}|")
    print("--+-+-+-+-+-+--")
    print(f"|{board[1][0]}|{board[1][1]}|{board[1][2]}|{board[1][3]}|{board[1][4]}|{board[1][5]}|{board[1][6]}|")
    print("--+-+-+-+-+-+--")
    print(f"|{board[2][0]}|{board[2][1]}|{board[2][2]}|{board[2][3]}|{board[2][4]}|{board[2][5]}|{board[2][6]}|")
    print("--+-+-+-+-+-+--")
    print(f"|{board[3][0]}|{board[3][1]}|{board[3][2]}|{board[3][3]}|{board[3][4]}|{board[3][5]}|{board[3][6]}|")
    print("--+-+-+-+-+-+--")
    print(f"|{board[4][0]}|{board[4][1]}|{board[4][2]}|{board[4][3]}|{board[4][4]}|{board[4][5]}|{board[4][6]}|")
    print("--+-+-+-+-+-+--")
    print(f"|{board[5][0]}|{board[5][1]}|{board[5][2]}|{board[5][3]}|{board[5][4]}|{board[5][5]}|{board[5][6]}|")
    print("---------------")
    print()


# This function ask for the player choice
def getPlayerLetter():
    choice = ''
    while choice not in 'X O'.split():
        print("Choose X or O?")
        choice = input().upper().strip()
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# This function return randomly the turn of the player
def getTurn():
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'


# This function verify if the input is correct
def getPlayerMove(board):
    column = ''
    while True:
        if column in '1 2 3 4 5 6 7'.split() and isColumnFree(board, int(column) - 1):
            return (int(column) - 1)
        else:
            print('What is your next move? 1-7')
            column = input().strip()


# This function is AI that thonk the next move of the computer
def getComputerMove(board, computerLetter):
    # Check the player letter
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # First, check if we can win in the next move
    for column in range(7):
        boardCopy = getBoardCopy(board)
        if isColumnFree(boardCopy, column):
            makeMove(boardCopy, column, computerLetter)
            if isWinner(boardCopy, computerLetter):
                return column

    # Check if the player could win on his nextmove, and block them
    for column in range(7):
        boardCopy = getBoardCopy(board)
        if isColumnFree(boardCopy, column):
            makeMove(boardCopy, column, playerLetter)
            if isWinner(boardCopy, playerLetter):
                return column

    # Make a aleatory move
    move = chooseRandomMove(board, [0, 1, 2, 3, 4, 5, 6])
    if move != None:
        return move


def chooseRandomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isColumnFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# This function check all the posibilities of winnig
def isWinner(board, letter):
    # This algoritism check the rows
    for row in range(len(board)):
        for column in range(len(board[row])):
            if isConnectFourRow(board, row, column, letter):
                return True

    # This algoritism check the columns
    for column in range(7):
        for row in range(6):
            if isConnectFourColumn(board, column, row, letter):
                return True

    # This algoritism check for diagonal
    for row in range(6):
        for column in range(7):
            if isConnectFourDiagonal(board, row, column, letter):
                return True

    # This algoritism check for diagonal ascendente
    for row in range(6):
        for column in range(1, 7):
            if isConnectFourDiagonal(board, row, column, letter):
                return True
    return False


def isConnectFourDiagonalReverse(board, row, column, letter):
    try:
        acum = 0
        for i in range(4):
            if board[row + i][(column + i) * -1] == letter:
                acum = acum + 1
            if acum == 4:
                return True
        return False
    except IndexError:
        return False


def isConnectFourDiagonal(board, row, column, letter):
    try:
        acum = 0
        for i in range(4):
            if board[row + i][column + i] == letter:
                acum = acum + 1
            if acum == 4:
                return True
        return False
    except IndexError:
        return False


def isConnectFourRow(board, row, column, letter):
    try:
        acum = 0
        for i in range(4):
            if board[row][column + i] == letter:
                acum = acum + 1
            if acum == 4:
                return True
        return False
    except IndexError:
        return False


def isConnectFourColumn(board, column, row, letter):
    try:
        acum = 0
        for i in range(4):
            if board[row + i][column] == letter:
                acum = acum + 1
            if acum == 4:
                return True
        return False
    except IndexError:
        return False


# This function create a copy of the original board
def getBoardCopy(board):
    boardCopy = [[' '] * 7 for i in range(6)]
    for row in range(len(board)):
        for column in range(len(board[row])):
            boardCopy[row][column] = board[row][column]
    return boardCopy


# This function check if the Column selected is free
def isColumnFree(board, column):
    for row in range(6):
        if board[row][column] == ' ':
            return True
    return False


# This function make the players move
def makeMove(board, column, playerLetter):
    for row in range(len(board)):
        if board[row][column] == ' ' and not isNextRowEmpty(board, row, column):
            board[row][column] = playerLetter
            break

        # This function check if there's a space in teh row


def isNextRowEmpty(board, row, col):
    try:
        if board[row + 1][col] == ' ':
            return True
    except IndexError:
        return False


# This function check if the board is full
def isBoardFull(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == ' ':
                return False
    return True

def main():
    while True:
        # The Games begins
        board = [[' '] * 7 for i in range(6)]
        playerLetter, computerLetter = getPlayerLetter()
        turn = getTurn()
        print('The ' + turn + ' will go first.')
        print(f"You're {playerLetter} don't forget it")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                drawBoard(board)
                move = getPlayerMove(board)
                makeMove(board, move, playerLetter)
                if isWinner(board, playerLetter):
                    drawBoard()
                    print("CONNECT 4! YOU WON")
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        drawBoard(board)
                        print('Tie! nobody wons or both wons')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer turn
                move = getComputerMove(board, computerLetter)
                makeMove(board, move, computerLetter)
                if isWinner(board, computerLetter):
                    drawBoard(board)
                    print("CONNECT 4! YOU LOSE")
                    gameIsPlaying = False
                else:
                    if isBoardFull(board):
                        drawBoard(board)
                        print('Tie! nobody wons or both wons')
                        break
                    else:
                        turn = 'player'

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break

if __name__ == '__main__':
    main()