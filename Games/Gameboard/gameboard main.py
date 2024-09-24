import pygame
import random
import math

pygame.init()

background_block = pygame.image.load('backround_piece.png')
wall_block = pygame.image.load('wall_piece.png')
player_img = pygame.image.load('player_piece.png')
enemy_1_img = pygame.image.load('enemy_1_piece.png')
objective_block = pygame.image.load('objective_piece.png')
player_img_o = pygame.image.load('player_piece_objective.png')
enemy_1_img_o = pygame.image.load('enemy_1_piece_objective.png')

# AVAILABLE COLORS

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)

# NEEDED STUFF

dis_width = 800
dis_height = 660
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Test Game')
font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)


Things = {0: background_block,
         1: wall_block,
         2: player_img,
         3: enemy_1_img,
         4: objective_block,
         5: player_img_o,
         6: enemy_1_img_o}


Gameboard = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

 ]
playing = True
player_in_obj = False
enemy_in_obj = False
player_score = 0
enemy_score = 0
obj_count = 0


def generate_board():
   global Gameboard
   global obj_count
   global player_score
   global enemy_score

   Gameboard = [
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

   ]

   obj_count = 0
   wall_count = 0
   player_score = 0
   enemy_score = 0
   placing_objectives = True
   while placing_objectives:
       rv = -1
       for r in Gameboard:
           rv += 1
           cv = -1
           for c in r:
               cv += 1
               if c == 0:
                   t = random.randint(1, 3)
                   if t == 1 and wall_count < 40:
                       Gameboard[rv][cv] = 1
                       wall_count += 1
                   o = random.randint(1, 64)
                   if o == 1 and 1 < rv < 8 and 1 < cv < 8 and obj_count < 5:
                       Gameboard[rv][cv] = 4
                       obj_count += 1
                   if obj_count > 4:
                       placing_objectives = False


def update_board():
   global obj_count
   obj_count = 0
   b_y = -30
   message1 = font2.render(str(player_score), False, white)
   message2 = font2.render(str(enemy_score), False, red)
   dis.blit(message1, (670, 20))
   dis.blit(message2, (730, 20))
   for r in Gameboard:
       b_y += 60
       b_x = -30
       for c in r:
           b_x += 60
           dis.blit(Things[c], (b_x, b_y))
           if c == 4 or c == 5 or c == 6:
               obj_count += 1


def move_up(t, t2):
   global player_in_obj
   global enemy_in_obj
   global player_score
   global enemy_score
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       if 0 < rv:
           for c in r:
               cv += 1
               if c == t:
                   if Gameboard[rv-1][cv] == 0:
                       Gameboard[rv - 1][cv] = t
                       Gameboard[rv][cv] = 0
                   if Gameboard[rv - 1][cv] == 4:
                       Gameboard[rv - 1][cv] = t2
                       Gameboard[rv][cv] = 0
                       if t == 2:
                           player_in_obj = True
                           player_score += 1
                       if t == 3:
                           enemy_in_obj = True
                           enemy_score += 1


def move_down(t, t2):
   global player_in_obj
   global enemy_in_obj
   global player_score
   global enemy_score
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       if rv < 9:
           for c in r:
               cv += 1
               if c == t:
                   if Gameboard[rv+1][cv] == 0:
                       Gameboard[rv + 1][cv] = t
                       Gameboard[rv][cv] = 0
                       rv = 8
                   if Gameboard[rv + 1][cv] == 4:
                       Gameboard[rv + 1][cv] = t2
                       Gameboard[rv][cv] = 0
                       if t == 2:
                           player_in_obj = True
                           player_score += 1
                       if t == 3:
                           enemy_in_obj = True
                           enemy_score += 1
                       rv = 8


def move_right(t, t2):
   global player_in_obj
   global enemy_in_obj
   global player_score
   global enemy_score
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       for c in r:
           cv += 1
           if c == t and cv < 9:
               if Gameboard[rv][cv+1] == 0:
                   Gameboard[rv][cv+1] = t
                   Gameboard[rv][cv] = 0
                   cv = 8
               if Gameboard[rv][cv+1] == 4:
                   Gameboard[rv][cv+1] = t2
                   Gameboard[rv][cv] = 0
                   if t == 2:
                       player_in_obj = True
                       player_score += 1
                   if t == 3:
                       enemy_in_obj = True
                       enemy_score += 1
                   cv = 8


