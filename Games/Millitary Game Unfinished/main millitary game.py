import pygame
import random
import spritesheet
import math
 
pygame.init()
 
 
with open('info.txt') as f:
    lines = f.readlines()
    for _b, _a in enumerate(lines):
        lines[_b] = _a[:-1]


size_multiplyer = float(input('Multiplyer'))
image_width = 30
image_height = 30


ss = spritesheet.spritesheet('terrain_spritesheet.png')
home_base_1_img = pygame.image.load("home_base_1.png")
home_base_1_img = pygame.transform.scale(home_base_1_img, [home_base_1_img.get_width()*size_multiplyer, home_base_1_img.get_height()*size_multiplyer])
home_base_2_img = pygame.image.load("home_base_2.png")
home_base_2_img = pygame.transform.scale(home_base_2_img, [home_base_2_img.get_width()*size_multiplyer, home_base_2_img.get_height()*size_multiplyer])
barracks_1_img = pygame.image.load("barracks_1.png")
barracks_1_img = pygame.transform.scale(barracks_1_img, [barracks_1_img.get_width()*size_multiplyer, barracks_1_img.get_height()*size_multiplyer])
barracks_2_img = pygame.image.load("barracks_2.png")
barracks_2_img = pygame.transform.scale(barracks_2_img, [barracks_2_img.get_width()*size_multiplyer, barracks_2_img.get_height()*size_multiplyer])

farm_1_img = pygame.image.load("farm_1.png")
farm_1_img = pygame.transform.scale(farm_1_img, [farm_1_img.get_width()*size_multiplyer, farm_1_img.get_height()*size_multiplyer])
farm_2_img = pygame.image.load("farm_2.png")
farm_2_img = pygame.transform.scale(farm_2_img, [farm_2_img.get_width()*size_multiplyer, farm_2_img.get_height()*size_multiplyer])

red_tint_img = pygame.image.load("red_tint.png")
red_tint_img = pygame.transform.scale(red_tint_img, [red_tint_img.get_width()*size_multiplyer, red_tint_img.get_height()*size_multiplyer])
purple_tint_img = pygame.image.load("purple_tint.png")
purple_tint_img = pygame.transform.scale(purple_tint_img, [purple_tint_img.get_width()*size_multiplyer, purple_tint_img.get_height()*size_multiplyer])
side_gradient_img = pygame.image.load("side_gradient.png")
side_gradient_img = pygame.transform.scale(side_gradient_img, [side_gradient_img.get_width()*size_multiplyer, side_gradient_img.get_height()*size_multiplyer])
zoomed_background_img = pygame.image.load("zoomed_background.png")
zoomed_background_img = pygame.transform.scale(zoomed_background_img, [zoomed_background_img.get_width()*size_multiplyer, zoomed_background_img.get_height()*size_multiplyer])
info_button_img = pygame.transform.scale(pygame.image.load("info_button.png"), [100*size_multiplyer, 50*size_multiplyer])

image_width2 = 60
image_height2 = 180
image_width3 = 90
image_height3 = 90
 
# Define colors and fonts
black = (0, 0, 0)
black2 = (1, 1, 1)
brown = (122, 85, 68)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 120, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)
 
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)
font6 = pygame.font.SysFont("bahnschrift", round(22*size_multiplyer))
 
 
# Create the window
dis_width = 1370
dis_height = 720
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Millitary_Game')
 
# Create the variables needed for the program such as card properties, chip properties, and hands.
clock = pygame.time.Clock()
 
playing = True
info_show = False
tile_clicked = False
 
