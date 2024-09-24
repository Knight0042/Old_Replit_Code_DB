import pygame
import random
# from replit import audio

# source = audio.play_file('music.mp3')

pygame.init()
 
lose_bg = pygame.image.load("lose_bg.png")
lose_bg = pygame.transform.scale(lose_bg, (1400, 691))

# LOAD ALL NEEDED IMAGES
 
# bg = pygame.image.load("bg.png")
# bg = pygame.transform.scale(bg, (1600, 400))
 
# bg2 = pygame.image.load("bg2.png")
# bg2 = pygame.transform.scale(bg2, (1600, 690))
 
f_player_image = pygame.image.load("f1player.png")
l_player_image = pygame.image.load("l1player.png")
r_player_image = pygame.image.load("r1player.png")
b_player_image = pygame.image.load("b1player.png")
 
projectile_image = pygame.image.load("projectile.png")
projectile_image2 = pygame.image.load("projectile2.png")
projectile_box_image = pygame.image.load("projectile_box.png")
 
f_enm1_image = pygame.image.load("f1enm1.png")
f_enm1_image2 = pygame.image.load("f2enm1.png")
f_enm1_image3 = pygame.image.load("f3enm1.png")

l_enm1_image = pygame.image.load("l1enm1.png")
l_enm1_image2 = pygame.image.load("l2enm1.png")
l_enm1_image3 = pygame.image.load("l3enm1.png")

r_enm1_image = pygame.image.load("r1enm1.png")
r_enm1_image2 = pygame.image.load("r2enm1.png")
r_enm1_image3 = pygame.image.load("r3enm1.png")

b_enm1_image = pygame.image.load("b1enm1.png")
b_enm1_image2 = pygame.image.load("b2enm1.png")
b_enm1_image3 = pygame.image.load("b3enm1.png")
 
f_enm2_image = pygame.image.load("f1enm2.png")
f_enm2_image2 = pygame.image.load("f2enm2.png")
f_enm2_image3 = pygame.image.load("f3enm2.png")

l_enm2_image = pygame.image.load("l1enm2.png")
l_enm2_image2 = pygame.image.load("l2enm2.png")
l_enm2_image3 = pygame.image.load("l3enm2.png")

r_enm2_image = pygame.image.load("r1enm2.png")
r_enm2_image2 = pygame.image.load("r2enm2.png")
r_enm2_image3 = pygame.image.load("r3enm2.png")

b_enm2_image = pygame.image.load("b1enm2.png")
b_enm2_image2 = pygame.image.load("b2enm2.png")
b_enm2_image3 = pygame.image.load("b3enm2.png")
 
f_enm3_image = pygame.image.load("f1enm3.png")
l_enm3_image = pygame.image.load("l1enm3.png")
r_enm3_image = pygame.image.load("r1enm3.png")
b_enm3_image = pygame.image.load("b1enm3.png")
 
f_senm_image = pygame.image.load("f1senm.png")
f_senm_image2 = pygame.image.load("f2senm.png")
f_senm_image3 = pygame.image.load("f3senm.png")

l_senm_image = pygame.image.load("l1senm.png")
l_senm_image2 = pygame.image.load("l2senm.png")
l_senm_image3 = pygame.image.load("l3senm.png")

r_senm_image = pygame.image.load("r1senm.png")
r_senm_image2 = pygame.image.load("r2senm.png")
r_senm_image3 = pygame.image.load("r3senm.png")

b_senm_image = pygame.image.load("b1senm.png")
b_senm_image2 = pygame.image.load("b2senm.png")
b_senm_image3 = pygame.image.load("b3senm.png")

f_enm4_image = pygame.image.load("f1enm4.png")
f_enm4_image2 = pygame.image.load("f2enm4.png")
f_enm4_image3 = pygame.image.load("f3enm4.png")

l_enm4_image = pygame.image.load("l1enm4.png")
l_enm4_image2 = pygame.image.load("l2enm4.png")
l_enm4_image3 = pygame.image.load("l3enm4.png")