def move_left(t, t2):
   global player_in_obj
   global enemy_in_obj
   global player_score
   global enemy_score
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       for c in r:
           cv += 1
           if c == t and 0 < cv:
               if Gameboard[rv][cv-1] == 0:
                   Gameboard[rv][cv-1] = t
                   Gameboard[rv][cv] = 0
               if Gameboard[rv][cv-1] == 4:
                   Gameboard[rv][cv-1] = t2
                   Gameboard[rv][cv] = 0
                   if t == 2:
                       player_in_obj = True
                       player_score += 1
                   if t == 3:
                       enemy_in_obj = True
                       enemy_score += 1


def break_wall(d, t):
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       for c in r:
           cv += 1
           if c == t and 0 < rv:
               if d == 1 and Gameboard[rv-1][cv] == 1:
                   Gameboard[rv - 1][cv] = 0
           if c == t and rv < 9:
               if d == 3 and Gameboard[rv+1][cv] == 1:
                   Gameboard[rv + 1][cv] = 0
           if c == t and cv < 9:
               if d == 2 and Gameboard[rv][cv+1] == 1:
                   Gameboard[rv][cv+1] = 0
           if c == t and 0 < cv:
               if d == 4 and Gameboard[rv][cv-1] == 1:
                   Gameboard[rv][cv-1] = 0


def reset_piece(first, second):
   global player_in_obj
   rv = -1
   for r in Gameboard:
       rv += 1
       cv = -1
       for c in r:
           cv += 1
           if c == first:
               Gameboard[rv][cv] = second
   player_in_obj = False


def place_obj():
   global obj_count
   placing_obj = True
   while placing_obj:
       rv = -1
       for r in Gameboard:
           rv += 1
           cv = -1
           for c in r:
               cv += 1
               if c == 0:
                   ob = random.randint(1, 64)
                   if ob == 1 and 1 < rv < 8 and 1 < cv < 8:
                       Gameboard[rv][cv] = 4
                       obj_count += 1
                       placing_obj = False
                       break


def remove_a_obj():
   iteration_count = 0
   removing_obj = True
   while removing_obj:
       iteration_count += 1
       rv = -1
       for r in Gameboard:
           rv += 1
           cv = -1
           for c in r:
               cv += 1
               if c == 4:
                   de = random.randint(1, 5)
                   if de == 1:
                       Gameboard[rv][cv] = 0
                       removing_obj = False
                       break
       if iteration_count > 3:
           removing_obj = False


class ObjChoice(pygame.sprite.Sprite):
   def __init__(self, color, width, height, x, y):
       super().__init__()
       self.image = pygame.Surface([width, height])
       self.image.fill(white)
       pygame.draw.rect(self.image, color, [0, 0, width, height])
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y


all_sprites = pygame.sprite.Group()

add_obj = ObjChoice(green, 50, 50, 680, 100)
keep_obj = ObjChoice(white, 50, 50, 680, 200)
remove_obj = ObjChoice(red, 50, 50, 680, 300)


def enemy_move():
   global Gameboard
   global enemy_in_obj
   global enemy_score
   global player_score
   rv = -1
   enemy_r = 0
   enemy_c = 0
   player_r = 0
   player_c = 0

   enemy_moving = True
   obj_pos_list = []
   for r in Gameboard:
       rv += 1
       cv = -1
       for c in r:
           cv += 1
           if c == 3 or c == 6:
               enemy_r = rv
               enemy_c = cv
           if c == 2 or c == 5:
               player_r = rv
               player_c = cv
           if c == 4:
               obj_r = rv
               obj_c = cv
               obj_pos_list.append(obj_r)
               obj_pos_list.append(obj_c)
   # print(obj_pos_list)
   # print(obj_r, obj_c)
   checker = 0

   current_distance_enm = 100
   current_distance_player = 100
   x = 0

   lowest_x_enm = 0
   lowest_y_enm = 0
   for n in obj_pos_list:
       checker += 1
       if checker == 1:
           x = n
       if checker == 2:
           y = n
           lowest_distance_enm = math.dist([enemy_r, enemy_c], [x, y])
           lowest_distance_player = math.dist([player_r, player_c], [x, y])
           if lowest_distance_enm < current_distance_enm:
               current_distance_enm = lowest_distance_enm
               lowest_x_enm = x
               lowest_y_enm = y
           if lowest_distance_player < current_distance_enm:
               current_distance_player = lowest_distance_player
               # lowest_x_player = x
               # lowest_y_player = y

           x = 0
           checker = 0
   while enemy_moving:
       if enemy_in_obj:
           if enemy_score < player_score:
               place_obj()
               enemy_in_obj = False
               break
           elif current_distance_player < current_distance_enm and enemy_score > player_score:
               remove_a_obj()
               enemy_in_obj = False
               break
           elif current_distance_player < current_distance_enm and enemy_score == player_score:
               place_obj()
               enemy_in_obj = False
               break
           else:
               enemy_in_obj = False

       if 0 < enemy_r:
           if enemy_r > lowest_x_enm and Gameboard[enemy_r-1][enemy_c] == 1:
               break_wall(1, 3)
               break
           if enemy_r > lowest_x_enm and enemy_moving:
               move_up(3, 6)
               break
       if enemy_r < 9 and enemy_moving:
           if enemy_r < lowest_x_enm and Gameboard[enemy_r + 1][enemy_c] == 1:
               break_wall(3, 3)
               break
           if enemy_r < lowest_x_enm and enemy_moving:
               move_down(3, 6)
               break
       if enemy_c < 9 and enemy_moving:
           if enemy_c < lowest_y_enm and Gameboard[enemy_r][enemy_c+1] == 1:
               break_wall(2, 3)
               break
           if enemy_c < lowest_y_enm and enemy_moving:
               move_right(3, 6)
               break
       if 0 < enemy_c and enemy_moving:
           if enemy_c > lowest_y_enm and Gameboard[enemy_r][enemy_c-1] == 1:
               break_wall(4, 3)
               break
           if enemy_c > lowest_y_enm and enemy_moving:
               move_left(3, 6)
               break

       enemy_moving = False


