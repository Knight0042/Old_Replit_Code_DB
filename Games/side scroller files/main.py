import pygame
import spritesheet
import random

#Photo by Chris Barbalis on Unsplash

pygame.init()

ss = spritesheet.spritesheet('player.png')
# Sprite is 16x16 pixels at location 0,0 in the file...
# 
run_images = []
walk_images = []
die_images = []
jump_images = []
#97x227
def load_animation(animation_list, num, x, y):
  image_size = 64
  if x == 0:
    correction = 0
  else:
    correction = 1
  if y == 0:
    correction2 = 0
  else:
    correction2 = 1
  for i in range(0, num):

    image = ss.image_at(((x+i)*image_size+correction, (y)*image_size+correction2, image_size, image_size), colorkey=(0, 0, 0) )
    animation_list.append(image)
# images = ss.images_at((0, 0, image_size, image_size),(image_size+1, 0, image_size,image_size))
# # colorkey=(255, 255, 255) 

load_animation(run_images, 4, 4, 0)
load_animation(run_images, 4, 0, 1)
load_animation(walk_images, 8, 0, 4)
load_animation(die_images, 8, 0, 2)
load_animation(jump_images, 8, 0, 5)


# print(run_images)
# for image in run_images:
#   image

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
bg_width = 1600
bg_height = 800
walkway_width = 345
walkway_height = 345
obstacle_width = 32
obstacle_height = 75
#96 468
obstacle_width2 = 32
obstacle_height2 = 329

bg = pygame.image.load('3163.png')
bg = pygame.transform.scale(bg, (bg_width, bg_height))
walkway = pygame.image.load('walkway.jpg')
walkway = pygame.transform.scale(walkway, (walkway_width, walkway_height))
obstacle_img = pygame.image.load('obstacle.png')
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))
obstacle_img2 = pygame.image.load('obstacle2.png')
obstacle_img2 = pygame.transform.scale(obstacle_img2, (obstacle_width2, obstacle_height2))
player_slide_image = pygame.image.load('player_slide.png')
clock = pygame.time.Clock()
dis =  pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('2d Sidescroller Game')
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)

score = 0
movement_cycle = 0
jump_cycle = 0

highscore = 0
previous_score = 0
initiate = True


class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = (walk_images[0])
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
  def change(self, image_list, frame):
    self.image = (image_list[frame])


class Obstacle(pygame.sprite.Sprite):
  def __init__(self, x, y, v):
    super().__init__()
    if v == 1:
      self.image = obstacle_img
    elif v == 2:
      self.image = obstacle_img2
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

# (dis_width/2-32), (dis_height/2-32)

walk_frame = 0
bg1_pos_x = 0
bg1_pos_y = -300
bg2_pos_x = bg_width
bg2_pos_y = -300

