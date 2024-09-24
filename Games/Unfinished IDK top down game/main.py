import pygame
import random
import math

pygame.init()

dis_width = 1000
dis_height = 680
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('i dont know')
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)
font6 = pygame.font.SysFont("bahnschrift", 70)

black = (0, 0, 0)
black2 = (1, 1, 1)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 100)
green = (0, 255, 0)
violet = (148,0,211)
orange = (255,165,0)
yellow = (255,255,0)
gray = (75, 75, 75)
gray2 = (100, 100, 100)
brown = (165,42,42)

backround_color = gray
middleground_color = black
playing = True
frame_rate = 30
plyr_spd = 4
all_sprites = pygame.sprite.Group()
all_enemy_sprites = pygame.sprite.Group()
all_projectile_sprites = pygame.sprite.Group()
timer = 0
timer2 = 0
bullet_img = pygame.image.load("bullet.png")
player_img = pygame.image.load("player_img.png")
def update_dis():
    dis.fill(backround_color)
    all_sprites.draw(dis)
    all_enemy_sprites.draw(dis)
    all_projectile_sprites.draw(dis)
    pygame.display.flip()
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)
    def move(self, d):
        plyr_spd = 4
        if d == 1:
            self.rect.x += plyr_spd
            if self.rect.x >= dis_width:
                self.rect.x -= plyr_spd
        if d == 2:
            self.rect.y += plyr_spd
            if self.rect.y >= dis_height:
                self.rect.y -= plyr_spd
        if d == 3:
            self.rect.x -= plyr_spd
            if self.rect.x <= 0:
                self.rect.x += plyr_spd
        if d == 4:
            self.rect.y -= plyr_spd
            if self.rect.y <= 0:
                self.rect.y += plyr_spd


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_enemy_sprites.add(self)
    def move(self, d):
        enm_spd = 4
        if d == 1:
            self.rect.x += enm_spd
            if self.rect.x >= dis_width:
                self.rect.x -= enm_spd
        if d == 2:
            self.rect.y += enm_spd
            if self.rect.y >= dis_height:
                self.rect.y -= enm_spd
        if d == 3:
            self.rect.x -= enm_spd
            if self.rect.x <= 0:
                self.rect.x += enm_spd
        if d == 4:
            self.rect.y -= enm_spd
            if self.rect.y <= 0:
                self.rect.y += enm_spd
    # def track(self):
    #     if player_pos[0]
    #     self.move(1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, img, angle, speed):
        super().__init__()
        self.image = pygame.transform.rotate(img, 360-angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.speed = speed
        all_projectile_sprites.add(self)
    def move(self):
        if 90 > self.angle >= 0:
            self.rect.x += self.speed+(self.angle)/5
            self.rect.y -= self.speed+(90-self.angle)/5
        elif 180 > self.angle >= 90:
            self.rect.x += (self.speed*-1+(self.angle-180)/5)*-1
            self.rect.y += self.speed+(self.angle-90)/5
        elif 270 > self.angle >= 180:
            self.rect.x -= self.speed+(self.angle-180)/5
            self.rect.y += (self.speed +(self.angle-270)/5)*-1
        elif 360 > self.angle >= 270:
            self.rect.x -= self.speed+((self.angle-360)/5)*-1
            self.rect.y -= self.speed+(self.angle-270)/5
        if self.rect.x > dis_width or self.rect.x < 0 or self.rect.y > dis_height or self.rect.y < 0:
            self.kill()
            
# test_bullet = Bullet(500, 300, bullet_img, timer2, 0)
player = Player(500, 300, player_img)
enemy1 = Enemy(590, 300, player_img)
while playing:
    player_pos = (player.rect.x, player.rect.y)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_menu = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     angle_measure = 0
        #     hypotenuse = math.dist((player_pos), (mouse_pos))
        #     if mouse_pos[1] > player_pos[1]:
        #         y_side = math.dist(player_pos, (player_pos[0], mouse_pos[1]))*-1
        #     elif mouse_pos[1] <= player_pos[1]:
        #         y_side = math.dist(player_pos, (player_pos[0], mouse_pos[1]))
        #     if mouse_pos[0] < player_pos[0]:
        #         x_side = (math.dist(player_pos, (mouse_pos[0], player_pos[1])))*-1
        #     elif mouse_pos[0] >= player_pos[0]:
        #         x_side = (math.dist(player_pos, (mouse_pos[0], player_pos[1])))
        #     if x_side != 0:
        #         angle_measure = math.degrees(math.acos((x_side/hypotenuse)))
        #         if y_side > 0:
        #             angle_measure = 360-angle_measure
        #         angle_measure += 90
        #         if angle_measure > 360:
        #             angle_measure -= 360
        #     # print(hypotenuse/y_side)
        #     # print(y_side)
        #     # print(x_side)
        #     print(angle_measure)
        #     bullet = Bullet(500, 300, bullet_img, angle_measure, 0)
    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True and timer > 1/6:
        angle_measure = 0
        hypotenuse = math.dist((player_pos), (mouse_pos))
        if mouse_pos[1] > player_pos[1]:
            y_side = math.dist(player_pos, (player_pos[0], mouse_pos[1]))*-1
        elif mouse_pos[1] <= player_pos[1]:
            y_side = math.dist(player_pos, (player_pos[0], mouse_pos[1]))
        if mouse_pos[0] < player_pos[0]:
            x_side = (math.dist(player_pos, (mouse_pos[0], player_pos[1])))*-1
        elif mouse_pos[0] >= player_pos[0]:
            x_side = (math.dist(player_pos, (mouse_pos[0], player_pos[1])))
        if x_side != 0:
            angle_measure = math.degrees(math.acos((x_side/hypotenuse)))
            if y_side > 0:
                angle_measure = 360-angle_measure
            angle_measure += 90
            if angle_measure > 360:
                angle_measure -= 360
        # print(hypotenuse/y_side)
        # print(y_side)
        # print(x_side)
        # print(angle_measure)
        bullet = Bullet(player_pos[0]+9, player_pos[1]+9, bullet_img, angle_measure, 0)
        timer = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(3)
    if keys[pygame.K_w]:
        player.move(4)
    if keys[pygame.K_d]:
        player.move(1)
    if keys[pygame.K_s]:
        player.move(2)
    for b in all_projectile_sprites:
        b.move()
        for e in all_enemy_sprites:
            if b.rect.colliderect(e):
                e.kill()
                # b.kill()
        # b.kill()
    # if timer > frame_rate/4:
    #     timer2 += 1
    #     test_bullet = Bullet(500, 300, bullet_img, timer2, 0)
    #     timer = 0
    # if timer > 1/7:
    #     enemy1 = Enemy(590 + timer*20, 300, player_img)
    update_dis()
    timer += 1/frame_rate
    clock.tick(frame_rate)