map_sprites = pygame.sprite.Group()
zoomed_map_sprites = pygame.sprite.Group()
player_1_sprites = pygame.sprite.Group()
player_2_sprites = pygame.sprite.Group()
zoomed_player_1_sprites = pygame.sprite.Group()
zoomed_player_2_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()


 
full_map = [[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
[0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

alterable_full_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0],
[0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, -2, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
 
all_player_1_structure_names = {0:'None', 1:'P1 Home Base', 2:'P1 Barracks', 3:'P1 Farm'}
all_player_2_structure_names = {0:'None', 1:'P2 Home Base', 2:'P2 Barracks', 3:'P2 Farm'}
all_terrain_names = {0: 'Grassland', 1: 'Water', 2: 'Sand', 3: 'Forest', 4: 'Mountain', 5: 'Snow', 6: 'Snowy Mountain'}
 
def load_images(image_list, num, x, y, ck, sprite_sheet, img_width, img_height):
   # Crops a spritesheet and adds the cropped image to a list
    if y == 0:
        correction2 = 0
    else:
        correction2 = 1
    for item in range(0, num):
        # if item == 0:
        correction = 0
        # else:
        #     correction = 1
        image = sprite_sheet.image_at(((x + item) * img_width + correction, y * img_height + correction2, img_width,
                                        img_height), colorkey=ck)
        image_list.append(pygame.transform.scale(image, [image.get_width()*size_multiplyer, image.get_height()*size_multiplyer]))

map_images = []
load_images(map_images, 7, 0, 0, black2, ss, image_width, image_height)
player_1_images = [purple_tint_img, home_base_1_img, barracks_1_img, farm_1_img]
player_2_images = [red_tint_img, home_base_2_img, barracks_2_img, farm_2_img]
button_images = [info_button_img]
image_width = 30*size_multiplyer
image_height = 30*size_multiplyer
 
class TerrainBox(pygame.sprite.Sprite):
    def __init__(self, x, y, sprt_list, type, view):
        super().__init__()
        self.type = type
        self.name = all_terrain_names[type]
        if view == 0:
            self.image = pygame.transform.scale(map_images[type], [map_images[type].get_width()*5, map_images[type].get_height()*5])
        elif view == 1:
            self.image = map_images[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprt_list.add(self)

class PlayerStructure(pygame.sprite.Sprite):
    def __init__(self, x, y, sprt_list, type, view, player):
        super().__init__()
        if player == 1:
            self.type = type+1
            self.name = all_player_1_structure_names[type]
            if view == 0:
                self.image = pygame.transform.scale(player_1_images[type], [player_1_images[type].get_width()*5, player_1_images[type].get_height()*5])
            if view == 1:
                self.image = player_1_images[type]
        elif player == 2:
            self.type = (type+1)*-1
            self.name = all_player_2_structure_names[type]
            if view == 0:
                self.image = pygame.transform.scale(player_2_images[type], [player_2_images[type].get_width()*5, player_2_images[type].get_height()*5])
            if view == 1:
                self.image = player_2_images[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprt_list.add(self)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, sprt_list, type):
        super().__init__()
        self.type = type
        self.image = button_images[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprt_list.add(self)
 
 
def update_dis(type):
    global image_width
    global image_height
    if type == 0:
        dis.fill(black)
        dis.blit(zoomed_background_img, [0, 0])
        dis.blit(side_gradient_img, [image_width*39, 0])
        zoomed_map_sprites.draw(dis)
        zoomed_player_1_sprites.draw(dis)
        zoomed_player_2_sprites.draw(dis)
    
    if type == 1:
        dis.fill(black)
        dis.blit(side_gradient_img, [image_width*39, 20])
        map_sprites.draw(dis)
        player_1_sprites.draw(dis)
        player_2_sprites.draw(dis)
    button_sprites.draw(dis)
    if info_show:
        pygame.draw.rect(dis, black, [0, 0, 1170, 720])

        line_count = 0
        for line in lines:
            line_count += 1
            info_mesg = font4.render(line, True, white)
            dis.blit(info_mesg, [100, 10+line_count*20])
    if tile_clicked:
        terrain_str = f'Terrain: {clicked_tile.name}'
        terrain_mesg = font6.render(terrain_str, True, white)
        dis.blit(terrain_mesg, [image_width*39+image_width//6, 3*image_height])
        if clicked_structure_tile != 0:
            structure_str = f'Structure: {clicked_structure_tile.name}'
            structure_mesg = font6.render(structure_str, True, white)
            dis.blit(structure_mesg, [image_width*39+image_width//6, 4*image_height])
            if clicked_structure_tile.type > 0:
                terrritory_str = 'Territory: Player 1'
            elif clicked_structure_tile.type < 0:
                terrritory_str = 'Territory: Player 2'
            terrritory_mesg = font6.render(terrritory_str, True, white)
            dis.blit(terrritory_mesg, [image_width*39+image_width//6, 5*image_height])
        else:
            structure_str = f'Structure: None'
            structure_mesg = font6.render(structure_str, True, white)
            dis.blit(structure_mesg, [image_width*39+image_width//6, 4*image_height])
            terrritory_str = 'Territory: Neutral'
            terrritory_mesg = font6.render(terrritory_str, True, white)
            dis.blit(terrritory_mesg, [image_width*39+image_width//6, 5*image_height])


    pygame.display.flip()

def make_map(type):
    global mouse_pos
    global image_width
    global image_height
    if type == 0:
        zoomed_map_sprites.empty()
        zoomed_player_1_sprites.empty()
        zoomed_player_2_sprites.empty()
        box_x = mouse_pos[0]//round(30*size_multiplyer)
        box_y = mouse_pos[1]//round(30*size_multiplyer)
        # AVOIDS ERRORS
        if box_x >= 36:
            box_x = 35
        if box_x <= 2:
            box_x = 3
        if box_y >= 22:
            box_y = 22
        if box_y <= 1:
            box_y = 2

        for num in range(4):
            for num2 in range(7):
                TerrainBox(num2*round(image_width*5)+round(image_width*2), num*round(image_height*5)+round(image_height*2), zoomed_map_sprites, full_map[box_y-2+num][box_x-3+num2], 0)
                if alterable_full_map[box_y-2+num][box_x-3+num2] > 0:
                    PlayerStructure(num2*round(image_width*5)+round(image_width*2), num*round(image_height*5)+round(image_height*2), zoomed_player_1_sprites, 0, 0, 1)
                    if alterable_full_map[box_y-2+num][box_x-3+num2] != 1:
                        x_adjustment = (round(image_width*5)-(player_1_images[alterable_full_map[box_y-2+num][box_x-3+num2]-1].get_width()*5))//2
                        y_adjustment = (round(image_height*5)-(player_1_images[alterable_full_map[box_y-2+num][box_x-3+num2]-1].get_height()*5))//2
                        PlayerStructure(num2*round(image_width*5)+round(image_width*2)+x_adjustment, num*round(image_height*5)+round(image_height*2)+y_adjustment, zoomed_player_1_sprites, alterable_full_map[box_y-2+num][box_x-3+num2]-1, 0, 1)
                if alterable_full_map[box_y-2+num][box_x-3+num2] < 0:
                    PlayerStructure(num2*round(image_width*5)+round(image_width*2), num*round(image_height*5)+round(image_height*2), zoomed_player_2_sprites, 0, 0, 2)
                    if alterable_full_map[box_y-2+num][box_x-3+num2] != -1:
                        x_adjustment = (round(image_width*5)-(player_2_images[alterable_full_map[box_y-2+num][box_x-3+num2]*-1-1].get_width()*5))//2
                        y_adjustment = (round(image_width*5)-(player_2_images[alterable_full_map[box_y-2+num][box_x-3+num2]*-1-1].get_height()*5))//2
                        PlayerStructure(num2*round(image_width*5)+round(image_width*2)+x_adjustment, num*round(image_height*5)+round(image_height*2)+y_adjustment, zoomed_player_2_sprites, alterable_full_map[box_y-2+num][box_x-3+num2]*-1-1, 0, 2)

    if type == 1:
        map_sprites.empty()
        player_1_sprites.empty()
        player_2_sprites.empty()
        r_num = -1
        #creates the full map
        for r in full_map:
            r_num += 1
            c_num = -1
            for c in r:
                c_num += 1
                TerrainBox(image_width*c_num, image_height*r_num, map_sprites, c, 1)
        r_num = -1
        #creates the second layer of the map
        for r in alterable_full_map:
            r_num += 1
            c_num = -1
            for c in r:
                c_num += 1
                if c > 0:
                    PlayerStructure(image_width*c_num, image_height*r_num, player_1_sprites, 0, 1, 1)
                    if c != 1:
                        x_adjustment = (image_width-(player_1_images[c-1].get_width()))//2
                        y_adjustment = (image_height-(player_1_images[c-1].get_height()))//2
                        PlayerStructure(image_width*c_num+x_adjustment, image_height*r_num+y_adjustment, player_1_sprites, c-1, 1, 1)
                if c < 0:
                    PlayerStructure(image_width*c_num, image_height*r_num, player_2_sprites, 0, 1, 2)
                    if c != -1:
                        x_adjustment = (image_width-(player_2_images[c*-1-1].get_width()))//2
                        y_adjustment = (image_height-(player_2_images[c*-1-1].get_height()))//2
                        PlayerStructure(image_width*c_num+x_adjustment, image_height*r_num+y_adjustment, player_2_sprites, c*-1-1, 1, 2)

map_view = 1
info_button = Button(image_width*40, image_height, button_sprites, 0)
make_map(1)
map_group_list = [zoomed_map_sprites, map_sprites]
player_1_group_list = [zoomed_player_1_sprites, player_1_sprites]
player_2_group_list = [zoomed_player_2_sprites, player_2_sprites]
while playing:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False
            if event.key == pygame.K_m:
                if map_view == 0:
                    map_view = 1
                    make_map(1)
                elif map_view == 1:
                    make_map(0)
                    map_view = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in button_sprites if s.rect.collidepoint(mouse_pos)]
            for i in clicked_sprites:
                if i == info_button:
                    if info_show:
                        info_show = False
                    else:
                        info_show = True
            clicked_sprites = [s for s in map_group_list[map_view] if s.rect.collidepoint(mouse_pos)]
            for i in clicked_sprites:
                for tile in map_group_list[map_view]:
                    if i == tile:
                        clicked_tile = tile
                        tile_clicked = True
            clicked_sprites = [s for s in player_1_group_list[map_view] if s.rect.collidepoint(mouse_pos)]
            clicked_structure_tile = 0
            for i in clicked_sprites:
                for tile in player_1_group_list[map_view]:
                    if i == tile:
                        clicked_structure_tile = tile
            if clicked_structure_tile == 0:
                clicked_sprites = [s for s in player_2_group_list[map_view] if s.rect.collidepoint(mouse_pos)]
                for i in clicked_sprites:
                    for tile in player_2_group_list[map_view]:
                        if i == tile:
                            clicked_structure_tile = tile
    keys = pygame.key.get_pressed()
    update_dis(map_view)
    clock.tick(60)

pygame.quit()