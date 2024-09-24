import pygame
import spritesheet
import random

ss =  spritesheet.spritesheet('monster_head_fire_spritesheet.png')
ss2 =  spritesheet.spritesheet('monster_mouth_animation.png')

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

player_img = pygame.image.load("player_img.png")
you_died_img = pygame.image.load("you_died.png")
you_win_img = pygame.image.load("you_win.png")
heart_img = pygame.transform.scale(pygame.image.load("heart.png"), [30, 30])
fight_button_img = pygame.transform.scale(pygame.image.load("fight_button.png"), [100, 50])
item_button_img = pygame.transform.scale(pygame.image.load("item_button.png"), [100, 50])
projectile1_img = pygame.image.load("projectile1.png")
projectile2_img = pygame.image.load("projectile2.png")
projectile3_img = pygame.image.load("projectile3.png")
projectile4_img = pygame.transform.rotate(projectile2_img, 90)
projectile5_img = pygame.transform.rotate(projectile3_img, 90)

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
test_num = 0
test_num2 = 0
test_num2_val = 1

backround_color = black
playing = True
attacking = True
frame_rate = 30
ply_spd = 4
timer = 1
timer2 = 0
timer3 = 0
rewind = False
enemy_death_stage = 0
attack_timer = 0
invincibility_timer = frame_rate
player_health = 100
enemy_health = 100
attack = random.randrange(1, 3)
variation = 1
all_sprites = pygame.sprite.Group()
all_button_sprites = pygame.sprite.Group()
all_start_sprites = pygame.sprite.Group()
all_projectile_sprites = pygame.sprite.Group()

head_images = []
mouth_images = []
image_width = 38
image_height = 60
image_height2 = 30

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



load_images(head_images, 14, 0, 0, black2, ss, image_width, image_height)
load_images(mouth_images, 5, 0, 0, black2, ss2, image_width, image_height2)