walkway1_pos_y = dis_height/2+32
walkway1_pos_x = 0
walkway2_pos_x = walkway_width
walkway3_pos_x = 2*walkway_width
walkway4_pos_x = 3*walkway_width
walkway5_pos_x = 4*walkway_width
# walkway6_pos_x = 5*walkway_width
player = Player((dis_width/2), (dis_height/2))
while initiate:
  # player = Player((dis_width/2-32), (dis_height/2-32))
  all_sprites = pygame.sprite.Group()
  obstacles = pygame.sprite.Group()
  all_sprites.add(player)
  player.rect.centerx = (dis_width/2)
  player.rect.centery = (dis_height/2)
  showcasing = True
  gameover = False
  reverse = False
  # dis.fill(white)
  message1 = font5.render('Press P to Start', 1, white)
  message2 = font2.render(f'Highscore: {highscore}', 1, white)
  message3 = font2.render(f'Previous Score: {previous_score}', 1, white)
  dis.blit(bg, (int(bg1_pos_x), int(bg1_pos_y)))
  dis.blit(bg, (int(bg2_pos_x), int(bg2_pos_y)))
  # pygame.draw.rect(dis, black, [0, dis_height/2+32, dis_width, dis_height/2])
  dis.blit(walkway, (int(walkway1_pos_x), int(walkway1_pos_y)))
  dis.blit(walkway, (int(walkway2_pos_x), int(walkway1_pos_y)))
  dis.blit(walkway, (int(walkway3_pos_x), int(walkway1_pos_y)))
  dis.blit(walkway, (int(walkway4_pos_x), int(walkway1_pos_y)))
  dis.blit(walkway, (int(walkway5_pos_x), int(walkway1_pos_y)))
  dis.blit(message1, (130, dis_height/2+37))
  dis.blit(message2, (150, dis_height/2-200))
  dis.blit(message3, (850, dis_height/2-200))
  walk_frame += 1/6
  if walk_frame > 15/2:
    walk_frame = 0
  player.change(walk_images, int(walk_frame))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      initiate = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        initiate = False
      if event.key == pygame.K_a:
        while showcasing:
          dis.fill(white)
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              showcasing = False
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                showcasing = False
          if movement_cycle > 200:
            movement_cycle = -5
          if movement_cycle < 26:
            dis.blit(run_images[0], (0, dis_height/2+32))
            dis.blit(walk_images[0], (100, dis_height/2+32))
            dis.blit(die_images[0], (200, dis_height/2+32))
          if movement_cycle > 25 and movement_cycle < 51:
            dis.blit(run_images[1], (0, dis_height/2+32))
            dis.blit(walk_images[1], (100, dis_height/2+32))
            dis.blit(die_images[1], (200, dis_height/2+32))
          if movement_cycle > 50 and movement_cycle < 76:
            dis.blit(run_images[2], (0, dis_height/2+32))
            dis.blit(walk_images[2], (100, dis_height/2+32))
            dis.blit(die_images[2], (200, dis_height/2+32))
          if movement_cycle > 75 and movement_cycle < 101:
            dis.blit(run_images[3], (0, dis_height/2+32))
            dis.blit(walk_images[3], (100, dis_height/2+32))
            dis.blit(die_images[3], (200, dis_height/2+32))
          if movement_cycle > 100 and movement_cycle < 126:
            dis.blit(run_images[4], (0, dis_height/2+32))
            dis.blit(walk_images[4], (100, dis_height/2+32))
            dis.blit(die_images[4], (200, dis_height/2+32))
          if movement_cycle > 125 and movement_cycle < 151:
            dis.blit(run_images[5], (0, dis_height/2+32))
            dis.blit(walk_images[5], (100, dis_height/2+32))
            dis.blit(die_images[5], (200, dis_height/2+32))
          if movement_cycle > 150 and movement_cycle < 176:
            dis.blit(run_images[6], (0, dis_height/2+32))
            dis.blit(walk_images[6], (100, dis_height/2+32))
            dis.blit(die_images[6], (200, dis_height/2+32))
          if movement_cycle > 175 and movement_cycle < 201:
            dis.blit(run_images[7], (0, dis_height/2+32))
            dis.blit(walk_images[7], (100, dis_height/2+32))
            dis.blit(die_images[7], (200, dis_height/2+32))
          if jump_cycle > 160:
            reverse = True
          if reverse:
            jump_cycle -= 10
          if jump_cycle < 0:
            reverse = False
            jump_cycle = 0
          if jump_cycle < 21:
            dis.blit(jump_images[0], (300, dis_height/2+32))
          if jump_cycle > 20 and jump_cycle < 41:
            dis.blit(jump_images[1], (300, dis_height/2+32))
          if jump_cycle > 40 and jump_cycle < 61:
            dis.blit(jump_images[2], (300, dis_height/2+32))
          if jump_cycle > 60 and jump_cycle < 81:
            dis.blit(jump_images[3], (300, dis_height/2+32))
          if jump_cycle > 80 and jump_cycle < 101:
            dis.blit(jump_images[4], (300, dis_height/2+32))
          if jump_cycle > 100 and jump_cycle < 121:
            dis.blit(jump_images[5], (300, dis_height/2+32))
          if jump_cycle > 120 and jump_cycle < 141:
            dis.blit(jump_images[6], (300, dis_height/2+32))
          if jump_cycle > 140 and jump_cycle < 161:
            dis.blit(jump_images[7], (300, dis_height/2+32))
          dis.blit(obstacle_img, (400, dis_height/2+obstacle_height/2))
          movement_cycle += 5
          jump_cycle += 5
          pygame.display.flip()
          clock.tick(60)
      if event.key == pygame.K_p:
        obstacle_timer = 0
        roll_frame = 0
        # Main Game
        run_frame = 0
        jump_frame = 0
        jump_stall = 0
        roll_stall = 0
        jump_up = False
        roll_down = False
        jump = False
        stalling = False
        stalling2 = False
        roll = False
        score = 0
        while not gameover:
          run_frame += 1/4
          if run_frame > 30/4:
            run_frame = 0
          player.change(run_images, int(run_frame))
          dis.blit(bg, (int(bg1_pos_x), int(bg1_pos_y)))
          dis.blit(bg, (int(bg2_pos_x), int(bg2_pos_y)))
          # pygame.draw.rect(dis, black, [0, dis_height/2+32, dis_width, dis_height/2])
          dis.blit(walkway, (int(walkway1_pos_x), int(walkway1_pos_y)))
          dis.blit(walkway, (int(walkway2_pos_x), int(walkway1_pos_y)))
          dis.blit(walkway, (int(walkway3_pos_x), int(walkway1_pos_y)))
          dis.blit(walkway, (int(walkway4_pos_x), int(walkway1_pos_y)))
          dis.blit(walkway, (int(walkway5_pos_x), int(walkway1_pos_y)))
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              gameover = True
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                gameover = True
              if event.key == pygame.K_w and not jump:
                jump_frame = 0
                jump_up = True
                jump = True
              if event.key == pygame.K_s and not roll:
                # player.rect.centery += 10
                roll_frame = 0
                roll_down = True
                roll = True
          if obstacle_timer > random.randrange(120, 1000):
            v = random.choice([1, 2])
            if v == 1:
              obstacles.add(Obstacle(dis_width+obstacle_width, (dis_height/2-obstacle_height)+40, 1))
            if v == 2:
              obstacles.add(Obstacle(dis_width+obstacle_width2, 0, 2))
            obstacle_timer = 0
          for obstacle_t in obstacles: 
            if player.rect.colliderect(obstacle_t):
              dying = True
              die_frame = 0
              while dying:
                die_frame += 1/6
                if die_frame > 7:
                  die_frame = 7
                  gameover = True
                  dying = False
                player.change(die_images, int(die_frame))
                all_sprites.update()
                dis.blit(bg, (int(bg1_pos_x), int(bg1_pos_y)))
                dis.blit(bg, (int(bg2_pos_x), int(bg2_pos_y)))
                dis.blit(walkway, (int(walkway1_pos_x), int(walkway1_pos_y)))
                dis.blit(walkway, (int(walkway2_pos_x), int(walkway1_pos_y)))
                dis.blit(walkway, (int(walkway3_pos_x), int(walkway1_pos_y)))
                dis.blit(walkway, (int(walkway4_pos_x), int(walkway1_pos_y)))
                dis.blit(walkway, (int(walkway5_pos_x), int(walkway1_pos_y)))
                all_sprites.draw(dis)
                obstacles.draw(dis)
                pygame.display.flip()
                clock.tick(60)
                
            obstacle_t.rect.x -= 3/2
            if obstacle_t.rect.x < -obstacle_width: # If our obstacle is off the screen we will remove it
                obstacle_t.kill()
          if not stalling:
            if jump_up: 
              jump_frame+=1/3
            if not jump_up: 
              jump_frame-=1/3
            if jump_frame > 7:
              jump_frame = 7
              stalling = True
              jump_up = False
            if jump_frame < 0:
              jumpframe = 0
              # jump = False
            if jump and jump_up:
              player.change(jump_images, int(jump_frame))
              player.rect.centery -= 6
            if jump and not jump_up:
              player.change(jump_images, int(jump_frame))
              player.rect.centery += 6
              if player.rect.centery > dis_height/2:
                player.rect.centery = dis_height/2
                jump = False
          if not stalling2:
            if roll_down: 
              roll_frame+=1/3
            if not roll_down: 
              roll_frame-=1/3
            if roll_frame > 8:
              roll_frame = 7
              stalling2 = True
              roll_down = False
            if roll_frame < 0:
              roll_frame = 0
            if roll and roll_down:
              player.image = player_slide_image
              player.rect.centery += 2
            if roll and not roll_down:
              player.image = player_slide_image
              player.rect.centery -= 2
              if player.rect.centery < dis_height/2:
                player.rect.centery = dis_height/2
                roll = False
          bg1_pos_x -= 3/2
          bg2_pos_x -= 3/2
          walkway1_pos_x -= 3/2
          walkway2_pos_x -= 3/2
          walkway3_pos_x -= 3/2
          walkway4_pos_x -= 3/2
          walkway5_pos_x -= 3/2
          if bg1_pos_x < -bg_width:
            bg1_pos_x = bg_width
          if bg2_pos_x < -bg_width:
            bg2_pos_x = bg_width
          if walkway1_pos_x < -walkway_width:
            walkway1_pos_x = 4*walkway_width
          if walkway2_pos_x < -walkway_width:
            walkway2_pos_x = 4*walkway_width
          if walkway3_pos_x < -walkway_width:
            walkway3_pos_x = 4*walkway_width
          if walkway4_pos_x < -walkway_width:
            walkway4_pos_x = 4*walkway_width
          if walkway5_pos_x < -walkway_width:
            walkway5_pos_x = 4*walkway_width
          if stalling:
            jump_stall += 1
            player.change(jump_images, random.randrange(5,7))
            if jump_stall > 45:
              jump_stall = 0
              stalling = False
          if stalling2:
            roll_stall += 1
            player.image = player_slide_image
            if roll_stall > 45:
              roll_stall = 0
              stalling2 = False
          all_sprites.add(player)
          all_sprites.update()
          all_sprites.draw(dis)
          obstacles.draw(dis)
          previous_score = score
          if score > highscore:
            highscore=score
          pygame.display.flip()
          score += 1
          obstacle_timer += 1
          clock.tick(60)
  # for image in run_images:
  bg1_pos_x -= 1/2
  bg2_pos_x -= 1/2
  walkway1_pos_x -= 1/2
  walkway2_pos_x -= 1/2
  walkway3_pos_x -= 1/2
  walkway4_pos_x -= 1/2
  walkway5_pos_x -= 1/2
  if bg1_pos_x < -bg_width:
    bg1_pos_x = bg_width
  if bg2_pos_x < -bg_width:
    bg2_pos_x = bg_width
  if walkway1_pos_x < -walkway_width:
    walkway1_pos_x = 4*walkway_width
  if walkway2_pos_x < -walkway_width:
    walkway2_pos_x = 4*walkway_width
  if walkway3_pos_x < -walkway_width:
    walkway3_pos_x = 4*walkway_width
  if walkway4_pos_x < -walkway_width:
    walkway4_pos_x = 4*walkway_width
  if walkway5_pos_x < -walkway_width:
    walkway5_pos_x = 4*walkway_width
  all_sprites.draw(dis)
  pygame.display.flip()
  clock.tick(60)
  