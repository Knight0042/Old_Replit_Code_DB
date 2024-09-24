player, opponent = 'x', 'o'


def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(0, 3):

        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:

            if b[row][0] == 'x':
                return 10
            elif b[row][0] == 'o':
                return -10

    # Checking for Columns for X or O victory.
    for col in range(0, 3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == 'x':
                return 10
            elif b[0][col] == 'o':
                return -10

    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == 'x':
            return 10
        elif b[0][0] == 'o':
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == 'x':
            return 10
        elif b[0][2] == 'o':
            return -10

    # Else if none of them have won then return 0
    return 0


def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False


def minimax(board, depth, isMaximizingPlayer):
    score = evaluate(board)
    if (score == 10):
        return score
    if (score == -10):
        return score
    if (isMovesLeft(board) == False):
        return 0
    if isMaximizingPlayer:
        best = -1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] == player
                    best = max(best, minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMaximizingPlayer))
                    board[i][j] = '_'
        return best


def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    print('The value of the best move is ', bestMove)
    return bestMove


board = [['_', '_', ''],
         ['_', '_', '_'],
         ['_', '_', '_']]
bestMove = findBestMove(board)
print("ROW:", bestMove[0], " COL:", bestMove[1])

# rndx = True
# game = True
# rndo = False
# print("TIC TAC TOE")
# print("~~~Instructions~~~")
# print("The first person will be X and the second will be O")
# print("In order to pick where you want the x or o to go, you have to type a certain number.")
# print("So its a grid like this, you type the number that corresponds to that grid slot.")
# print("_1_|_2_|_3_")
# print("_4_|_5_|_6_")
# print(" 7 | 8 | 9 ")
# print("A 1 on the grid indicates an X while a 2 indicates an O")
# print("DO NOT USE THE SAME NUMBER TWICE")
# while game:
#   if rndx:
#       move = int(input('Choose a space - '))
#       if move == 1:
#           Thing[0][0] = 'x'
#       elif move == 2:
#           Thing[0][1] = 'x'
#       elif move == 3:
#           Thing[0][2] = 'x'
#       elif move == 4:
#           Thing[1][0] = 'x'
#       elif move == 5:
#           Thing[1][1] = 'x'
#       elif move == 6:
#           Thing[1][2] = 'x'
#       elif move == 7:
#           Thing[2][0] = 'x'
#       elif move == 8:
#           Thing[2][1] = 'x'
#       elif move == 9:
#           Thing[2][2] = 'x'
#       print(Thing[0])
#       print(Thing[1])
#       print(Thing[2])
#       rndo = True
#       rndx = False
#       if Thing[0][1] == 'x' and Thing[0][0] == 'x' and Thing[0][2] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[0][0] == 'x' and Thing[1][0] == 'x' and Thing[2][0] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[0][0] == 'x' and Thing[1][1] == 'x' and Thing[2][2] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[0][1] == 'x' and Thing[1][1] == 'x' and Thing[2][1] == 1:
#           print('X Wins')
#           game = False
#       elif Thing[0][2] == 'x' and Thing[1][2] == 'x' and Thing[2][2] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[1][0] == 'x' and Thing[1][1] == 'x' and Thing[1][2] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[0][2] == 'x' and Thing[1][1] == 'x' and Thing[2][0] == 'x':
#           print('X Wins')
#           game = False
#       elif Thing[2][0] == 'x' and Thing[2][1] == 'x' and Thing[2][2] == 'x':
#           print('X Wins')
#           game = False
#   elif rndo:
#       move = int(input('Choose a space - '))
#       if move == 1:
#           Thing[0][0] = 'o'
#       elif move == 2:
#           Thing[0][1] = 'o'
#       elif move == 3:
#           Thing[0][2] = 'o'
#       elif move == 4:
#           Thing[1][0] = 'o'
#       elif move == 5:
#           Thing[1][1] = 'o'
#       elif move == 6:
#           Thing[1][2] = 'o'
#       elif move == 7:
#           Thing[2][0] = 'o'
#       elif move == 8:
#           Thing[2][1] = 'o'
#       elif move == 9:
#           Thing[2][2] = 'o'
#       print(Thing[0])
#       print(Thing[1])
#       print(Thing[2])
#       rndx = True
#       rndo = False
#       if Thing[0][1] == 'o' and Thing[0][0] == 'o' and Thing[0][2] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[0][0] == 'o' and Thing[1][0] == 'o' and Thing[2][0] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[0][0] == 'o' and Thing[1][1] == 'o' and Thing[2][2] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[0][1] == 'o' and Thing[1][1] == 'o' and Thing[2][1] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[0][2] == 'o' and Thing[1][2] == 'o' and Thing[2][2] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[1][0] == 'o' and Thing[1][1] == 'o' and Thing[1][2] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[0][2] == 'o' and Thing[1][1] == 'o' and Thing[2][0] == 'o':
#           print('O Wins')
#           game = False
#       elif Thing[2][0] == 'o' and Thing[2][1] == 'o' and Thing[2][2] == 'o':
#           print('O Wins')
#           game = False
# if __name__ == "__main__":
#   value = evaluate(Thing)
#   print("The value of this board is", value)
# print(Thing[0])
# print(Thing[1])
# print(Thing[2])
