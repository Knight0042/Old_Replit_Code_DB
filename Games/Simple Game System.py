import pygame
import random
from random import randint

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
dis_width = 800
dis_height = 500
paddle_height = 100
paddle_width = 10
initiate = True
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Simple Games System')

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - 325, dis_height / 2 - 10])


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

    # class o(pygame.sprite.Sprite):
    #   def __init__(self, color, width, height):
    #     super().__init__()
    #     self.image = pygame.Surface([width, height])
    #     self.image.fill(black)
    #     self.image.set_colorkey(black)
    #     # pygame.draw.line(self.image, color, [0, 0], [0, 0], width)
    #     pygame.draw.circle(self.image, color, [0, 0], 10)
    #     self.rect = self.image.get_rect()

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
    while running:
        def xwincondition():
            # win = False
            # while not win:
            if x__1 == True and x__2 == True and x__3 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                # win = True
                running = False
            elif x__1 == True and x__4 == True and x__7 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__1 == True and x__5 == True and x__9 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__2 == True and x__5 == True and x__8 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__3 == True and x__6 == True and x__9 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__3 == True and x__5 == True and x__7 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__4 == True and x__5 == True and x__6 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif x__7 == True and x__8 == True and x__9 == True:
                dis.fill(black)
                x_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif final_count >= 9:
                dis.fill(black)
                no_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # else:
                #   win == False

        def owincondition():
            if o__1 == True and o__2 == True and o__3 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__1 == True and o__4 == True and o__7 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__1 == True and o__5 == True and o__9 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__2 == True and o__5 == True and o__8 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__3 == True and o__6 == True and o__9 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__3 == True and o__5 == True and o__7 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__4 == True and o__5 == True and o__6 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif o__7 == True and o__8 == True and o__9 == True:
                dis.fill(black)
                o_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
                running = False
                # win = True
            elif final_count >= 9:
                dis.fill(black)
                no_win_message()
                pygame.display.flip()
                pygame.time.wait(500)
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
                    if i == square1 and x__1 == False and o__1 == False and x_move == True:
                        pygame.draw.line(dis, white, [75, 75 + x_height], [75 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [75, 75], [75 + x_width, 75 + x_height], 10)
                        x__1 = True
                        x_move = False
                        final_count += 1
                    if i == square2 and x__2 == False and o__2 == False and x_move == True:
                        pygame.draw.line(dis, white, [195, 75 + x_height], [195 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [195, 75], [195 + x_width, 75 + x_height], 10)
                        x__2 = True
                        x_move = False
                        final_count += 1
                    if i == square3 and x__3 == False and o__3 == False and x_move == True:
                        pygame.draw.line(dis, white, [305, 75 + x_height], [305 + x_width, 75], 10)
                        pygame.draw.line(dis, white, [305 + x_width, 75 + x_height], [305, 75], 10)
                        x__3 = True
                        x_move = False
                        final_count += 1
                    if i == square4 and x__4 == False and o__4 == False and x_move == True:
                        pygame.draw.line(dis, white, [75, 195 + x_height], [75 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [75, 195], [75 + x_width, 195 + x_height], 10)
                        x__4 = True
                        final_count += 1
                        x_move = False
                    if i == square5 and x__5 == False and o__5 == False and x_move == True:
                        pygame.draw.line(dis, white, [195, 195 + x_height], [195 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [195, 195], [195 + x_width, 195 + x_height], 10)
                        x__5 = True
                        x_move = False
                        final_count += 1
                    if i == square6 and x__6 == False and o__6 == False and x_move == True:
                        pygame.draw.line(dis, white, [305, 195 + x_height], [305 + x_width, 195], 10)
                        pygame.draw.line(dis, white, [305, 195], [305 + x_width, 195 + x_height], 10)
                        x__6 = True
                        x_move = False
                        final_count += 1
                    if i == square7 and x__7 == False and o__7 == False and x_move == True:
                        pygame.draw.line(dis, white, [75, 305 + x_height], [75 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [75, 305], [75 + x_width, 305 + x_height], 10)
                        x__7 = True
                        x_move = False
                        final_count += 1
                    if i == square8 and x__8 == False and o__8 == False and x_move == True:
                        pygame.draw.line(dis, white, [195, 305 + x_height], [195 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [195, 305], [195 + x_width, 305 + x_height], 10)
                        x__8 = True
                        x_move = False
                        final_count += 1
                    if i == square9 and x__9 == False and o__9 == False and x_move == True:
                        pygame.draw.line(dis, white, [305, 305 + x_height], [305 + x_width, 305], 10)
                        pygame.draw.line(dis, white, [305, 305], [305 + x_width, 305 + x_height], 10)
                        x__9 = True
                        x_move = False
                        final_count += 1

                    if i == square1 and x__1 == False and o__1 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 100], 30, 5)
                        o__1 = True
                        x_move = True
                        final_count += 1
                    if i == square2 and x__2 == False and o__2 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 100], 30, 5)
                        o__2 = True
                        x_move = True
                        final_count += 1
                    if i == square3 and x__3 == False and o__3 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 100], 30, 5)
                        o__3 = True
                        x_move = True
                        final_count += 1
                    if i == square4 and x__4 == False and o__4 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 220], 30, 5)
                        o__4 = True
                        x_move = True
                        final_count += 1
                    if i == square5 and x__5 == False and o__5 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 220], 30, 5)
                        o__5 = True
                        x_move = True
                        final_count += 1
                    if i == square6 and x__6 == False and o__6 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 220], 30, 5)
                        o__6 = True
                        x_move = True
                        final_count += 1
                    if i == square7 and x__7 == False and o__7 == False and x_move == False:
                        pygame.draw.circle(dis, white, [100, 340], 30, 5)
                        o__7 = True
                        x_move = True
                        final_count += 1
                    if i == square8 and x__8 == False and o__8 == False and x_move == False:
                        pygame.draw.circle(dis, white, [220, 340], 30, 5)
                        o__8 = True
                        x_move = True
                        final_count += 1
                    if i == square9 and x__9 == False and o__9 == False and x_move == False:
                        pygame.draw.circle(dis, white, [340, 340], 30, 5)
                        o__9 = True
                        x_move = True
                        final_count += 1

        all_sprites.draw(dis)

        pygame.draw.line(dis, white, [160, 50], [160, 400], 5)
        pygame.draw.line(dis, white, [280, 50], [280, 400], 5)
        pygame.draw.line(dis, white, [50, 160], [400, 160], 5)
        pygame.draw.line(dis, white, [50, 280], [400, 280], 5)
        xwincondition()
        owincondition()
        if final_count >= 9:
            no_win_message()

        pygame.display.flip()
        clock.tick(60)