def update_dis(num, num2):
    global test_num
    global test_num2
    if num == 0:
        dis.fill(backround_color)
        pygame.draw.rect(dis, white, [350, 300, 300, 250], 10)
        dis.blit(heart_img, (310, 575))
        player_health_mesg = font2.render((f"Player Health {player_health}/100"), True, white)
        dis.blit(player_health_mesg, (350, 575))
        dis.blit(heart_img, (310, 250))
        player_health_mesg = font2.render((f"Enemy Health {enemy_health}/100"), True, white)
        dis.blit(player_health_mesg, (350, 250))
        # pygame.draw.line(dis, white,(350,300),(650,550), 50)
        # pygame.draw.line(dis, white,(350,550),(650,300), 50)
        all_sprites.draw(dis)
        if num2 == 1:
            all_projectile_sprites.draw(dis)
        elif num2 == 2:
            all_button_sprites.draw(dis)
        elif num2 == 3:
            dis.blit(you_died_img, [250, 375])
        elif num2 == 4:
            dis.blit(you_win_img, [250, 375])
        dis.blit(head_images[test_num], [462, 50])
        dis.blit(mouth_images[test_num2], [464, 118])

    
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
        elif self.type > 1:
            all_start_sprites.add(self)
    def move(self, d):
        if d == 1:
            self.rect.x += ply_spd
            if self.rect.x >= 622:
                self.rect.x -= ply_spd
        if d == 2:
            self.rect.y += ply_spd
            if self.rect.y >= 522:
                self.rect.y -= ply_spd
        if d == 3:
            self.rect.x -= ply_spd
            if self.rect.x <= 353:
                self.rect.x += ply_spd
        if d == 4:
            self.rect.y -= ply_spd
            if self.rect.y <= 302:
                self.rect.y += ply_spd

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, img, stage, num):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.org_x = x
        self.org_y = y
        self.stage = stage
        self.num = num
        all_projectile_sprites.add(self)
    def move_pattern(self):
        if self.num == 0:
            self.stage += 1
            if self.stage >= frame_rate:
                self.kill()
        if self.num == 1:
            if self.stage == 1:
                self.rect.x += 3
                self.rect.y += 2
                if self.rect.x == self.org_x + 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x += 3
                self.rect.y += 1
                if self.rect.x == self.org_x + 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x += 3
                self.rect.y -= 1
                if self.rect.x == self.org_x + 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x += 3
                self.rect.y -= 2
                if self.rect.x == self.org_x + 360:
                    self.kill()
        if self.num == 2:
            if self.stage == 1:
                self.rect.x += 3
                self.rect.y -= 2
                if self.rect.x == self.org_x + 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x += 3
                self.rect.y -= 1
                if self.rect.x == self.org_x + 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x += 3
                self.rect.y += 1
                if self.rect.x == self.org_x + 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x += 3
                self.rect.y += 2
                if self.rect.x == self.org_x + 360:
                    self.kill()
        if self.num == 3:
            if self.stage == 1:
                self.rect.x -= 3
                self.rect.y -= 2
                if self.rect.x == self.org_x - 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x -= 3
                self.rect.y -= 1
                if self.rect.x == self.org_x - 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x -= 3
                self.rect.y += 1
                if self.rect.x == self.org_x - 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x -= 3
                self.rect.y += 2
                if self.rect.x == self.org_x - 360:
                    self.kill()
        if self.num == 4:
            if self.stage == 1:
                self.rect.x -= 3
                self.rect.y += 2
                if self.rect.x == self.org_x - 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x -= 3
                self.rect.y += 1
                if self.rect.x == self.org_x - 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x -= 3
                self.rect.y -= 1
                if self.rect.x == self.org_x - 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x -= 3
                self.rect.y -= 2
                if self.rect.x == self.org_x - 360:
                    self.kill()
        if self.num == 5:
            if self.stage == 1:
                self.rect.x += 2
                self.rect.y += 3
                if self.rect.y == self.org_y + 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x += 1
                self.rect.y += 3
                if self.rect.y == self.org_y + 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x -= 1
                self.rect.y += 3
                if self.rect.y == self.org_y + 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x -= 2
                self.rect.y += 3
                if self.rect.y == self.org_y + 360:
                    self.kill()
        if self.num == 6:
            if self.stage == 1:
                self.rect.x += 2
                self.rect.y -= 3
                if self.rect.y == self.org_y - 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x += 1
                self.rect.y -= 3
                if self.rect.y == self.org_y - 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x -= 1
                self.rect.y -= 3
                if self.rect.y == self.org_y - 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x -= 2
                self.rect.y -= 3
                if self.rect.y == self.org_y - 360:
                    self.kill()
        if self.num == 7:
            if self.stage == 1:
                self.rect.x -= 2
                self.rect.y -= 3
                if self.rect.y == self.org_y - 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x -= 1
                self.rect.y -= 3
                if self.rect.y == self.org_y - 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x += 1
                self.rect.y -= 3
                if self.rect.y == self.org_y - 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x += 2
                self.rect.y -= 3
                if self.rect.y == self.org_y - 360:
                    self.kill()
        if self.num == 8:
            if self.stage == 1:
                self.rect.x -= 2
                self.rect.y += 3
                if self.rect.y >= self.org_y + 90:
                    self.stage = 2
            elif self.stage == 2:
                self.rect.x -= 1
                self.rect.y += 3
                if self.rect.y >= self.org_y + 180:
                    self.stage = 3
            elif self.stage == 3:
                self.rect.x += 1
                self.rect.y += 3
                if self.rect.y >= self.org_y + 270:
                    self.stage = 4
            elif self.stage == 4:
                self.rect.x += 2
                self.rect.y += 3
                if self.rect.y >= self.org_y + 360:
                    self.kill()
        if self.num == 9:
            self.rect.x += 4
            self.stage += 1
            if self.stage >= frame_rate:
                self.kill()
        if self.num == 10:
            self.rect.x -= 4
            self.stage += 1
            if self.stage >= frame_rate:
                self.kill()
        if self.num == 11:
            self.rect.y -= 4
            self.stage += 1
            if self.stage >= frame_rate:
                self.kill()
        if self.num == 12:
            self.rect.y += 4
            self.stage += 1
            if self.stage >= frame_rate:
                self.kill()

                
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img, type):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        if self.type == 0 or self.type == 1:
            all_button_sprites.add(self)
        elif self.type > 1:
            all_start_sprites.add(self)

def damage(amount, id):
    global player_health
    global enemy_health
    if id == 1:
        enemy_health -= amount
    if id == 2:
        player_health -= amount
        if player_health > 100:
            player_health = 100
# test_projectile = Projectile(310, 300, projectile2_img, 1, 1)
player = Player(493, 450, player_img, 1)
fight_button = Button(200, 350, fight_button_img, 1)
item_button = Button(200, 450, item_button_img, 1)


