import pygame
import random

pygame.init()
dis_width = 1000
dis_height = 680
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Aim Trainer')
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)
font6 = pygame.font.SysFont("bahnschrift", 70)

target_img = pygame.image.load("target.png")
stop_button_img = pygame.image.load("stop_button.png")
start_button_img = pygame.image.load("start_button_img.png")
target_num_img = pygame.image.load("target_num_button_img.png")

black = (0, 0, 0)
black2 = (1, 1, 1)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 100)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (75, 75, 75)
gray2 = (100, 100, 100)
brown = (165, 42, 42)

backround_color = white
stop = False

all_sprites = pygame.sprite.Group()
all_start_sprites = pygame.sprite.Group()
score = 0
timer = 0
shot_attempts = 0
target_string = '3'


def update_dis(num):
    dis.fill(backround_color)
    if num == 0:
        all_start_sprites.draw(dis)
        target_mesg = font6.render(target_string, True, black)
        if timer != 0:
            tar_a_sec_mesg = font3.render(f"{(int((score / timer) * 100)) / 100} Targets a Second", True, black)
            dis.blit(tar_a_sec_mesg, [450, 110])
        if shot_attempts != 0:
            tar_acc_mesg = font3.render(f"%{int((score / shot_attempts) * 100)} Accuracy", True, black)
            dis.blit(tar_acc_mesg, [450, 150])
        dis.blit(target_mesg, [355, 100])
    if num == 1:
        all_sprites.draw(dis)
        score_mesg = font2.render((f"Score: {score}   Timer:{int(timer)}"), True, black)
        dis.blit(score_mesg, [350, 20])

    pygame.display.flip()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img, type):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        if self.type == 0 or self.type == 1:
            all_sprites.add(self)
        elif self.type > 1:
            all_start_sprites.add(self)

    def change(self, img):
        self.image = img


def make_new_target():
    target = Button(random.randrange(100, 900), random.randrange(100, 550), target_img, 0)


def create_starting_targets():
    global score
    global timer
    global shot_attempts
    shot_attempts = 0
    score = 0
    timer = 0
    for sp in all_sprites:
        sp.kill()
    for n in range(int(target_string)):
        make_new_target()
    stop_button = Button(200, 10, stop_button_img, 1)


def start_game():
    start_button = Button(150, 200, start_button_img, 2)
    target_num_button = Button(150, 100, target_num_img, 3)


start_game()
initiating = True
while initiating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            initiating = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                initiating = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_start_sprites if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                for spr in all_start_sprites:
                    if i == spr:
                        if spr.type == 2:
                            playing = True
                            create_starting_targets()
                            while playing:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        playing = False
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            playing = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        shot_attempts += 1
                                        pos = pygame.mouse.get_pos()
                                        clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                                        for i in clicked_sprites:
                                            position = 0
                                            for s in all_sprites:
                                                if s.type == 1:
                                                    if i == s:
                                                        stop = True
                                                        break
                                                elif i == s:

                                                    score += 1
                                                    s.kill()
                                                    make_new_target()
                                                position += 1

                                timer += 1 / 30
                                update_dis(1)
                                if stop:
                                    pygame.draw.rect(dis, red, [0, 180, 1000, 200])
                                    stop_mesg = font6.render(f"{(int((score / timer) * 100)) / 100} Targets a Second",
                                                             True, black)
                                    dis.blit(stop_mesg, [0, 200])
                                    stop_mesg2 = font6.render(f"%{int((score / shot_attempts) * 100)} Accuracy", True,
                                                              black)
                                    dis.blit(stop_mesg2, [0, 250])
                                    pygame.display.flip()
                                    pygame.time.wait(5000)
                                    playing = False
                                    stop = False
                                clock.tick(30)
                        if spr.type == 3:
                            inputting = True
                            while inputting:
                                event = pygame.event.poll()

                                if event.type == pygame.KEYDOWN:
                                    key = pygame.key.name(event.key)  # Returns string id of pressed key.
                                    for num in range(0, 10):
                                        if key == str(num):
                                            target_string += key
                                        if key == 'backspace':
                                            target_string = ''
                                        if key == 'return':
                                            if target_string == '':
                                                target_string = '1'
                                            else:
                                                if int(target_string) > 100:
                                                    target_string = '100'
                                            typed = True
                                            inputting = False
                                update_dis(0)
        update_dis(0)
        clock.tick(30)
pygame.quit()