def gameLoop1():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)


def gameloop():
    x1 = 25
    y1 = dis_height / 2

    x2 = dis_width - 35
    y2 = dis_height / 2

    x3 = dis_width / 2
    y3 = dis_height / 2

    ball_size = 10
    score1 = 0
    score2 = 0

    def pong_ball():
        pygame.draw.rect(dis, white, [x3, y3, ball_size, ball_size])

    class Paddle(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()

        def moveUp(self, pixels):
            self.rect.y -= pixels
            if self.rect.y < 0:
                self.rect.y = 0

        def moveDown(self, pixels):
            self.rect.y += pixels
            if self.rect.y > (dis_height - paddle_height):
                self.rect.y = (dis_height - paddle_height)

    class Ball(pygame.sprite.Sprite):
        # This class represents a ball. It derives from the "Sprite" class in Pygame.

        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Pass in the color of the ball, its width and height.
            # Set the background color and set it to be transparent
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)

            # Draw the ball (a rectangle!)
            pygame.draw.rect(self.image, color, [0, 0, width, height])

            self.velocity = [randint(4, 8), randint(-8, 8)]

            # Fetch the rectangle object that has the dimensions of the image.
            self.rect = self.image.get_rect()

        def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

        def bounce(self):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8, 8)

    paddle1 = Paddle(white, paddle_width, paddle_height)
    paddle1.rect.x = x1
    paddle1.rect.y = y1
    paddle2 = Paddle(white, paddle_width, paddle_height)
    paddle2.rect.x = x2
    paddle2.rect.y = y2
    ball = Ball(white, ball_size, ball_size)
    ball.rect.x = x3
    ball.rect.y = y3
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddle1)
    all_sprites_list.add(paddle2)
    all_sprites_list.add(ball)
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.moveUp(5)
        if keys[pygame.K_s]:
            paddle1.moveDown(5)
        if keys[pygame.K_UP]:
            paddle2.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddle2.moveDown(5)
        all_sprites_list.update()
        if ball.rect.x >= (dis_width - ball_size):
            score1 += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            score2 += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > (dis_height - ball_size):
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
            ball.bounce()
        dis.fill(black)
        pygame.draw.line(dis, white, [((dis_width / 2) - 5), 0], [((dis_width / 2) - 5), dis_height], 5)
        all_sprites_list.draw(dis)
        font = pygame.font.Font(None, 74)
        text = font.render(str(score1), 1, white)
        dis.blit(text, (((dis_width / 2) - 174), 10))
        text = font.render(str(score2), 1, white)
        dis.blit(text, (((dis_width / 2) + 126), 10))
        if score1 >= 10:
            text = font.render('Player 1 Wins', 1, white)
            dis.blit(text, (40, dis_height / 2))
            pygame.display.flip()
            pygame.time.delay(5000)
            game_running = False
        if score2 >= 10:
            text = font.render('Player 2 Wins', 1, white)
            dis.blit(text, (dis_width / 2 + 5, dis_height / 2))
            pygame.display.flip()
            pygame.time.delay(5000)
            game_running = False
        pygame.display.flip()
        clock.tick(60)