generate_board()
player_move = True


while playing:
   dis.fill(black)

   all_sprites = pygame.sprite.Group()

   all_sprites.add(add_obj)
   all_sprites.add(keep_obj)
   all_sprites.add(remove_obj)

   in_obj = False
   if player_in_obj:
       all_sprites.update()
       all_sprites.draw(dis)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           playing = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_ESCAPE:
               playing = False
       if event.type == pygame.MOUSEBUTTONDOWN and player_in_obj:
           pos = pygame.mouse.get_pos()
           # posx = pos[0]
           # posy = pos[1]
           clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
           for i in clicked_sprites:
               if i == add_obj:
                   place_obj()
                   in_obj = False
               if i == remove_obj:
                   remove_a_obj()
           reset_piece(5, 2)
           player_move = False
   keys = pygame.key.get_pressed()
   # if player_in_obj:
   if keys[pygame.K_SPACE] and obj_count == 0:
       generate_board()
       update_board()
   if keys[pygame.K_w] and player_move:
       if not player_in_obj:
           move_up(2, 5)
       elif player_in_obj:
           reset_piece(5, 2)
           move_up(2, 5)
       player_move = False
   if keys[pygame.K_s] and player_move:
       if not player_in_obj:
           move_down(2, 5)
       elif player_in_obj:
           reset_piece(5, 2)
           move_down(2, 5)
       player_move = False
   if keys[pygame.K_d] and player_move:
       if not player_in_obj:
           move_right(2, 5)
       elif player_in_obj:
           reset_piece(5, 2)
           move_right(2, 5)
       player_move = False

   if keys[pygame.K_a] and player_move:
       if not player_in_obj:
           move_left(2, 5)
       elif player_in_obj:
           reset_piece(5, 2)
           move_left(2, 5)
       player_move = False

   if keys[pygame.K_1] and player_move:
       if not player_in_obj:
           break_wall(1, 2)
       elif player_in_obj:
           break_wall(1, 5)
       player_move = False
   if keys[pygame.K_2] and player_move:
       if not player_in_obj:
           break_wall(2, 2)
       elif player_in_obj:
           break_wall(2, 5)
       player_move = False
   if keys[pygame.K_3] and player_move:
       if not player_in_obj:
           break_wall(3, 2)
       elif player_in_obj:
           break_wall(3, 5)
       player_move = False
   if keys[pygame.K_4] and player_move:
       if not player_in_obj:
           break_wall(4, 2)
       elif player_in_obj:
           break_wall(4, 5)
       player_move = False
   if not player_move:
       if not enemy_in_obj:
           enemy_move()
       if enemy_in_obj:
           r_v = -1
           for r_ in Gameboard:
               r_v += 1
               c_v = -1
               for c_ in r_:
                   c_v += 1
                   if Gameboard[r_v][c_v] == 6:
                       Gameboard[r_v][c_v] = 3
           enemy_move()
       player_move = True
   end_color = white
   if enemy_score < player_score:
       end_color = green
   if enemy_score > player_score:
       end_color = red
   end_message = font2.render(f'The Score was {player_score} : {enemy_score}', False, end_color)
   update_board()
   if obj_count == 0:
       dis.fill(black)
       dis.blit(end_message, (150, dis_height/2))
   pygame.display.flip()
   clock.tick(10)
pygame.quit()
