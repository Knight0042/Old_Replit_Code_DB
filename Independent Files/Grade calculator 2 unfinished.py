import pygame
import math

pygame.init()
dis_width = 1200
dis_height = 690
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Drawing')
clock = pygame.time.Clock()
running = True

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148,0,211)
orange = (255,165,0)
yellow = (255,255,0)
gray = (75, 75, 75)
gray2 = (100, 100, 100)
brown = (165,42,42)
backround_color = black

all_sprites = pygame.sprite.Group()
framerate = 30

def update_dis():
    dis.fill(backround_color)
    all_sprites.draw(dis)
    pygame.display.flip()

class TextBox(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((1, 1, 1))
        self.image.set_colorkey((1, 1, 1))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)

# student_total1 = float(input('Student Total 1: '))
# student_total2 = float(input('Student Total 2: '))
# Max1 = float(input('Max Total 1: '))
# Max2 = float(input('Max Total 2: '))
# if Max1 == 0:
#     Max1 = 1
# if Max2 == 0:
#     Max2 = 1
# weight1 = float(input('Weight of First Total: '))
# weight2 = float(input('Weight of Second Total: '))
# total1 = (student_total1/Max1)*weight1
# total2 = (student_total2/Max2)*weight2
# end_percentage = (total1+total2)

# print('The End Percentage is: %', end_percentage)

student_total1_text_box = TextBox(white, 42, 100, 80, 25)
student_total2_text_box = TextBox(white, 42, 150, 80, 25)
student_total3_text_box = TextBox(white, 42, 200, 80, 25)
student_max1_text_box = TextBox(white, 142, 100, 80, 25)
student_max2_text_box = TextBox(white, 142, 150, 80, 25)
student_max3_text_box = TextBox(white, 142, 200, 80, 25)

while running:
    update_dis()
    clock.tick(framerate)