while playing:
    
    for p in all_projectile_sprites:
        p.move_pattern()
        if p.rect.colliderect(player):
            if invincibility_timer >= 1:
                invincibility_timer = 0
                damage(10, 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_menu = False
        if event.type == pygame.MOUSEBUTTONDOWN and not attacking:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_button_sprites if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                if i == fight_button:
                    damage(10, 1)
                    attacking = True
                if i == item_button:
                    damage(-15, 2)
                    attacking = True



    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(3)
    if keys[pygame.K_w]:
        player.move(4)
    if keys[pygame.K_d]:
        player.move(1)
    if keys[pygame.K_s]:
        player.move(2)
    if timer >= 2-enemy_death_stage/2:
        if attack == 1:
            test_projectile = Projectile(310, 300+attack_timer*10, projectile1_img, 1, 1)
            test_projectile = Projectile(310, 550-attack_timer*10, projectile1_img, 1, 2)
            test_projectile = Projectile(670, 550-attack_timer*10, projectile1_img, 1, 3)
            test_projectile = Projectile(670, 300+attack_timer*10, projectile1_img, 1, 4)
            test_projectile = Projectile(340+attack_timer*10, 260, projectile1_img, 1, 5)
            test_projectile = Projectile(340+attack_timer*10, 590, projectile1_img, 1, 6)
            test_projectile = Projectile(660-attack_timer*10, 590, projectile1_img, 1, 7)
            test_projectile = Projectile(660-attack_timer*10, 300, projectile1_img, 1, 8)
        if attack == 2:
            test_projectile = Projectile(310, 250+attack_timer*10, projectile2_img, 1, 1)
            test_projectile = Projectile(670, 500-attack_timer*10, projectile2_img, 1, 3)
            test_projectile = Projectile(310, 500-attack_timer*10, projectile2_img, 1, 2)
            test_projectile = Projectile(670, 250+attack_timer*10, projectile2_img, 1, 4)
        if attack == 3:
            if variation == 1:
                test_projectile = Projectile(475, 250, projectile3_img, 1, 0)
                variation = 2
            elif variation == 2:
                test_projectile = Projectile(315, 250, projectile3_img, 1, 9)
                test_projectile = Projectile(635, 250, projectile3_img, 1, 10)
                variation = 1
        if attack == 4:
            test_projectile = Projectile(320+attack_timer*10, 250, projectile4_img, 1, 5)
            test_projectile = Projectile(320+attack_timer*10, 580, projectile4_img, 1, 6)
            test_projectile = Projectile(580-attack_timer*10, 580, projectile4_img, 1, 7)
            test_projectile = Projectile(580-attack_timer*10, 250, projectile4_img, 1, 8)
        if attack == 5:
            if variation == 1:
                test_projectile = Projectile(300, 400, projectile5_img, 1, 0)
                variation = 2
            elif variation == 2:
                test_projectile = Projectile(300, 550, projectile5_img, 1, 11)
                test_projectile = Projectile(300, 225, projectile5_img, 1, 12)
                variation = 1
        timer = 0
    if attacking:
        if attack_timer == 0:
            attack = random.randrange(1, 6)
            variation = 1
        timer += 1/frame_rate
        attack_timer += 1/frame_rate
        
        if attack_timer >= 10:
            for pro in all_projectile_sprites:
                pro.kill()
            attack_timer = 0
            timer = 1
            attacking = False
        invincibility_timer += 1/frame_rate
        update_dis(0, 1)
    else:
        update_dis(0, 2)
    if player_health <= 0:
        update_dis(0, 3)
        playing = False
    elif enemy_health <= 0:
        enemy_death_stage += 1
        enemy_health = 100
    if enemy_death_stage == 1:
        if timer2 == frame_rate/10/frame_rate and test_num < 9:
            test_num += 1
            if test_num > 13:
                test_num = 9
            timer2 = 0
        elif timer2 == frame_rate/6/frame_rate:
            test_num += 1
            if test_num > 13:
                test_num = 10
            timer2 = 0
        timer2 += 1/frame_rate
    elif enemy_death_stage == 2:
        update_dis(0, 4)
        playing = False
    if timer3 == frame_rate/6/frame_rate:
        test_num2 += test_num2_val
        if rewind:
            test_num2 -= 4
            rewind = False
        if test_num2 == 2:
            test_num2_val = -1
        elif test_num2 < 0:
            test_num2 += 4
            test_num2_val = 1
        elif test_num2 > 4:
            test_num2 -= 2
            test_num2_val = 1
            rewind = True

        timer3 = 0

    timer3 += 1/frame_rate
    # player_health = 100
    clock.tick(frame_rate)