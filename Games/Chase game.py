import pygame
import random

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
main_color = white
secondary_color = red
tertiary_color = yellow
objects = []
initiate = True
dis_width = 1000
dis_height = 600
player_width = 10
player_height = 10
player_x = (100)
player_y = (100)
playing = True
tracker_speed = 1
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game')
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)


def game_loop():
    class boost(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(black)
            self.image.set_colorkey(black)
            pygame.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()

        def relocate(self):
            self.rect.x = round(random.randrange(0, dis_width - player_width) / 5) * 5
            self.rect.y = round(random.randrange(0, dis_height - player_height) / 5) * 5

    class player(pygame.sprite.Sprite):
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
            if self.rect.y > (dis_height - self.rect.width):
                self.rect.y = (dis_height - self.rect.width)

        def moveLeft(self, pixels):
            self.rect.x -= pixels
            if self.rect.x < 0:
                self.rect.x = 0

        def moveRight(self, pixels):
            self.rect.x += pixels
            if self.rect.x > (dis_width - self.rect.width):
                self.rect.x = (dis_width - self.rect.width)

    # class explode(pygame.sprite.Sprite):
    #   def __init__(self, color, width, height):
    #     super().__init__()
    #     self.image = pygame.Surface([width, height])
    #     self.image.fill(black)
    #     self.image.set_colorkey(black)
    #     pygame.draw.rect(self.image, color, [0, 0, width, height], 5)
    #     self.rect = self.image.get_rect()

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

    going = True
    score = 0
    boost_total = 0
    explode_timer = 0
    tracker_speed = 1
    player1 = player(main_color, player_width, player_height)
    player1.rect.x = dis_width / 2
    player1.rect.y = dis_height / 2

    tracker1 = tracker_projectile(secondary_color, player_width, player_height)
    tracker1.rect.x = 0 - player_width
    tracker1.rect.y = 0 - player_height
    tracker2 = tracker_projectile(secondary_color, player_width, player_height)
    tracker2.rect.x = dis_width / 2
    tracker2.rect.y = 0 - player_height
    tracker3 = tracker_projectile(secondary_color, player_width, player_height)
    tracker3.rect.x = dis_width + player_width
    tracker3.rect.y = 0 - player_height
    tracker4 = tracker_projectile(secondary_color, player_width, player_height)
    tracker4.rect.x = dis_width + player_width
    tracker4.rect.y = dis_height / 2
    tracker5 = tracker_projectile(secondary_color, player_width, player_height)
    tracker5.rect.x = dis_width + player_width
    tracker5.rect.y = dis_height + player_height
    tracker6 = tracker_projectile(secondary_color, player_width, player_height)
    tracker6.rect.x = dis_width / 2
    tracker6.rect.y = dis_height + player_height
    tracker7 = tracker_projectile(secondary_color, player_width, player_height)
    tracker7.rect.x = 0 - player_width
    tracker7.rect.y = dis_height + player_height
    tracker8 = tracker_projectile(secondary_color, player_width, player_height)
    tracker8.rect.x = 0 - player_width
    tracker8.rect.y = dis_height / 2
    boost1 = boost(tertiary_color, player_width, player_height)
    boost1.relocate()

    while going:
        lose_mesg = font1.render('You Lose', True, white)
        score_mesg = font2.render(f'Your Score Was: {score + boost_total}', True, white)

        def lose_message():
            dis.blit(lose_mesg, [30, 200])
            dis.blit(score_mesg, [300, 400])

        dis.fill(black)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player1)
        all_sprites.add(boost1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    going = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.moveUp(5)
        if keys[pygame.K_s]:
            player1.moveDown(5)
        if keys[pygame.K_a]:
            player1.moveLeft(5)
        if keys[pygame.K_d]:
            player1.moveRight(5)

        if player1.rect.colliderect(tracker1):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker2):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker3):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker4):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker5):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker6):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker7):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker8):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if player1.rect.colliderect(tracker2):
            dis.fill(black)
            lose_message()
            pygame.display.flip()
            pygame.time.wait(5000)
            going = False
        if score >= 0:
            all_sprites.add(tracker1)
            # objects.append(tracker1)
            tracker_speed = 1
            tracker1.chase_player(player1)
        if score >= 600:
            all_sprites.add(tracker2)
            tracker_speed = 1.5
            tracker2.chase_player(player1)
        if score >= 1200:
            all_sprites.add(tracker3)
            tracker_speed = 2
            tracker3.chase_player(player1)
        if score >= 1800:
            all_sprites.add(tracker4)
            tracker_speed = 2.5
            tracker4.chase_player(player1)
        if score >= 2400:
            all_sprites.add(tracker5)
            tracker_speed = 3
            tracker5.chase_player(player1)
        if score >= 3000:
            all_sprites.add(tracker6)
            tracker_speed = 3.5
            tracker6.chase_player(player1)
        if score >= 3600:
            all_sprites.add(tracker7)
            tracker_speed = 4
            tracker7.chase_player(player1)
        if score >= 4200:
            all_sprites.add(tracker8)
            tracker_speed = 4.5
            tracker8.chase_player(player1)
        if player1.rect.colliderect(boost1):
            boost_total += 200
            boost1.relocate()
        # if (score + boost_total) > high_score:
        #   high_score = (score + boost_total)+1
        all_sprites.update()
        all_sprites.draw(dis)
        pygame.display.flip()
        score += 1
        explode_timer += 1
        clock.tick(60)


font4 = pygame.font.Font(None, 90)
font3 = pygame.font.Font(None, 27)
while initiate:
    dis.fill(black)
    message1 = font4.render('Press C to Play and ESC to Exit', 1, white)
    message2 = font3.render(
        'Choose a Primary Color: W = White, L = Black, B = Blue, G = Green, R = Red, V = Violet, O = Orange, E = Yellow',
        1, white)
    message3 = font3.render(
        'Choose a Backround Color: 1 = White, 2 = Black, 3 = Blue, 4 = Green, 5 = Red, 6 = Violet, 7 = Orange, 8 = Yellow',
        1, white)
    dis.blit(message1, (30, dis_height / 2 - 37))
    dis.blit(message2, (10, dis_height / 2 + 30))
    dis.blit(message3, (10, dis_height / 2 + 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            initiate = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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
            if event.key == pygame.K_c:
                game_loop()
                initiate = True
pygame.quit()
quit()