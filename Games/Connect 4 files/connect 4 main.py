import pygame

pygame.init()
dis_width = 1000
dis_height = 680
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)

transparent_img = pygame.image.load("90x50_transparent.png")
down_arrow_img = pygame.image.load("down_arrow.png")
red_wins_img = pygame.image.load("red_wins_image.png")
yellow_wins_img = pygame.image.load("yellow_wins_image.png")

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

Gameboard = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

playing = True
backround_color = white

all_sprites = pygame.sprite.Group()

winner = 0

def update_dis():
    dis.fill(backround_color)
    pygame.draw.rect(dis, brown, [155, 52, 690, 575])
    r_num = 0
    for r in Gameboard:
        r_num += 1
        c_num = 0
        for c in r:
            c_num += 1
            if c == 0:
                pygame.draw.circle(dis, backround_color, [95*c_num+120, 95*r_num+7], 40)
            elif c == 1:
                pygame.draw.circle(dis, yellow, [95*c_num+120, 95*r_num+7], 40)
            elif c == 2:
                pygame.draw.circle(dis, red, [95*c_num+120, 95*r_num+7], 40)
    all_sprites.draw(dis)
    if winner == 1:
        dis.blit(yellow_wins_img, [150, 89])
    elif winner == 2:
        dis.blit(red_wins_img, [150, 89])
    pygame.display.flip()

def check_for_winner():
    global winner
    yellow_count = 0
    red_count = 0

    for num in range(3):
        for numb in range(4):
            for numbe in range(4):
                if Gameboard[num+numbe][numb+numbe]:
                    yellow_count += 1
                if Gameboard[num+numbe][numb+numbe] == 0 or Gameboard[num+numbe][numb+numbe] == 2:
                    yellow_count = 0
                if yellow_count >= 4:
                    winner = 1
    yellow_count = 0
    red_count = 0
    for num in range(3):
        for numb in range(6, 3, -1):
            for numbe in range(4):
                if Gameboard[num+numbe][numb-numbe]:
                    yellow_count += 1
                if Gameboard[num+numbe][numb-numbe] == 0 or Gameboard[num+numbe][numb-numbe] == 2:
                    yellow_count = 0
                if yellow_count >= 4:
                    winner = 1
    yellow_count = 0
    red_count = 0
    for num in range(7):
        for r in Gameboard:
            if r[num] == 1:
                yellow_count += 1
            elif r[num] == 0 or r[num] == 2:
                yellow_count = 0
            if r[num] == 2:
                red_count += 1
            elif r[num] == 0 or r[num] == 2:
                red_count = 0
            if yellow_count >= 4:
                winner = 1
            if red_count >= 4:
                winner = 2
            for c in r:
                yellow_count = 0
                red_count = 0
                if c == 1:
                    yellow_count += 1
                elif c == 0 or c == 2:
                    yellow_count = 0
                if c == 2:
                    red_count += 1
                elif c == 0 or c == 1:
                    red_count = 0
                if yellow_count >= 4:
                    winner = 1
                if red_count >= 4:
                    winner = 2

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)
    def change(self, img):
        self.image = img

for num in range(7):
    c_space = Button(num*95+170, 0, transparent_img)

chip_type = 1

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                for s in all_sprites:
                    if i == s:
                        for num_ in range(7):
                            if s.rect.x == 95*num_+170:
                                for num in range(5, -1, -1):
                                    if Gameboard[num][num_] == 0:
                                        Gameboard[num][num_] = chip_type
                                        if chip_type == 1:
                                            chip_type = 2
                                        elif chip_type == 2:
                                            chip_type = 1
                                        break

    pos = pygame.mouse.get_pos()
    clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
    for s in clicked_sprites:
        s.change(down_arrow_img)
    
    update_dis()
    check_for_winner()
    for s in all_sprites:
        s.change(transparent_img)
    clock.tick(30)