font2 = pygame.font.Font(None, 51)
font3 = pygame.font.Font(None, 22)
while initiate:
    dis.fill(black)
    message1 = font2.render('Press P for Pong, S for Snake, T for TicTacToe', 1, white)
    message2 = font3.render(
        'Choose a Primary Color: W = White, L = Black, B = Blue, G = Green, R = Red, V = Violet, O = Orange, E = Yellow',
        1, white)
    message3 = font3.render(
        'Choose a Backround Color: 1 = White, 2 = Black, 3 = Blue, 4 = Green, 5 = Red, 6 = Violet, 7 = Orange, 8 = Yellow',
        1, white)
    dis.blit(message1, (20, dis_height / 2 - 37))
    dis.blit(message2, (5, dis_height / 2 + 20))
    dis.blit(message3, (5, dis_height / 2 + 40))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            initiate = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                initiate = False
            if event.key == pygame.K_n:
                initiate = False
            if event.key == pygame.K_r:
                white = red
            if event.key == pygame.K_b:
                white = blue
            if event.key == pygame.K_g:
                white = green
            if event.key == pygame.K_w:
                white = (255, 255, 255)
            if event.key == pygame.K_v:
                white = violet
            if event.key == pygame.K_o:
                white = orange
            if event.key == pygame.K_y:
                white = yellow
            if event.key == pygame.K_l:
                white = (0, 0, 0)
            if event.key == pygame.K_2:
                black = (0, 0, 0)
            if event.key == pygame.K_1:
                black = (255, 255, 255)
            if event.key == pygame.K_3:
                black = blue
            if event.key == pygame.K_4:
                black = green
            if event.key == pygame.K_5:
                black = red
            if event.key == pygame.K_6:
                black = violet
            if event.key == pygame.K_7:
                black = orange
            if event.key == pygame.K_8:
                black = yellow
            if event.key == pygame.K_p:
                gameloop()
                initiate = True
            if event.key == pygame.K_s:
                gameLoop1()
                initiate = True
            if event.key == pygame.K_t:
                gameloop2()
                initiate = True
pygame.quit()
quit()