r_enm4_image = pygame.image.load("r1enm4.png")
r_enm4_image2 = pygame.image.load("r2enm4.png")
r_enm4_image3 = pygame.image.load("r3enm4.png")

b_enm4_image = pygame.image.load("b1enm4.png")
b_enm4_image2 = pygame.image.load("b2enm4.png")
b_enm4_image3 = pygame.image.load("b3enm4.png")

initiate = True
# g = 0

# textures = {
#     g : pygame.image.load("grass.png")

#     }

# tilemap = [
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
#        [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g]
#     ]
# tilesize = 90
# mapwidth = len(tilemap[0])
# mapheight = len(tilemap)
 
heart_image = pygame.image.load("heart.png")
heart_image = pygame.transform.scale(heart_image, (30, 30))
 
health_potion_image = pygame.image.load("Health_potion.png")

# AVAILABLE COLORS

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148,0,211)
orange = (255,165,0)
yellow = (255,255,0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)

# NEEDED STUFF

dis_width = 1290
dis_height = 690
clock = pygame.time.Clock()
dis =  pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('2d Shooter Game')
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)

score = 0

highscore = 0
previous_score = 0

while initiate:
  
  dis.fill(black)
  message1 = font5.render('Press P to Start', 1, white)
  message2 = font2.render(f'Highscore: {highscore}', 1, white)
  message3 = font2.render(f'Previous Score: {previous_score}', 1, white)
  dis.blit(message1, (130, dis_height/2-37))
  dis.blit(message2, (150, dis_height/2-200))
  dis.blit(message3, (850, dis_height/2-200))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      initiate = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        initiate = False
      if event.key == pygame.K_p:

        # INITIAL VARIABLES

        running = True
        score = 0
        # backround_x = 0
        # jump_cooldown = 120
        shot_cooldown = 100
        shot_cooldown2 = 100
        spawn_cooldown = 300
        spawn_cooldown2 = 300
        spawn_cooldown3 = 300
        spawn_cooldown4 = 300
        spawn_cooldown5 = 300
        spawn_cooldown6 = 300
        shooting = False
        shooting2 = False
        spawned = False
        facing_direction = 'd'

        walk_cycle = 0
        walk_cycle2 = 0
        walk_cycle3 = 0
        walk_cycle4 = 4
        
        projectile_box_count = 0
        health_remaining = 300
        hit_count = 0
        hit_count2 = 0

        # USED CLASSES AND FUNCTIONS

        class Player(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_player_image
            self.rect = self.image.get_rect()
          
          def moveUp(self, pixels):
            self.rect.y -= pixels
            self.image = b_player_image
            if self.rect.y < 50:
              self.rect.y = 50
          
          def moveDown(self, pixels):
            self.rect.y += pixels
            self.image = f_player_image
            if self.rect.y > dis_height - 50:
              self.rect.y = dis_height - 50
          
          def moveLeft(self, pixels):
            self.rect.x -= pixels
            self.image = l_player_image
            if self.rect.x < 0:
              self.rect.x = 0
          
          def moveRight(self, pixels):
            self.rect.x += pixels
            self.image = r_player_image
            if self.rect.x > dis_width - 20:
              self.rect.x = dis_width - 20
          
          def jump_up(self, pixels):
              self.rect.y -= pixels
              all_sprites.update()
          
          def jump_down(self, pixels):
            self.rect.y += pixels
            all_sprites.update()
          
          
        class Projectile(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = projectile_image
            self.rect = self.image.get_rect()
          def shoot_right(self, pixels):
            self.rect.x += pixels
          
          def shoot_left(self, pixels):
            self.rect.x -= pixels
          
          def shoot_up(self, pixels):
            self.rect.y -= pixels
          
          def shoot_down(self, pixels):
            self.rect.y += pixels

        
        class Projectile2(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = projectile_image2
            self.rect = self.image.get_rect()
          def shoot_right(self, pixels):
            self.rect.x += pixels
          
          def shoot_left(self, pixels):
            self.rect.x -= pixels
          
          def shoot_up(self, pixels):
            self.rect.y -= pixels
          
          def shoot_down(self, pixels):
            self.rect.y += pixels
          

        class SpawnedEnemy(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_senm_image
            self.rect = self.image.get_rect()
        
          def tracker (self, the_player, cycle):
            if the_player.rect.y > self.rect.y:
              self.rect.y += 3
              if cycle <= 5 and cycle > 0:
                self.image = f_senm_image2
              elif cycle <= 10 and cycle > 5:
                self.image = f_senm_image3
              else:
                self.image = f_senm_image
                
            if the_player.rect.y < self.rect.y:
              self.rect.y -= 3
              if cycle <= 5 and cycle > 0:
                self.image = b_senm_image2
              elif cycle <= 10 and cycle > 5:
                self.image = b_senm_image3
              else:
                self.image = b_senm_image
            if the_player.rect.x > self.rect.x:
              self.rect.x += 3
              if cycle <= 5 and cycle > 0:
                self.image = r_senm_image2
              elif cycle <= 10 and cycle > 5:
                self.image = r_senm_image3
              else:
                self.image = r_senm_image
            if the_player.rect.x < self.rect.x:
              self.rect.x -= 3
              if cycle <= 5 and cycle > 0:
                self.image = l_senm_image2
              elif cycle <= 10 and cycle > 5:
                self.image = l_senm_image3
              else:
                self.image = l_senm_image
        
        
        class Enemy1(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_enm1_image
            self.rect = self.image.get_rect()
        
          def tracker (self, the_player, cycle):
            if the_player.rect.y > self.rect.y:
              self.rect.y += 1
              if cycle <= 10 and cycle > 0:
                self.image = f_enm1_image2
              elif cycle <= 20 and cycle > 10:
                self.image = f_enm1_image3
              else:
                self.image = f_enm1_image
            if the_player.rect.y < self.rect.y:
              self.rect.y -= 1
              if cycle <= 10 and cycle > 0:
                self.image = b_enm1_image2
              elif cycle <= 20 and cycle > 10:
                self.image = b_enm1_image3
              else:
                self.image = b_enm1_image
            if the_player.rect.x > self.rect.x:
              self.rect.x += 1
              if cycle <= 10 and cycle > 0:
                self.image = r_enm1_image2
              elif cycle <= 20 and cycle > 10:
                self.image = r_enm1_image3
              else:
                self.image = r_enm1_image
            if the_player.rect.x < self.rect.x:
              self.rect.x -= 1
              if cycle <= 10 and cycle > 0:
                self.image = l_enm1_image2
              elif cycle <= 20 and cycle > 10:
                self.image = l_enm1_image3
              else:
                self.image = l_enm1_image
        
        
        class Enemy2(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_enm2_image
            self.rect = self.image.get_rect()
          
          def tracker (self, the_player, cycle):
            if the_player.rect.y > self.rect.y:
              self.rect.y += 2
              if cycle <= 7 and cycle > 0:
                self.image = f_enm2_image2
              elif cycle <= 14 and cycle > 7:
                self.image = f_enm2_image3
              else:
                self.image = f_enm2_image
            if the_player.rect.y < self.rect.y:
              self.rect.y -= 2
              if cycle <= 7 and cycle > 0:
                self.image = b_enm2_image2
              elif cycle <= 14 and cycle > 7:
                self.image = b_enm2_image3
              else:
                self.image = b_enm2_image
            if the_player.rect.x > self.rect.x:
              self.rect.x += 2
              if cycle <= 7 and cycle > 0:
                self.image = r_enm2_image2
              elif cycle <= 14 and cycle > 7:
                self.image = r_enm2_image3
              else:
                self.image = r_enm2_image
            if the_player.rect.x < self.rect.x:
              self.rect.x -= 2
              if cycle <= 7 and cycle > 0:
                self.image = l_enm2_image2
              elif cycle <= 14 and cycle > 7:
                self.image = l_enm2_image3
              else:
                self.image = l_enm2_image
        
        class Enemy3(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_enm3_image
            self.rect = self.image.get_rect()
          
          def tracker (self, the_player):
            if the_player.rect.y > self.rect.y:
              self.rect.y -= 2
              if self.rect.y < 53:
                self.rect.y = 53
                self.image = f_enm3_image
              else:
                self.image = b_enm3_image
            if the_player.rect.y < self.rect.y:
              self.rect.y += 2
              if self.rect.y > dis_height - 60:
                self.rect.y = dis_height - 60
                self.image = b_enm3_image
              else:
                self.image = f_enm3_image
            if the_player.rect.x > self.rect.x:
              self.rect.x -= 2
              if self.rect.x < 0:
                self.rect.x = 0
                self.image = r_enm3_image
              else:
                self.image = l_enm3_image
            if the_player.rect.x < self.rect.x:
              self.rect.x += 2
              if self.rect.x > dis_width - 30:
                self.rect.x = dis_width - 30
                self.image = l_enm3_image
              else:
                self.image = r_enm3_image
            

        class Enemy4(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = f_enm4_image
            self.rect = self.image.get_rect()
          def tracker (self, the_player, cycle):
            if the_player.rect.y > self.rect.y:
              self.rect.y += 4
              if cycle <= 7 and cycle > 0:
                self.image = f_enm4_image2
              elif cycle <= 14 and cycle > 7:
                self.image = f_enm4_image3
              else:
                self.image = f_enm4_image
            if the_player.rect.y < self.rect.y:
              self.rect.y -= 4
              if cycle <= 7 and cycle > 0:
                self.image = b_enm4_image2
              elif cycle <= 14 and cycle > 7:
                self.image = b_enm4_image3
              else:
                self.image = b_enm4_image
            if the_player.rect.x > self.rect.x:
              self.rect.x += 4
              if cycle <= 7 and cycle > 0:
                self.image = r_enm4_image2
              elif cycle <= 14 and cycle > 7:
                self.image = r_enm4_image3
              else:
                self.image = r_enm4_image
            if the_player.rect.x < self.rect.x:
              self.rect.x -= 4
              if cycle <= 7 and cycle > 0:
                self.image = l_enm4_image2
              elif cycle <= 14 and cycle > 7:
                self.image = l_enm4_image3
              else:
                self.image = l_enm4_image

          
        
        class HealthPotion(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = health_potion_image
            self.rect = self.image.get_rect()


        class ProjectileBox(pygame.sprite.Sprite):
          def __init__(self):
            super().__init__()
            self.image = projectile_box_image
            self.rect = self.image.get_rect()
        
        # CREATING SPRITES

        player = Player()
        player.rect.x = dis_width/2
        player.rect.y = 400
        
        health_potion = HealthPotion()
        health_potion.rect.x = random.randint(20, dis_width-20)
        health_potion.rect.y = random.randint(70, dis_height - 20)

        projectile_box = ProjectileBox()
        projectile_box.rect.x = random.randint(20, dis_width-20)
        projectile_box.rect.y = random.randint(70, dis_height - 20)
        
        enm1_1 = Enemy1()
        enm1_1.rect.x = random.choice([-40, dis_width+40])
        enm1_1.rect.y = random.randint(0, dis_height)
        
        enm1_2 = Enemy1()
        enm1_2.rect.x = random.choice([-40, dis_width+40])
        enm1_2.rect.y = random.randint(0, dis_height)
        
        enm2_2 = Enemy2()
        enm2_2.rect.x = random.choice([-40, dis_width+40])
        enm2_2.rect.y = random.randint(0, dis_height)
        
        enm3_1 = Enemy3()
        enm3_1.rect.x = random.choice([-40, dis_width+40])
        enm3_1.rect.y = random.randint(0, dis_height)
        
        senm = SpawnedEnemy()
        senm.rect.x = enm3_1.rect.x
        senm.rect.y = enm3_1.rect.y
        
        enm4_1 = Enemy4()
        enm4_1.rect.x = random.choice([-40, dis_width+40])
        enm4_1.rect.y = random.randint(0, dis_height)

        while running:

          # MESSAGES AND MESSAGE FUNCTION

          all_sprites = pygame.sprite.Group()
          lose_mesg = font1.render('You Lose', True, black)
          score_mesg = font2.render(f'Your Score Was: {score}', True, black)
          credit_mesg = font3.render('Image Credit: photo created by bearfotos - www.freepik.com', True, black)
          credit_mesg2 = font4.render('Photo by Ferdinand Stöhr on Unsplash, and Photo by David Monje on Unsplash', True, black)
          message3 = font2.render(f'Previous Score: {previous_score}', 1, white)
          current_score_mesg = font2.render(f'Score: {score}', True, yellow)
          current_projectile_mesg = font2.render(f'{projectile_box_count}', True, yellow)
          def lose_message():
            lose_backround_x = 0
            losing = 0
            while losing < 300:
              dis.blit(lose_bg, [lose_backround_x, 0])
              dis.blit(lose_mesg, [200, 200])
              dis.blit(score_mesg, [500, 400])
              dis.blit(credit_mesg, [200, 500])
              dis.blit(credit_mesg2, [220, 550])
              lose_backround_x -= 1/3
              losing += 1
              pygame.display.flip()
          
          # ADD SPRITES

          all_sprites.add(player)
          all_sprites.add(health_potion)
          all_sprites.add(projectile_box)
          all_sprites.add(enm1_1)
          all_sprites.add(enm1_2)
          all_sprites.add(enm2_2)
          all_sprites.add(enm3_1)
          all_sprites.add(enm4_1)

          # EVENTS

          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and shot_cooldown > 60:
              shooting = True
              projectile = Projectile()
              projectile.rect.x = player.rect.x + 5
              projectile.rect.y = player.rect.y + 15
              all_sprites.add(projectile)
              shot_cooldown = 0
          keys = pygame.key.get_pressed()
          if keys[pygame.K_w]:
              player.moveUp(3)
              facing_direction = 'u'
          if keys[pygame.K_s]:
              player.moveDown(3)
              facing_direction = 'd'
          if keys[pygame.K_a]:
              player.moveLeft(3)
              facing_direction = 'l'
          if keys[pygame.K_d]:
              player.moveRight(3)
              facing_direction = 'r'
          if keys[pygame.K_SPACE] and projectile_box_count > 0 and shot_cooldown2 > 60:
            shooting2 = True
            projectile2 = Projectile2()
            projectile2.rect.x = player.rect.x + 5
            projectile2.rect.y = player.rect.y + 15
            all_sprites.add(projectile2)
            projectile_box_count -= 1
            shot_cooldown2 = 0
          
            
          
          # FOLLOW FUNCTIONS, WALK CYCLES, AND HEALTH MANAGEMENT

          if walk_cycle > 20:
            walk_cycle = 1
          if walk_cycle2 > 20:
            walk_cycle2 = 1
          if walk_cycle3 > 14:
            walk_cycle3 = 1
          if walk_cycle4 > 14:
            walk_cycle4 = 1

          if spawn_cooldown > 60:
            enm1_1.tracker(player, walk_cycle2)
            if enm1_1.rect.colliderect(player):
              health_remaining -= 3
          if score > 180 and spawn_cooldown2 > 60:
            enm1_2.tracker(player, walk_cycle2)
            if enm1_2.rect.colliderect(player):
              health_remaining -= 3
          if score > 600 and spawn_cooldown3 > 180:
            enm2_2.tracker(player, walk_cycle3)
            if enm2_2.rect.colliderect(player):
              health_remaining -= 3
          if score > 1200 and spawn_cooldown4 > 180:
            enm3_1.tracker(player)
            if enm3_1.rect.colliderect(player):
              health_remaining -= 1
            spawned = True
          if spawned and spawn_cooldown5 > 60:
            senm.tracker(player, walk_cycle)
            all_sprites.add(senm)
            if senm.rect.colliderect(player):
              health_remaining -= 1
          if score > 1800 and spawn_cooldown6 > 180:
            enm4_1.tracker(player, walk_cycle4)
            if enm4_1.rect.colliderect(player):
              health_remaining -= 3
          if health_remaining < 0:
            lose_message()
            running = False
          if health_potion.rect.colliderect(player):
            health_remaining += 50
            health_potion.rect.x = random.randint(30, dis_width-30)
            health_potion.rect.y = random.randint(90, dis_height - 40)
          if health_remaining > 450:
            health_remaining = 450

          if projectile_box.rect.colliderect(player):
            projectile_box_count += 1
            projectile_box.rect.x = random.randint(30, dis_width-30)
            projectile_box.rect.y = random.randint(90, dis_height - 40)

          # PROJECTILE FIRING

          if shooting and shot_cooldown < 60:
            if facing_direction == 'r':
              projectile.shoot_right(5)
            if facing_direction == 'l':
              projectile.shoot_left(5)
            if facing_direction == 'u':
              projectile.shoot_up(5)
            if facing_direction == 'd':
              projectile.shoot_down(5)
            all_sprites.add(projectile)
            all_sprites.update()

            # CHECK COLLISIONS BETWEEN PROJECTILE AND ENEMIES

            if enm1_1.rect.colliderect(projectile):
              enm1_1.kill()
              enm1_1 = Enemy1()
              enm1_1.rect.x = random.randint(0, dis_width)
              enm1_1.rect.y = random.choice([-40, dis_height+40])
              all_sprites.add(enm1_1)
              spawn_cooldown = 0
            if enm1_2.rect.colliderect(projectile):
              enm1_2.kill()
              enm1_2 = Enemy1()
              enm1_2.rect.x = random.randint(0, dis_width)
              enm1_2.rect.y = random.choice([-40, dis_height+40])
              spawn_cooldown2 = 0
            if enm2_2.rect.colliderect(projectile):
              hit_count += 1
              if hit_count > 3:
                enm2_2.kill()
                enm2_2 = Enemy2()
                enm2_2.rect.x = random.choice([-40, dis_width+40])
                enm2_2.rect.y = random.randint(0, dis_height)
                all_sprites.add(enm2_2)
                hit_count = 0
                spawn_cooldown3 = 0
              elif hit_count < 3:
                shot_cooldown = 61
                projectile.kill()
            if spawned:
              if senm.rect.colliderect(projectile):
                senm = SpawnedEnemy()
                senm.rect.x = enm3_1.rect.x
                senm.rect.y = enm3_1.rect.y
                spawn_cooldown5 = 0
            if enm3_1.rect.colliderect(projectile):
              enm3_1.kill()
              enm3_1 = Enemy3()
              enm3_1.rect.x = random.choice([-40, dis_width+40])
              enm3_1.rect.y = random.randint(0, dis_height)
              senm.rect.x = enm3_1.rect.x
              senm.rect.y = enm3_1.rect.y
              spawn_cooldown4 = 0
              spawned = False
            if enm4_1.rect.colliderect(projectile):
              hit_count2 += 1
              if hit_count2 > 9:
                enm4_1.kill()
                enm4_1 = Enemy4()
                enm4_1.rect.x = random.choice([-40, dis_width+40])
                enm4_1.rect.y = random.randint(0, dis_height)
                all_sprites.add(enm4_1)
                hit_count2 = 0
                spawn_cooldown6 = 0
              elif hit_count2 < 9:
                shot_cooldown = 61
                projectile.kill()
          
          if shooting2 and shot_cooldown2 < 60:
            if facing_direction == 'r':
              projectile2.shoot_right(5)
            if facing_direction == 'l':
              projectile2.shoot_left(5)
            if facing_direction == 'u':
              projectile2.shoot_up(5)
            if facing_direction == 'd':
              projectile2.shoot_down(5)
            all_sprites.add(projectile2)
            all_sprites.update()

            # CHECK COLLISIONS BETWEEN PROJECTILE AND ENEMIES

            if enm1_1.rect.colliderect(projectile2):
              enm1_1.kill()
              enm1_1 = Enemy1()
              enm1_1.rect.x = random.randint(0, dis_width)
              enm1_1.rect.y = random.choice([-40, dis_height+40])
              all_sprites.add(enm1_1)
              spawn_cooldown = 0
            if enm1_2.rect.colliderect(projectile2):
              enm1_2.kill()
              enm1_2 = Enemy1()
              enm1_2.rect.x = random.randint(0, dis_width)
              enm1_2.rect.y = random.choice([-40, dis_height+40])
              spawn_cooldown2 = 0
            if enm2_2.rect.colliderect(projectile2):
              hit_count += 10
              if hit_count > 3:
                enm2_2.kill()
                enm2_2 = Enemy2()
                enm2_2.rect.x = random.choice([-40, dis_width+40])
                enm2_2.rect.y = random.randint(0, dis_height)
                all_sprites.add(enm2_2)
                hit_count = 0
                spawn_cooldown3 = 0
              elif hit_count < 3:
                shot_cooldown2 = 61
                projectile.kill()
            if spawned:
              if senm.rect.colliderect(projectile2):
                senm = SpawnedEnemy()
                senm.rect.x = enm3_1.rect.x
                senm.rect.y = enm3_1.rect.y
                spawn_cooldown5 = 0
            if enm3_1.rect.colliderect(projectile2):
              enm3_1.kill()
              enm3_1 = Enemy3()
              enm3_1.rect.x = random.choice([-40, dis_width+40])
              enm3_1.rect.y = random.randint(0, dis_height)
              senm.rect.x = enm3_1.rect.x
              senm.rect.y = enm3_1.rect.y
              spawn_cooldown4 = 0
              spawned = False
            if enm4_1.rect.colliderect(projectile2):
              hit_count2 += 10
              if hit_count2 > 9:
                enm4_1.kill()
                enm4_1 = Enemy4()
                enm4_1.rect.x = random.choice([-40, dis_width+40])
                enm4_1.rect.y = random.randint(0, dis_height)
                all_sprites.add(enm4_1)
                hit_count2 = 0
                spawn_cooldown6 = 0
              elif hit_count2 < 9:
                shot_cooldown2 = 61
                projectile.kill()

          # JUMPING

          # if jump_cooldown < 12:
          #   player.jump_up(5)
          # if jump_cooldown < 25 and jump_cooldown > 12:
          #   player.jump_down(5)
          
          # CREATE THE SCENE

          all_sprites.update()
          all_sprites.draw(dis)
          dis.fill(black)
          # for row in range(mapheight):
          #   for column in range(mapwidth):
          #       dis.blit(textures[tilemap[row][column]], (column*tilesize, row*tilesize))
          dis.blit(heart_image, [10, 10])
          dis.blit(projectile_box_image, [550, 8])
          pygame.draw.rect(dis, red, [50, 15, health_remaining, 20])
          pygame.draw.line(dis, red, [0, 50], [dis_width, 50], 3)
          dis.blit(current_score_mesg, [700, 10])
          dis.blit(current_projectile_mesg, [600, 10])
          dis.blit(message2, (1000, 10))
          # dis.blit(bg2, [backround_x, 0])
          # dis.blit(bg, [backround_x, 0])
          all_sprites.draw(dis)
          pygame.display.flip()

          # ADD TO TIMERS AND UPDATE

          # jump_cooldown += 1
          shot_cooldown += 1
          shot_cooldown2 += 1
          spawn_cooldown += 1
          spawn_cooldown2 += 1
          spawn_cooldown3 += 1
          spawn_cooldown4 += 1
          spawn_cooldown5 += 1
          spawn_cooldown6 += 1
          score += 1
          walk_cycle += 1
          walk_cycle2 += 1
          walk_cycle3 += 1
          walk_cycle4 += 1
          if score > highscore:
            highscore = score
          previous_score = score
          clock.tick(60)

      # CREATES THE START SCREEN
  pygame.display.flip()
        

pygame.quit()
    