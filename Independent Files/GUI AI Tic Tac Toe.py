import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
dis_width = 450
dis_height = 450
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont("bahnschrift", 100)
x_mesg = font.render('X WINS', True, white)
o_mesg = font.render('O WINS', True, white)
tie_mesg = font.render('TIE', True, white)


def x_win_message():
    dis.blit(x_mesg, [100, dis_height / 2 - 10])


def o_win_message():
    dis.blit(o_mesg, [100, dis_height / 2 - 10])


def no_win_message():
    dis.blit(tie_mesg, [100, dis_height / 2 - 10])


def gameloop2():
    dis.fill(black)
    pygame.display.flip()
    final_count = 0
    x1 = 50
    y1 = 50
    x2 = 170
    y2 = 50
    x3 = 290
    y3 = 50
    x4 = 50
    y4 = 170
    x5 = 170
    y5 = 170
    x6 = 290
    y6 = 170
    x7 = 50
    y7 = 290
    x8 = 170
    y8 = 290
    x9 = 290
    y9 = 290
    # Python3 program to find the next optimal move for a player
    player, opponent = 'x', 'o'

    # This function returns true if there are moves
    # remaining on the board. It returns false if
    # there are no moves left to play.
    def isMovesLeft(board):

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    return True
        return False

    # This is the evaluation function as discussed
    # in the previous article ( http://goo.gl/sJgv68 )
    def evaluate(b):

        # Checking for Rows for X or O victory.
        for row in range(3):
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == player):
                    return 10
                elif (b[row][0] == opponent):
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3):

            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

                if (b[0][col] == player):
                    return 10
                elif (b[0][col] == opponent):
                    return -10

        # Checking for Diagonals for X or O victory.
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

            if (b[0][0] == player):
                return 10
            elif (b[0][0] == opponent):
                return -10

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

            if (b[0][2] == player):
                return 10
            elif (b[0][2] == opponent):
                return -10

        # Else if none of them have won then return 0
        return 0

    # This is the minimax function. It considers all
    # the possible ways the game can go and returns
    # the value of the board
    def minimax(board, depth, isMax):
        score = evaluate(board)

        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 10):
            return score

        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -10):
            return score

        # If there are no more moves and no winner then
        # it is a tie
        if (isMovesLeft(board) == False):
            return 0

        # If this maximizer's move
        if (isMax):
            best = -1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if (board[i][j] == '_'):
                        # Make the move
                        board[i][j] = player

                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, minimax(board,
                                                 depth + 1,
                                                 not isMax))

                        # Undo the move
                        board[i][j] = '_'
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if (board[i][j] == '_'):
                        # Make the move
                        board[i][j] = opponent

                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, minimax(board, depth + 1, not isMax))

                        # Undo the move
                        board[i][j] = '_'
            return best

    # This will return the best possible move for the player
    def findBestMove(board):
        bestVal = -1000
        bestMove = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '_'):

                    # Make the move
                    board[i][j] = player

                    # compute evaluation function for this
                    # move.
                    moveVal = minimax(board, 0, False)

                    # Undo the move
                    board[i][j] = '_'

                    if (moveVal > bestVal):
                        bestMove = (i, j)
                        bestVal = moveVal

        return bestMove

    #  test = True
    #  thing = 0
    # xImg = pygame.image.load('X_modified.png')
    # x_img = pygame.transform.scale(xImg, (80, 80))
    square_width = 100
    square_height = 100
    x_width = 50
    x_height = 50
    running = True

    # all_sprites = []
    class x(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)
            # pygame.draw.line(self.image, color, [0, 0], [0, 0], width)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()

    class square(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()

    square1 = square(black, square_width, square_height)
    square1.rect.x = x1
    square1.rect.y = y1
    square2 = square(black, square_width, square_height)
    square2.rect.x = x2
    square2.rect.y = y2
    square3 = square(black, square_width, square_height)
    square3.rect.x = x3
    square3.rect.y = y3
    square4 = square(black, square_width, square_height)
    square4.rect.x = x4
    square4.rect.y = y4
    square5 = square(black, square_width, square_height)
    square5.rect.x = x5
    square5.rect.y = y5
    square6 = square(black, square_width, square_height)
    square6.rect.x = x6
    square6.rect.y = y6
    square7 = square(black, square_width, square_height)
    square7.rect.x = x7
    square7.rect.y = y7
    square8 = square(black, square_width, square_height)
    square8.rect.x = x8
    square8.rect.y = y8
    square9 = square(black, square_width, square_height)
    square9.rect.x = x9
    square9.rect.y = y9
    all_sprites = pygame.sprite.Group()
    all_sprites.add(square1)
    all_sprites.add(square2)
    all_sprites.add(square3)
    all_sprites.add(square4)
    all_sprites.add(square5)
    all_sprites.add(square6)
    all_sprites.add(square7)
    all_sprites.add(square8)
    all_sprites.add(square9)
    x__1 = False
    x__2 = False
    x__3 = False
    x__4 = False
    x__5 = False
    x__6 = False
    x__7 = False
    x__8 = False
    x__9 = False
    o__1 = False
    o__2 = False
    o__3 = False
    o__4 = False
    o__5 = False
    o__6 = False
    o__7 = False
    o__8 = False
    o__9 = False
    x_move = True
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    while running:
        def xwincondition():
            # win = False
            # while not win:
            if x__1 == True and x__2 == True and x__3 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                # win = True
                running = False
            elif x__1 == True and x__4 == True and x__7 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__1 == True and x__5 == True and x__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__2 == True and x__5 == True and x__8 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__3 == True and x__6 == True and x__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__3 == True and x__5 == True and x__7 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__4 == True and x__5 == True and x__6 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif x__7 == True and x__8 == True and x__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif final_count >= 9:
                pygame.time.wait(1000)
                dis.fill(black)
                no_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # else:
                #   win == False

        def owincondition():
            if o__1 == True and o__2 == True and o__3 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__1 == True and o__4 == True and o__7 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__1 == True and o__5 == True and o__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__2 == True and o__5 == True and o__8 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__3 == True and o__6 == True and o__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__3 == True and o__5 == True and o__7 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__4 == True and o__5 == True and o__6 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif o__7 == True and o__8 == True and o__9 == True:
                pygame.time.wait(1000)
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False
                # win = True
            elif final_count >= 9:
                pygame.time.wait(1000)
                dis.fill(black)
                no_win_message()
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()
                quit()
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    xwincondition()
                    owincondition()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                for i in clicked_sprites:
                    if i == square1 and x__1 == False and o__1 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 100], 30, 5)
                        o__1 = True
                        x_move = True
                        board[0][0] = 'o'
                        final_count += 1
                    if i == square2 and x__2 == False and o__2 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 100], 30, 5)
                        o__2 = True
                        x_move = True
                        board[0][1] = 'o'
                        final_count += 1
                    if i == square3 and x__3 == False and o__3 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 100], 30, 5)
                        o__3 = True
                        x_move = True
                        board[0][2] = 'o'
                        final_count += 1
                    if i == square4 and x__4 == False and o__4 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 220], 30, 5)
                        o__4 = True
                        x_move = True
                        board[1][0] = 'o'
                        final_count += 1
                    if i == square5 and x__5 == False and o__5 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 220], 30, 5)
                        o__5 = True
                        x_move = True
                        board[1][1] = 'o'
                        final_count += 1
                    if i == square6 and x__6 == False and o__6 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 220], 30, 5)
                        o__6 = True
                        x_move = True
                        board[1][2] = 'o'
                        final_count += 1
                    if i == square7 and x__7 == False and o__7 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 340], 30, 5)
                        o__7 = True
                        x_move = True
                        board[2][0] = 'o'
                        final_count += 1
                    if i == square8 and x__8 == False and o__8 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 340], 30, 5)
                        o__8 = True
                        x_move = True
                        board[2][1] = 'o'
                        final_count += 1
                    if i == square9 and x__9 == False and o__9 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 340], 30, 5)
                        o__9 = True
                        x_move = True
                        board[2][2] = 'o'
                        final_count += 1
        if x_move:
            if final_count == 0:
                board[0][0] = 'x'
            else:
                bestMove = findBestMove(board)
                board[bestMove[0]][bestMove[1]] = 'x'
            for row in range(3):
                for column in range(3):
                    if board[0][0] == 'x':
                        pygame.draw.line(dis, white, [75, 75 + x_height], [75 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [75, 75], [75 + x_width, 75 + x_height], 10)
                        #  x_1 = x(white, x_width, x_height)
                        #  all_sprites.add(x_1)
                        #  x_1.rect.x = (75)
                        #  x_1.rect.y = (75)
                        x__1 = True
                    if board[0][1] == 'x':
                        pygame.draw.line(dis, white, [195, 75 + x_height], [195 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [195, 75], [195 + x_width, 75 + x_height], 10)
                        #  x_2 = x(white, x_width, x_height)
                        #  all_sprites.add(x_2)
                        #  x_2.rect.x = (195)
                        #  x_2.rect.y = (75)
                        x__2 = True
                    if board[0][2] == 'x':
                        pygame.draw.line(dis, white, [305, 75 + x_height], [305 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [305 + x_width, 75 + x_height], [305, 75], 10)
                        x__3 = True
                    if board[1][0] == 'x':
                        pygame.draw.line(dis, white, [75, 195 + x_height], [75 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [75, 195], [75 + x_width, 195 + x_height], 10)
                    if board[1][1] == 'x':
                        pygame.draw.line(dis, white, [195, 195 + x_height], [195 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [195, 195], [195 + x_width, 195 + x_height], 10)
                        x__5 = True

                    if board[1][2] == 'x':
                        pygame.draw.line(dis, white, [305, 195 + x_height], [305 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [305, 195], [305 + x_width, 195 + x_height], 10)
                        x__6 = True

                    if board[2][0] == 'x':
                        pygame.draw.line(dis, white, [75, 305 + x_height], [75 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [75, 305], [75 + x_width, 305 + x_height], 10)
                        x__7 = True

                    if board[2][1] == 'x':
                        pygame.draw.line(dis, white, [195, 305 + x_height], [195 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [195, 305], [195 + x_width, 305 + x_height], 10)
                        x__7 = True

                    if board[2][2] == 'x':
                        pygame.draw.line(dis, white, [305, 305 + x_height], [305 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [305, 305], [305 + x_width, 305 + x_height], 10)
                        x__9 = True

            final_count += 1
            pygame.display.flip()
            x_move = False

        all_sprites.draw(dis)

        pygame.draw.line(dis, white, [160, 50], [160, 400], 5)
        pygame.draw.line(dis, white, [280, 50], [280, 400], 5)
        pygame.draw.line(dis, white, [50, 160], [400, 160], 5)
        pygame.draw.line(dis, white, [50, 280], [400, 280], 5)
        pygame.display.flip()
        xwincondition()
        owincondition()
        if final_count >= 9:
            no_win_message()
            pygame.display.flip()
        clock.tick(60)


gameloop2()
pygame.quit()
quit()
