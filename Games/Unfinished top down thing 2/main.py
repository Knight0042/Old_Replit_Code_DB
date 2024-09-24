import pygame
import spritesheet
import random

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
green = (0, 100, 0)
violet = (148,0,211)
orange = (255,165,0)
yellow = (255,255,0)
gray = (75, 75, 75)
grey = gray
gray2 = (100, 100, 100)
brown = (165,42,42)

backround_color = black
playing = True
frame_rate = 30
all_sprites = pygame.sprite.Group()
environment_sprites = pygame.sprite.Group()
plyr_speed2 = 4


player_img = pygame.image.load("player_img.png")


def load_images(image_list, num, x, y, ck, sprite_sheet, img_width, img_height):
    # Crops a spritesheet and adds the cropped image to a list
    global image_height
    global image_width
    correction = 1
    if y == 0:
        correction2 = 1
    else:
        correction2 = 1
    for item in range(0, num):
        if item > 9:
            correction2 = 0
            image = sprite_sheet.image_at(((x + item) * img_width + correction*item+1, y * img_height + correction2, img_width,
                                       img_height), colorkey=ck)
        else:
            image = sprite_sheet.image_at(((x + item) * img_width + correction*item, y * img_height + correction2, img_width,
                                       img_height), colorkey=ck)
        image_list.append(pygame.transform.scale(image, [img_width*2, img_height*2]))


def update_dis(num, num2):
    if num == 0:
        dis.fill(green)
        environment_sprites.draw(dis)
        all_sprites.draw(dis)

    pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img, type):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        if self.type == 0 or self.type == 1:
            all_sprites.add(self)

class BuildingPiece(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, piece_type):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black2)
        self.image.set_colorkey(black2)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.piece_type = piece_type
        environment_sprites.add(self)
    def shift(self, d):
        if d == 1:
            self.rect.x += plyr_speed2
        if d == 2:
            self.rect.y += plyr_speed2
        if d == 3:
            self.rect.x -= plyr_speed2
        if d == 4:
            self.rect.y -= plyr_speed2
        if self.rect.colliderect(player):
            if self.piece_type == 1:
                r = 2
                if d>2:
                    r = -2
                for s in environment_sprites:
                    s.shift(d+r)

def construct_building(x, y, type):
    if type == 1:
        floor_1 = BuildingPiece(grey, 800, 600, x, y, 2)
        wall_1 = BuildingPiece(black, 800, 20, x, y, 1)
        wall_2 = BuildingPiece(black, 20, 600, x, y, 1)
        wall_3 = BuildingPiece(black, 350, 20, x, y+580, 1)
        wall_4 = BuildingPiece(black, 350, 20, x+450, y+580, 1)
        wall_5 = BuildingPiece(black, 20, 600, x+780, y, 1)

player = Player(493, 333, player_img, 1)
construct_building(300, 200, 1)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        for s in environment_sprites:
            s.shift(1)
    if keys[pygame.K_w]:
        for s in environment_sprites:
            s.shift(2)
    if keys[pygame.K_d]:
        for s in environment_sprites:
            s.shift(3)
    if keys[pygame.K_s]:
        for s in environment_sprites:
            s.shift(4)
    update_dis(0, 1)
    clock.tick(frame_rate)