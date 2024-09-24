import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)

player_width = 10
player_height = 10

paddle_height = 100
paddle_width = 10

paddle_height2 = 10
paddle_width2 = 100

dis_height = 600
dis_width = 600
running = True

pygame.init()

clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Defence')

current_x = -100
current_y = -100
tracker_speed = 1
score = 0


class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class tracker_projectile(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def chase_player(self, thing):
        if thing.rect.x > self.rect.x:
            self.rect.x += tracker_speed
        if thing.rect.x < self.rect.x:
            self.rect.x -= tracker_speed
        if thing.rect.y > self.rect.y:
            self.rect.y += tracker_speed
        if thing.rect.y < self.rect.y:
            self.rect.y -= tracker_speed


tracker1 = tracker_projectile(red, player_width, player_height)
tracker1.rect.x = 0 - player_width
tracker1.rect.y = dis_height / 2 - (player_height / 2)

tracker2 = tracker_projectile(red, player_width, player_height)
tracker2.rect.x = dis_width / 2 - player_width / 2
tracker2.rect.y = 0 - (player_height)

tracker3 = tracker_projectile(red, player_width, player_height)
tracker3.rect.x = dis_width + player_height
tracker3.rect.y = dis_height / 2 - (player_height / 2)

tracker4 = tracker_projectile(red, player_width, player_height)
tracker4.rect.x = dis_width / 2 - player_width / 2
tracker4.rect.y = dis_height - (player_height)
being_pressed = False

while running:
    being_pressed = False
    all_sprites = pygame.sprite.Group()
    player1 = player(white, player_width, player_height)
    player1.rect.x = (dis_width / 2) - (player_width / 2)
    player1.rect.y = (dis_height / 2) - (player_height / 2)


    class paddle(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()
        # def moveUp(self):
        #   self.rect.y = up_y
        #   self.rect.x = up_x
        # def moveDown(self):
        #   self.rect.y = down_y
        #   self.rect.x = down_x
        # def moveLeft(self):
        #   self.rect.x = left_x
        #   self.rect.y = left_y
        # def moveRight(self):
        #   self.rect.x = right_x
        #   self.rect.y = right_y


    # paddle1 = paddle(white, 0, 0)
    # paddle1.rect.x = -100
    # paddle1.rect.y = -100
    font1 = pygame.font.SysFont("bahnschrift", 150)
    font2 = pygame.font.SysFont("bahnschrift", 50)
    lose_mesg = font1.render('You Lose', True, white)
    score_mesg = font2.render(f'Your Score Was: {score}', True, white)


    def lose_message():
        dis.blit(lose_mesg, [65, 200])
        dis.blit(score_mesg, [125, 400])


    up_x = ((player1.rect.x - (paddle_width2 / 2)) + player_width / 2)
    down_x = (player1.rect.x - (paddle_width2 / 2) + player_width / 2)
    right_x = ((player1.rect.x - (paddle_width / 2)) + 60)
    left_x = ((player1.rect.x - (paddle_width / 2)) - 50)

    up_y = (player1.rect.y - (paddle_height2 / 2) - 50)
    down_y = ((player1.rect.y - (paddle_height2 / 2)) + 60)
    right_y = (player1.rect.x - (paddle_height / 2) + player_width / 2)
    left_y = (player1.rect.x - (paddle_height / 2) + player_width / 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and being_pressed == False:
        being_pressed = True
        paddle2 = paddle(white, paddle_width2, paddle_height2)
        # paddle1.moveUp()
        paddle2.rect.y = up_y
        paddle2.rect.x = up_x
        all_sprites.add(paddle2)
        if paddle2.rect.colliderect(tracker1):
            tracker1.rect.x = 0 - player_width
            tracker1.rect.y = dis_height / 2 - (player_height / 2)
        if paddle2.rect.colliderect(tracker2):
            tracker2.rect.x = dis_width / 2 - player_width / 2
            tracker2.rect.y = 0 - (player_height)
        if paddle2.rect.colliderect(tracker3):
            tracker3.rect.x = dis_width + player_height
            tracker3.rect.y = dis_height / 2 - (player_height / 2)
        if paddle2.rect.colliderect(tracker4):
            tracker4.rect.x = dis_width / 2 - player_width / 2
            tracker4.rect.y = dis_height - (player_height)
    if keys[pygame.K_s] and being_pressed == False:
        being_pressed = True
        paddle2 = paddle(white, paddle_width2, paddle_height2)
        paddle2.rect.y = down_y
        paddle2.rect.x = down_x
        all_sprites.add(paddle2)
        if paddle2.rect.colliderect(tracker1):
            tracker1.rect.x = 0 - player_width
            tracker1.rect.y = dis_height / 2 - (player_height / 2)
        if paddle2.rect.colliderect(tracker2):
            tracker2.rect.x = dis_width / 2 - player_width / 2
            tracker2.rect.y = 0 - (player_height)
        if paddle2.rect.colliderect(tracker3):
            tracker3.rect.x = dis_width + player_height
            tracker3.rect.y = dis_height / 2 - (player_height / 2)
        if paddle2.rect.colliderect(tracker4):
            tracker4.rect.x = dis_width / 2 - player_width / 2
            tracker4.rect.y = dis_height - (player_height)
    if keys[pygame.K_a] and being_pressed == False:
        being_pressed = True
        paddle_height = 100
        paddle_width = 10
        paddle1 = paddle(white, paddle_width, paddle_height)
        paddle1.rect.x = left_x
        paddle1.rect.y = left_y
        all_sprites.add(paddle1)
        if paddle1.rect.colliderect(tracker1):
            tracker1.rect.x = 0 - player_width
            tracker1.rect.y = dis_height / 2 - (player_height / 2)
        if paddle1.rect.colliderect(tracker2):
            tracker2.rect.x = dis_width / 2 - player_width / 2
            tracker2.rect.y = 0 - (player_height)
        if paddle1.rect.colliderect(tracker3):
            tracker3.rect.x = dis_width + player_height
            tracker3.rect.y = dis_height / 2 - (player_height / 2)
        if paddle1.rect.colliderect(tracker4):
            tracker4.rect.x = dis_width / 2 - player_width / 2
            tracker4.rect.y = dis_height - (player_height)
    if keys[pygame.K_d] and being_pressed == False:
        being_pressed = True
        paddle_height = 100
        paddle_width = 10
        paddle1 = paddle(white, paddle_width, paddle_height)
        paddle1.rect.x = right_x
        paddle1.rect.y = right_y
        all_sprites.add(paddle1)
        if paddle1.rect.colliderect(tracker1):
            tracker1.rect.x = 0 - player_width
            tracker1.rect.y = dis_height / 2 - (player_height / 2)
        if paddle1.rect.colliderect(tracker2):
            tracker2.rect.x = dis_width / 2 - player_width / 2
            tracker2.rect.y = 0 - (player_height)
        if paddle1.rect.colliderect(tracker3):
            tracker3.rect.x = dis_width + player_height
            tracker3.rect.y = dis_height / 2 - (player_height / 2)
        if paddle1.rect.colliderect(tracker4):
            tracker4.rect.x = dis_width / 2 - player_width / 2
            tracker4.rect.y = dis_height - (player_height)
    if player1.rect.colliderect(tracker1):
        dis.fill(black)
        lose_message()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
    if player1.rect.colliderect(tracker2):
        dis.fill(black)
        lose_message()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
    if player1.rect.colliderect(tracker3):
        dis.fill(black)
        lose_message()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
    if player1.rect.colliderect(tracker4):
        dis.fill(black)
        lose_message()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False

    score += 1
    dis.fill(black)
    tracker1.chase_player(player1)
    all_sprites.add(tracker1)
    if score > 140:
        all_sprites.add(tracker2)
        tracker2.chase_player(player1)
    if score > 80:
        all_sprites.add(tracker3)
        tracker3.chase_player(player1)
    if score > 220:
        all_sprites.add(tracker4)
        tracker4.chase_player(player1)
    all_sprites.add(player1)
    all_sprites.update()
    all_sprites.draw(dis)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
