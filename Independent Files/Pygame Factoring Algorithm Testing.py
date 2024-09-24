import pygame, sys
from pygame.locals import QUIT
import math
from functools import reduce

pygame.init()
dis_width = 1280
dis_height = 720
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Hello World!')

black = (0, 0, 0)
black2 = (1, 1, 1)
white = (255, 255, 255)
red = (205, 0, 0)
blue = (0, 0, 205)
green = (0, 120, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)
gray3 = (240, 240, 240)
gray4 = (150, 150, 150)
gray5 = (120, 120, 120)

level_select_menu_button_sprites = pygame.sprite.Group()


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type, angle, type2):
        super().__init__()
        rectangle = pygame.Surface([width, height])
        rectangle.fill(color)
        self.image = rectangle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.count = 999999
        self.type2 = type2
        self.angle = angle
        if type == 3:
            level_select_menu_button_sprites.add(self)


def dis_update():
    dis.fill(gray3)
    level_select_menu_button_sprites.draw(dis)

    pygame.display.flip()


def factor(n):
    return reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))


map_list = []

while True:
    start_time = pygame.time.get_ticks()
    map_list.append(0)
    level_select_menu_button_sprites.empty()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    map_count = len(map_list)
    factor_list = factor(map_count)
    if len(factor_list) == 2 and map_count > 3:
        factor_list = factor(map_count + 1)
    lowest_factor_total = 99999999
    for f in range(0, len(factor_list), 2):
        factor_total = factor_list[f] + factor_list[f + 1]
        if factor_total < lowest_factor_total:
            lowest_factor_total = factor_total
            factor_1 = factor_list[f]
            factor_2 = factor_list[f + 1]

    button_gap = 10
    left_border = 40
    right_border = 170
    top_border = 120
    bottom_border = 40
    button_width = (dis_width - (left_border + right_border) - (button_gap * (factor_2 - 1))) / (factor_2)
    button_height = (dis_height - (top_border + bottom_border) - (button_gap * (factor_1 - 1))) / (factor_1)

    i = 0
    for r in range(factor_1):
        for c in range(factor_2):
            if not i >= len(map_list):
                menu_button = Button(button_width, button_height, c * (button_width + button_gap) + left_border,
                                     r * (button_height + button_gap) + top_border, red, 3, 0, i)
            i += 1
    dis_update()
    end_time = pygame.time.get_ticks()
    process_time = end_time - start_time
    if process_time < 600:
        pygame.time.wait(600 - process_time)
