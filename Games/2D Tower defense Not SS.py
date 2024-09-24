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
gray = (50, 50, 50)
gray2 = (100, 100, 100)
tower_width = 25
tower_height = 25
dis_width = 1000
dis_height = 600

box_width = 500
box_height = 100

working = True
score = 0
tower1_timer = 300
tower2_timer = 300
tower1_ready_timer = 50
tower2_ready_timer = 25

tower1_aim = False
tower1_aim2 = False
tower2_aim = False
tower3_aim = False
tower4_aim = False
tower5_aim = False
tower6_aim = False

punch_timer = 0
punch_timer2 = 0
punch_timer3 = 0
punch_timer4 = 0
punch_timer5 = 0
punch_timer6 = 0
shoot_timer = 0

tracker_timer = 180

check = 30

using_tower1 = False
using_tower2 = False
towpos1_type1 = False
towpos2_type1 = False
towpos3_type1 = False
towpos1_type2 = False
towpos4_type1 = False
towpos5_type1 = False
towpos6_type1 = False

clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Game')
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)

base_width = 40
base_height = 40

enemy_speed = 3


class tower_type1(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class tower_type2(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class projectile(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.last = pygame.time.get_ticks()
        self.cooldown = 1000

    def tracker(self, enemy, enemy2, enemy3, enemy4, x_coord, y_coord):
        # now = pygame.time.get_ticks()
        # test = 0
        chasing = 0
        chase2 = True
        chase3 = True
        chasing4 = 0
        chasing2 = 0
        chasing3 = 0
        while chasing < 30:
            if enemy.rect.x > self.rect.x:
                self.rect.x += 5
            if enemy.rect.x < self.rect.x:
                self.rect.x -= 5
            if enemy.rect.y > self.rect.y:
                self.rect.y += 5
            if enemy.rect.y < self.rect.y:
                self.rect.y -= 5
            if self.rect.colliderect(enemy):
                enemy.rect.x = -10
                enemy.rect.y = dis_height / 2 - 5
                self.rect.x = x_coord
                self.rect.y = y_coord
                chasing = 31
                chase2 = False
                chase3 = False
            all_sprites.update()
            pygame.draw.rect(dis, gray, [dis_width - box_width, 0, box_width, box_height])
            all_sprites.draw(dis)
            pygame.display.flip()
            chasing += 5
        self.rect.x = x_coord
        self.rect.y = y_coord
        while chasing4 < 30:
            if enemy4.rect.x > self.rect.x:
                self.rect.x += 5
            if enemy4.rect.x < self.rect.x:
                self.rect.x -= 5
            if enemy4.rect.y > self.rect.y:
                self.rect.y += 5
            if enemy4.rect.y < self.rect.y:
                self.rect.y -= 5
            if self.rect.colliderect(enemy):
                enemy4.rect.x = -10
                enemy4.rect.y = dis_height / 2 - 5
                self.rect.x = x_coord
                self.rect.y = y_coord
                chasing4 = 31
                chase2 = False
                chase3 = False
            all_sprites.update()
            pygame.draw.rect(dis, gray, [dis_width - box_width, 0, box_width, box_height])
            all_sprites.draw(dis)
            pygame.display.flip()
            chasing4 += 5
        self.rect.x = x_coord
        self.rect.y = y_coord
        while chasing2 < 30 and chase2:
            if enemy2.rect.x > self.rect.x:
                self.rect.x += 5
            if enemy2.rect.x < self.rect.x:
                self.rect.x -= 5
            if enemy2.rect.y > self.rect.y:
                self.rect.y += 5
            if enemy2.rect.y < self.rect.y:
                self.rect.y -= 5
            if self.rect.colliderect(enemy2):
                enemy2.rect.x = -10
                enemy2.rect.y = dis_height / 2 - 5
                self.rect.x = x_coord
                self.rect.y = y_coord
                chasing2 = 31
                chase2 = False
                chase3 = False
            all_sprites.update()
            pygame.draw.rect(dis, gray, [dis_width - box_width, 0, box_width, box_height])
            all_sprites.draw(dis)
            pygame.display.flip()
            chasing2 += 5
        self.rect.x = x_coord
        self.rect.y = y_coord
        while chasing3 < 30 and chase3:
            if enemy3.rect.x > self.rect.x:
                self.rect.x += 5
            if enemy3.rect.x < self.rect.x:
                self.rect.x -= 5
            if enemy3.rect.y > self.rect.y:
                self.rect.y += 5
            if enemy3.rect.y < self.rect.y:
                self.rect.y -= 5
            if self.rect.colliderect(enemy3):
                enemy3.rect.x = -10
                enemy3.rect.y = dis_height / 2 - 5
                self.rect.x = x_coord
                self.rect.y = y_coord
                chasing3 = 31
                chase3 = False
            all_sprites.update()
            pygame.draw.rect(dis, gray, [dis_width - box_width, 0, box_width, box_height])
            all_sprites.draw(dis)
            pygame.display.flip()
            chasing3 += 5
        self.rect.x = x_coord
        self.rect.y = y_coord


class tower_type1_selection(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class tower_type2_selection(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class enemy_type1(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class enemy_type2(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class tower_position(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class base(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class track(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


base1 = base(blue, base_width, base_height)
base1.rect.x = dis_width / 2 - (base_width / 2)
base1.rect.y = dis_height / 2 - (base_height / 2)

enm_type1_1 = enemy_type1(red, 10, 10)
enm_type1_1.rect.x = 0 - 10
enm_type1_1.rect.y = dis_height / 2 - 5

enm_type1_2 = enemy_type1(red, 10, 10)
enm_type1_2.rect.x = 0 - 10
enm_type1_2.rect.y = dis_height / 2 - 5

enm_type1_3 = enemy_type1(red, 10, 10)
enm_type1_3.rect.x = 0 - 10
enm_type1_3.rect.y = dis_height / 2 - 5

enm_type1_3 = enemy_type1(red, 10, 10)
enm_type1_3.rect.x = 0 - 10
enm_type1_3.rect.y = dis_height / 2 - 5

enm_type2_1 = enemy_type2(white, 10, 10)
enm_type2_1.rect.x = 0 - 10
enm_type2_1.rect.y = dis_height / 2 - 5

track_piece_1 = track(gray, 100, 2)
track_piece_1.rect.x = -1
track_piece_1.rect.y = dis_height / 2 - 1

track_piece_2 = track(gray, 2, 200)
track_piece_2.rect.x = 99
track_piece_2.rect.y = dis_height / 2 - 201

track_piece_3 = track(gray, 150, 2)
track_piece_3.rect.x = 99
track_piece_3.rect.y = dis_height / 2 - 201

track_piece_4 = track(gray, 2, 400)
track_piece_4.rect.x = 249
track_piece_4.rect.y = dis_height / 2 - 201

track_piece_5 = track(gray, 450, 2)
track_piece_5.rect.x = 249
track_piece_5.rect.y = dis_height / 2 + 199

track_piece_6 = track(gray, 2, 199)
track_piece_6.rect.x = 699
track_piece_6.rect.y = dis_height / 2

track_piece_7 = track(gray, 179, 2)
track_piece_7.rect.x = dis_width / 2 + 20
track_piece_7.rect.y = dis_height / 2

tower_pos1 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos1.rect.x = 119
tower_pos1.rect.y = dis_height / 2 - 181

tower_pos2 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos2.rect.x = 199
tower_pos2.rect.y = dis_height / 2 - 181

tower_pos3 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos3.rect.x = 44
tower_pos3.rect.y = dis_height / 2 - 45

tower_pos4 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos4.rect.x = dis_width / 2
tower_pos4.rect.y = dis_height / 2 + 209

tower_pos5 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos5.rect.x = dis_width / 2 + 159
tower_pos5.rect.y = dis_height / 2 + 159

tower_pos6 = track(gray2, tower_width + 5, tower_height + 5)
tower_pos6.rect.x = dis_width / 2 + 159
tower_pos6.rect.y = dis_height / 2 + 10

tower_type1_1 = tower_type1(yellow, tower_width, tower_height)
tower_type1_1.rect.x = 121.5
tower_type1_1.rect.y = dis_height / 2 - 178

tower_type2_1 = tower_type1(orange, tower_width, tower_height)
tower_type2_1.rect.x = 121.5
tower_type2_1.rect.y = dis_height / 2 - 178

tower_type1_2 = tower_type1(yellow, tower_width, tower_height)
tower_type1_2.rect.x = 201.5
tower_type1_2.rect.y = dis_height / 2 - 178.5

tower_type1_3 = tower_type1(yellow, tower_width, tower_height)
tower_type1_3.rect.x = 46.5
tower_type1_3.rect.y = (dis_height / 2 - 42.5)

tower_type1_3 = tower_type2(yellow, tower_width, tower_height)
tower_type1_3.rect.x = 46.5
tower_type1_3.rect.y = (dis_height / 2 - 42.5)

tower_type1_4 = tower_type2(yellow, tower_width, tower_height)
tower_type1_4.rect.x = dis_width / 2 + 2.5
tower_type1_4.rect.y = dis_height / 2 + 211.5

tower_type1_5 = tower_type2(yellow, tower_width, tower_height)
tower_type1_5.rect.x = dis_width / 2 + 159 + 2.5
tower_type1_5.rect.y = dis_height / 2 + 159 + 2.5

tower_type1_6 = tower_type2(yellow, tower_width, tower_height)
tower_type1_6.rect.x = dis_width / 2 + 159 + 2.5
tower_type1_6.rect.y = dis_height / 2 + 10 + 2.5

projectile1 = projectile(yellow, 10, 10)
projectile1.rect.x = 119 + (tower_width + 5) / 2
projectile1.rect.y = dis_height / 2 - 181 + (tower_width + 5) / 2

projectile2 = projectile(yellow, 10, 10)
projectile2.rect.x = 199 + (tower_width + 5) / 2
projectile2.rect.y = dis_height / 2 - 181 + (tower_width + 5) / 2

projectile3 = projectile(yellow, 10, 10)
projectile3.rect.x = 44 + (tower_width + 5) / 2
projectile3.rect.y = dis_height / 2 - 45 + (tower_width + 5) / 2

projectile4 = projectile(yellow, 10, 10)
projectile4.rect.x = dis_width / 2 + (tower_width + 5) / 2
projectile4.rect.y = dis_height / 2 + 209 + (tower_width + 5) / 2

projectile5 = projectile(yellow, 10, 10)
projectile5.rect.x = dis_width / 2 + 159 + (tower_width + 5) / 2
projectile5.rect.y = dis_height / 2 + 159 + (tower_width + 5) / 2

projectile6 = projectile(yellow, 10, 10)
projectile6.rect.x = dis_width / 2 + 159 + (tower_width + 5) / 2
projectile6.rect.y = dis_height / 2 + 10 + (tower_width + 5) / 2

while working:
    tower_type1_selection_box = tower_type1_selection(yellow, box_height / 2, 0 + tower1_ready_timer)
    tower_type1_selection_box.rect.x = (dis_width - box_width) + box_height / 4
    tower_type1_selection_box.rect.y = box_height / 4

    tower_type2_selection_box = tower_type2_selection(orange, box_height / 2, 0 + tower2_ready_timer)
    tower_type2_selection_box.rect.x = (dis_width - box_width) + box_height
    tower_type2_selection_box.rect.y = box_height / 4


    def follow_path_1(enemy, direction):
        moving = 1
        right = False
        up = False
        down = False
        left = False
        if direction == 'r':
            right = True
        if direction == 'u':
            up = True
        if direction == 'd':
            down = True
        if direction == 'l':
            left = True
        following = True
        while following:
            all_sprites.update()
            all_sprites.draw(dis)
            if moving > enemy_speed:
                following = False
            elif right:
                enemy.rect.x += enemy_speed
            elif up:
                enemy.rect.y -= enemy_speed
            elif down:
                enemy.rect.y += enemy_speed
            elif left:
                enemy.rect.x -= enemy_speed
            moving += enemy_speed


    lose_mesg = font1.render('You Lose', True, white)
    score_mesg = font2.render(f'Your Score Was: {score}', True, white)


    def lose_message():
        dis.blit(lose_mesg, [30, 200])
        dis.blit(score_mesg, [300, 400])


    dis.fill(black)
    all_sprites = pygame.sprite.Group()
    projectile_list = pygame.sprite.Group()

    all_sprites.add(track_piece_1)
    all_sprites.add(track_piece_2)
    all_sprites.add(track_piece_3)
    all_sprites.add(track_piece_4)
    all_sprites.add(track_piece_5)
    all_sprites.add(track_piece_6)
    all_sprites.add(track_piece_7)
    all_sprites.add(tower_pos1)
    all_sprites.add(tower_pos2)
    all_sprites.add(tower_pos3)
    all_sprites.add(tower_pos4)
    all_sprites.add(tower_pos5)
    all_sprites.add(tower_pos6)
    all_sprites.add(enm_type1_1)
    all_sprites.add(enm_type1_2)
    all_sprites.add(enm_type1_3)
    all_sprites.add(enm_type2_1)
    all_sprites.add(base1)
    all_sprites.add(tower_type1_selection_box)
    all_sprites.add(tower_type2_selection_box)
    if towpos1_type1 == True:
        all_sprites.add(tower_type1_1)
        all_sprites.add(projectile1)
        tower1_aim = True
        # pygame.draw.circle(dis, blue, [131.5, dis_height/2-168.5], 5)
        # if towpos1_type2==True:
        #   all_sprites.add(tower_type2_1)
        # all_sprites.add(projectile1_type1)
        tower1_aim2 = True
    if towpos2_type1 == True:
        all_sprites.add(tower_type1_2)
        all_sprites.add(projectile2)
        tower2_aim = True
    if towpos3_type1 == True:
        all_sprites.add(tower_type1_3)
        all_sprites.add(projectile3)
        tower3_aim = True
    if towpos4_type1 == True:
        all_sprites.add(tower_type1_4)
        all_sprites.add(projectile4)
        tower4_aim = True
    if towpos5_type1 == True:
        all_sprites.add(tower_type1_5)
        all_sprites.add(projectile5)
        tower5_aim = True
    if towpos6_type1 == True:
        all_sprites.add(tower_type1_6)
        all_sprites.add(projectile6)
        tower6_aim = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                working = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
            for i in clicked_sprites:

                if i == tower_pos1 and using_tower1:
                    towpos1_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_pos1 and using_tower2:
                    towpos1_type2 = True
                    using_tower2 = False
                    tower2_timer = 0
                    tower2_ready_timer = 0
                if i == tower_pos2 and using_tower1:
                    towpos2_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_pos3 and using_tower1:
                    towpos3_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_pos4 and using_tower1:
                    towpos4_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_pos5 and using_tower1:
                    towpos5_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_pos6 and using_tower1:
                    towpos6_type1 = True
                    using_tower1 = False
                    tower1_timer = 0
                    tower1_ready_timer = 0
                if i == tower_type1_selection_box and tower1_timer > 300:
                    using_tower1 = True
                if i == tower_type2_selection_box and tower2_timer > 600:
                    using_tower2 = True

    keys = pygame.key.get_pressed()

    # if keys[pygame.K_w]:
    # exploding = 0
    # while exploding < 180:
    #   pygame.draw.rect(dis, orange, [(dis_width/2 - (base_width/2))-exploding/2, (dis_height/2 - (base_width/2))-exploding/2, base_width + exploding, base_height + exploding], 5)
    #   pygame.time.wait(500)
    #   exploding += 30

    # if keys[pygame.K_s]:

    # if keys[pygame.K_a]:

    # if keys[pygame.K_d]:
    if score > 60:
        if enm_type1_1.rect.colliderect(track_piece_1) or enm_type1_1.rect.colliderect(
                track_piece_3) or enm_type1_1.rect.colliderect(track_piece_5):
            follow_path_1(enm_type1_1, 'r')
        if enm_type1_1.rect.colliderect(track_piece_2) or enm_type1_1.rect.colliderect(track_piece_6):
            follow_path_1(enm_type1_1, 'u')
        if enm_type1_1.rect.colliderect(track_piece_4):
            follow_path_1(enm_type1_1, 'd')
        if enm_type1_1.rect.colliderect(track_piece_7):
            follow_path_1(enm_type1_1, 'l')
    if score > 120 and check > 30:
        if enm_type1_2.rect.colliderect(track_piece_1) or enm_type1_2.rect.colliderect(
                track_piece_3) or enm_type1_2.rect.colliderect(track_piece_5):
            follow_path_1(enm_type1_2, 'r')
        if enm_type1_2.rect.colliderect(track_piece_2) or enm_type1_2.rect.colliderect(track_piece_6):
            follow_path_1(enm_type1_2, 'u')
        if enm_type1_2.rect.colliderect(track_piece_4):
            follow_path_1(enm_type1_2, 'd')
        if enm_type1_2.rect.colliderect(track_piece_7):
            follow_path_1(enm_type1_2, 'l')
    if score > 600 and check > 75:
        if enm_type1_3.rect.colliderect(track_piece_1) or enm_type1_3.rect.colliderect(
                track_piece_3) or enm_type1_3.rect.colliderect(track_piece_5):
            follow_path_1(enm_type1_3, 'r')
        if enm_type1_3.rect.colliderect(track_piece_2) or enm_type1_3.rect.colliderect(track_piece_6):
            follow_path_1(enm_type1_3, 'u')
        if enm_type1_3.rect.colliderect(track_piece_4):
            follow_path_1(enm_type1_3, 'd')
        if enm_type1_3.rect.colliderect(track_piece_7):
            follow_path_1(enm_type1_3, 'l')
    if score > 180 and check > 105:
        if enm_type2_1.rect.colliderect(track_piece_1) or enm_type2_1.rect.colliderect(
                track_piece_3) or enm_type2_1.rect.colliderect(track_piece_5):
            follow_path_1(enm_type2_1, 'r')
        if enm_type2_1.rect.colliderect(track_piece_2) or enm_type2_1.rect.colliderect(track_piece_6):
            follow_path_1(enm_type2_1, 'u')
        if enm_type2_1.rect.colliderect(track_piece_4):
            follow_path_1(enm_type2_1, 'd')
        if enm_type2_1.rect.colliderect(track_piece_7):
            follow_path_1(enm_type2_1, 'l')

    if tower1_ready_timer >= 50:
        tower1_ready_timer = 50
    if tower2_ready_timer >= 50:
        tower2_ready_timer = 50

    if enm_type1_1.rect.colliderect(base1) or enm_type1_2.rect.colliderect(base1) or enm_type1_3.rect.colliderect(
            base1):
        exploding = 0
        while exploding < 180:
            all_sprites.draw(dis)
            pygame.draw.rect(dis, red, [(dis_width / 2) - exploding / 2 - 2, (dis_height / 2) - exploding / 2 - 2,
                                        2.5 + exploding, 2.5 + exploding], 1)
            pygame.draw.rect(dis, yellow, [(dis_width / 2) - exploding / 2 - 2, (dis_height / 2) - exploding / 2 - 2,
                                           1.25 + exploding, 1.25 + exploding], 1)
            pygame.draw.rect(dis, orange,
                             [(dis_width / 2) - exploding / 2 - 2, (dis_height / 2) - exploding / 2 - 2, 5 + exploding,
                              5 + exploding], 2)
            pygame.time.wait(50)
            pygame.display.flip()
            exploding += 10
        dis.fill(black)
        lose_message()
        pygame.display.flip()
        pygame.time.wait(3000)
        working = False
    if tower1_aim and punch_timer > 120:
        projectile1.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1, 119 + (tower_width + 5) / 2,
                            dis_height / 2 - 181 + (tower_width + 5) / 2)
        # check=0
        punch_timer = 0
    if tower1_aim2 == True and shoot_timer > 120:
        pass
    if tower2_aim and punch_timer2 > 120:
        projectile2.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1, 199 + (tower_width + 5) / 2,
                            dis_height / 2 - 181 + (tower_width + 5) / 2)
        punch_timer2 = 0
    if tower3_aim and punch_timer3 > 120:
        projectile3.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1, 44 + (tower_width + 5) / 2,
                            dis_height / 2 - 45 + (tower_width + 5) / 2)
        punch_timer3 = 0
    if tower4_aim and punch_timer4 > 120:
        projectile4.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1, dis_width / 2 + (tower_width + 5) / 2,
                            dis_height / 2 + 209 + (tower_width + 5) / 2)
        punch_timer4 = 0
    if tower5_aim and punch_timer5 > 120:
        projectile5.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1,
                            dis_width / 2 + 159 + (tower_width + 5) / 2, dis_height / 2 + 159 + (tower_width + 5) / 2)
        punch_timer5 = 0
    if tower6_aim and punch_timer6 > 120:
        projectile6.tracker(enm_type1_1, enm_type1_2, enm_type1_3, enm_type2_1,
                            dis_width / 2 + 159 + (tower_width + 5) / 2, dis_height / 2 + 10 + (tower_width + 5) / 2)
        punch_timer6 = 0
    all_sprites.update()
    pygame.draw.rect(dis, gray, [dis_width - box_width, 0, box_width, box_height])
    all_sprites.draw(dis)
    projectile_list.draw(dis)
    pygame.display.flip()
    score += 1
    tower1_timer += 1
    punch_timer += 1
    punch_timer2 += 1
    punch_timer3 += 1
    punch_timer4 += 1
    punch_timer5 += 1
    punch_timer6 += 1
    shoot_timer += 1
    # tracker_timer += 1
    tower1_ready_timer += (1 / 6)
    tower2_ready_timer += (1 / 12)
    tower2_timer += 1
    check += 1
    clock.tick(60)
pygame.quit()
quit()