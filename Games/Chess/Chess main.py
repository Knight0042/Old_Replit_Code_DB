import pygame
import spritesheet

ss = spritesheet.spritesheet("chess_pieces_transparent.png")
ss2 = spritesheet.spritesheet("end_spritesheet.png")
chess_board_img = pygame.image.load("chess_board.png")
transparent_img = pygame.image.load("transparent_60x60.png")
draw_button_img = pygame.image.load("draw_button_image.png")
forfeit_button_img = pygame.image.load("forfeit_button_image.png")
adjust_button_img = pygame.image.load("adjust_button.png")
pygame.init()
dis_width = 680
dis_height = 680
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)


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
    [1, 5, 2, 3, 4, 2, 5, 1],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [12, 12, 12, 12, 12, 12, 12, 12],
    [7, 11, 8, 9, 10, 8, 11, 7]
]
image_height = 191
image_width = 191
image_height2 = 200
image_width2 = 500

white_move = True
piece_chosen = False

castling = 0
promotion = 0
promoting = False

agreed_draw = False
agreed_draw1 = False
agreed_draw2 = False

adjusting = False

def load_images(image_list, num, x, y, sprite_sheet, img_width, img_height, check, color_key):
    # Crops a spritesheet and adds the cropped image to a list
    if y == 0:
        correction2 = 0
    else:
        correction2 = 45
    for item in range(0, num):
        if 4 > item >= 2:
            correction = 5
        elif item >= 4:
            correction = 15
        else:
            correction = 0
        if check == 0:
            correction = 0
        image = sprite_sheet.image_at(((x + item) * img_width + correction, y * img_height + correction2, img_width,
                                       img_height), colorkey=color_key)
        if check == 1:
            image = pygame.transform.scale(image, (60, 60))
        image_list.append(image)
all_images = []
all_end_images = []
load_images(all_images, 6, 0, 0, ss, image_width, image_height, 1, -1)
load_images(all_images, 6, 0, 1, ss, image_width, image_height, 1, -1)
load_images(all_end_images, 3, 0, 0, ss2, image_width2, image_height2, 0, (1, 1, 1))
playing = True

all_sprites = pygame.sprite.Group()
all_promotion_buttons = pygame.sprite.Group()
all_promotion_buttons2 = pygame.sprite.Group()
all_buttons = pygame.sprite.Group()

class ChessSpace(pygame.sprite.Sprite):
    def __init__(self, x, y, img, pos_in_board, piece_type):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.board_pos = pos_in_board
        self.type = piece_type
        self.been_moved = False
        all_sprites.add(self)
    def change(self, img):
        self.image = img

class PromotionButton(pygame.sprite.Sprite):
    def __init__(self, x, y, img, piece_type, piece):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if piece_type == 1:
            all_promotion_buttons.add(self)
        if piece_type == 2:
            all_promotion_buttons2.add(self)
        self.piece = piece


class GameButton(pygame.sprite.Sprite):
    def __init__(self, x, y, img, button_type):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button_type = button_type
        all_buttons.add(self)


def generate_board():
    row = -1
    for r in Gameboard:
        row += 1
        col = -1
        for c in r:
            col += 1
            if c == 0:
                c_space = ChessSpace(col*60+100, row*60+100, transparent_img, (row, col), c)
            else:
                c_space = ChessSpace(col*60+100, row*60+100, all_images[c-1], (row, col), c)
    row = -1
    for digit in range(4):
        row += 1
        if digit < 3:
            p_button = PromotionButton(250+(row*60), 580, all_images[digit], 2, digit+1)
            p_button2 = PromotionButton(250+(row*60), 25, all_images[digit+6], 1, digit+7)
        elif digit == 3:
            p_button = PromotionButton(250+(row*60), 580, all_images[digit+1], 2, digit+2)
            p_button2 = PromotionButton(250+(row*60), 25, all_images[digit+7], 1, digit+8)

    g_button = GameButton(20, 145, draw_button_img, 1)
    g_button = GameButton(20, 215, forfeit_button_img, 2)
    g_button = GameButton(20, 385, forfeit_button_img, 3)
    g_button = GameButton(20, 455, draw_button_img, 4)
    g_button = GameButton(20, 305, adjust_button_img, 5)



def update_dis():
    global playing
    winner = -1

    dis.fill(dark_blue)
    dis.blit(chess_board_img, [100, 100])
    all_sprites.draw(dis)
    all_buttons.draw(dis)
    black_king = False
    white_king = False
    draw = True
    for grid_row in Gameboard:
        for grid_space in grid_row:
            if grid_space == 10:
                white_king = True
            if grid_space == 4:
                black_king = True
            if grid_space != 0:
                if grid_space != 10 and grid_space != 4:
                    draw = False
    if draw or agreed_draw:
        winner = 0
    if not white_king:
        winner = 2
    if not black_king:
        winner = 1
    if winner > -1:
        dis.blit(all_end_images[winner], [90, 240])
        playing = False
    if agreed_draw1:
        pygame.draw.rect(dis, green, [30, 105, 30, 30])
    if agreed_draw2:
        pygame.draw.rect(dis, green, [30, 515, 30, 30])
    pygame.display.flip()


def check_move(player, piece, pos1, pos2, been_moved):
    global valid_move
    global castling
    global promotion
    if player == 1:
        if piece == 12:
            if pos2[0] == (pos1[0]-1) and pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos2[0] == 0:
                        valid_move = False
                        promotion = 1
            elif pos2[0] == (pos1[0]-2) and pos2[1] == pos1[1] and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]+1][pos2[1]] == 0:
                    valid_move = True
            elif pos2[0] == (pos1[0]-1) and pos2[1] == (pos1[1]-1):
                if 0 < Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos2[0] == 0:
                        valid_move = False
                        promotion = 1
            elif pos2[0] == (pos1[0]-1) and pos2[1] == (pos1[1]+1):
                if 0 < Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos2[0] == 0:
                        valid_move = False
                        promotion = 1
        if piece == 11:
            if pos2[0] == pos1[0]+1 or pos2[0] == pos1[0]-1:
                if pos2[1] == pos1[1]+2 or pos2[1] == pos1[1]-2:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
            elif pos2[0] == pos1[0]+2 or pos2[0] == pos1[0]-2:
                if pos2[1] == pos1[1]+1 or pos2[1] == pos1[1]-1:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
        if piece == 10:
            if pos2[0] == (pos1[0]-1) or pos2[0] == (pos1[0]+1) or pos2[0] == (pos1[0]):
                if pos2[1] == (pos1[1]-1) or pos2[1] == (pos1[1]+1) or pos2[1] == (pos1[1]):
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        been_moved = True
            if pos2[0]==pos1[0] and pos2[1] == pos1[1]+2 and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]][pos2[1]-1] == 0 and Gameboard[pos1[0]][pos1[1]+3] == 7:
                    for spr in all_sprites:
                        if spr.board_pos == (7, 7):
                            if spr.been_moved == False:
                                valid_move = True
                                castling = 1
            if pos2[0]==pos1[0] and pos2[1] == pos1[1]-2 and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]][pos2[1]+1] == 0 and Gameboard[pos1[0]][pos1[1]-4] == 7 and Gameboard[pos1[0]][pos1[1]-3] == 0:
                    for spr in all_sprites:
                        if spr.board_pos == (7, 0):
                            if spr.been_moved == False:
                                castling = 2
        if piece == 7:
            if pos2[0] == pos1[0]:
                if Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos1[1] < pos2[1]:
                        for number in Gameboard[pos2[0]][pos1[1]+1:pos2[1]]:
                            if number != 0:
                                valid_move = False
                                been_moved = True
                    elif pos1[1] > pos2[1]:
                        for number in Gameboard[pos2[0]][pos2[1]+1:pos1[1]]:
                            if number != 0:
                                valid_move = False
                                been_moved = True
            elif pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos1[0] < pos2[0]:
                        for each_row in Gameboard[pos1[0]+1:pos2[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
                    elif pos1[0] > pos2[0]:
                        for each_row in Gameboard[pos2[0]+1:pos1[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
        if piece == 8:
            for num in range(1, 9):
                if pos2[0] == pos1[0]+num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]+num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]-numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]-numb] != 0:
                                    valid_move = False
        if piece == 9:
            for num in range(1, 9):
                if pos2[0] == pos1[0]+num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]+num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]-numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] < 7:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]-numb] != 0:
                                    valid_move = False
            if pos2[0] == pos1[0]:
                if Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos1[1] < pos2[1]:
                        for number in Gameboard[pos2[0]][pos1[1]+1:pos2[1]]:
                            if number != 0:
                                valid_move = False
                    elif pos1[1] > pos2[1]:
                        for number in Gameboard[pos2[0]][pos2[1]+1:pos1[1]]:
                            if number != 0:
                                valid_move = False
            elif pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] < 7:
                    valid_move = True
                    if pos1[0] < pos2[0]:
                        for each_row in Gameboard[pos1[0]+1:pos2[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
                    elif pos1[0] > pos2[0]:
                        for each_row in Gameboard[pos2[0]+1:pos1[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
    elif player == 2:
        if piece == 6:
            if pos2[0] == (pos1[0]+1) and pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos2[0] == 7:
                        valid_move = False
                        promotion = 2
            elif pos2[0] == (pos1[0]+2) and pos2[1] == pos1[1] and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]-1][pos2[1]] == 0:
                    valid_move = True
            elif pos2[0] == (pos1[0]+1) and pos2[1] == (pos1[1]-1):
                if Gameboard[pos2[0]][pos2[1]] >= 7:
                    valid_move = True
                    if pos2[0] == 7:
                        valid_move = False
                        promotion = 2
            elif pos2[0] == (pos1[0]+1) and pos2[1] == (pos1[1]+1):
                if Gameboard[pos2[0]][pos2[1]] >= 7:
                    valid_move = True
                    if pos2[0] == 7:
                        valid_move = False
                        promotion = 2
        if piece == 5:
            if pos2[0] == pos1[0]+1 or pos2[0] == pos1[0]-1:
                if pos2[1] == pos1[1]+2 or pos2[1] == pos1[1]-2:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
            elif pos2[0] == pos1[0]+2 or pos2[0] == pos1[0]-2:
                if pos2[1] == pos1[1]+1 or pos2[1] == pos1[1]-1:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
        elif piece == 4:
            if pos2[0] == (pos1[0]-1) or pos2[0] == (pos1[0]+1) or pos2[0] == (pos1[0]):
                if pos2[1] == (pos1[1]-1) or pos2[1] == (pos1[1]+1) or pos2[1] == (pos1[1]):
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
            if pos2[0]==pos1[0] and pos2[1] == pos1[1]+2 and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]][pos2[1]-1] == 0 and Gameboard[pos1[0]][pos1[1]+3] == 1:
                    for spr in all_sprites:
                        if spr.board_pos == (0, 7):
                            if spr.been_moved == False:
                                valid_move = True
                                castling = 1
            if pos2[0]==pos1[0] and pos2[1] == pos1[1]-2 and not been_moved:
                if Gameboard[pos2[0]][pos2[1]] == 0 and Gameboard[pos2[0]][pos2[1]+1] == 0 and Gameboard[pos1[0]][pos1[1]-4] == 1 and Gameboard[pos1[0]][pos1[1]-3] == 0:
                    for spr in all_sprites:
                        if spr.board_pos == (0, 0):
                            if spr.been_moved == False:
                                valid_move = True
                                castling = 2
        if piece == 1:
            if pos2[0] == pos1[0]:
                if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos1[1] < pos2[1]:
                        for number in Gameboard[pos2[0]][pos1[1]+1:pos2[1]]:
                            if number != 0:
                                valid_move = False
                    elif pos1[1] > pos2[1]:
                        for number in Gameboard[pos2[0]][pos2[1]+1:pos1[1]]:
                            if number != 0:
                                valid_move = False
            elif pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos1[0] < pos2[0]:
                        for each_row in Gameboard[pos1[0]+1:pos2[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
                    elif pos1[0] > pos2[0]:
                        for each_row in Gameboard[pos2[0]+1:pos1[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
        if piece == 2:
            for num in range(1, 9):
                if pos2[0] == pos1[0]+num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]+num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]-numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]-numb] != 0:
                                    valid_move = False
        if piece == 3:
            for num in range(1, 9):
                if pos2[0] == pos1[0]+num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]+num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos2[0]-pos1[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]+numb][pos1[1]-numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]+num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]+numb] != 0:
                                    valid_move = False
                elif pos2[0] == pos1[0]-num and pos2[1] == pos1[1]-num:
                    if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                        valid_move = True
                        distance = pos1[0]-pos2[0]
                        if distance > 0:
                            for numb in range(1, distance):
                                if Gameboard[pos1[0]-numb][pos1[1]-numb] != 0:
                                    valid_move = False
            if pos2[0] == pos1[0]:
                if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos1[1] < pos2[1]:
                        for number in Gameboard[pos2[0]][pos1[1]+1:pos2[1]]:
                            if number != 0:
                                valid_move = False
                    elif pos1[1] > pos2[1]:
                        for number in Gameboard[pos2[0]][pos2[1]+1:pos1[1]]:
                            if number != 0:
                                valid_move = False
            elif pos2[1] == pos1[1]:
                if Gameboard[pos2[0]][pos2[1]] >= 7 or Gameboard[pos2[0]][pos2[1]] == 0:
                    valid_move = True
                    if pos1[0] < pos2[0]:
                        for each_row in Gameboard[pos1[0]+1:pos2[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False
                    elif pos1[0] > pos2[0]:
                        for each_row in Gameboard[pos2[0]+1:pos1[0]]:
                            if each_row[pos2[1]] != 0:
                                valid_move = False

generate_board()
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
            clicked_sprites2 = [s for s in all_buttons if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                for s in all_sprites:
                    if i == s and white_move and s.type >= 7:
                        change_val = s.type
                        piece_chosen = True
                        original_piece = s
                    elif i == s and white_move and s.type < 7 and piece_chosen:
                        valid_move = False
                        check_move(1, original_piece.type, original_piece.board_pos, s.board_pos, original_piece.been_moved)
                        if valid_move:
                            original_piece.been_moved = True
                            s.been_moved = True
                            s.change(all_images[change_val-1])
                            s.type = change_val
                            Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                            original_piece.change(transparent_img)
                            original_piece.type = 0
                            Gameboard[original_piece.board_pos[0]][original_piece.board_pos[1]] = 0
                            piece_chosen = False
                            white_move = False

                        if castling == 1:
                            for piece in all_sprites:
                                if piece.board_pos == (7, 5):
                                    rook_pos2 = piece
                                if piece.board_pos == (7, 7):
                                    rook_moving = piece
                            rook_moving.been_moved = True
                            rook_moving.change(transparent_img)
                            rook_moving.type = 0
                            Gameboard[rook_moving.board_pos[0]][rook_moving.board_pos[1]] = 0
                            rook_pos2.been_moved = True
                            rook_pos2.change(all_images[6])
                            rook_pos2.type = 7
                            Gameboard[rook_pos2.board_pos[0]][rook_pos2.board_pos[1]] = 0
                            castling = 0

                        if castling == 2:
                            for piece in all_sprites:
                                if piece.board_pos == (7, 3):
                                    rook_pos2 = piece
                                if piece.board_pos == (7, 0):
                                    rook_moving = piece
                            rook_moving.been_moved = True
                            rook_moving.change(transparent_img)
                            rook_moving.type = 0
                            Gameboard[rook_moving.board_pos[0]][rook_moving.board_pos[1]] = 0
                            rook_pos2.been_moved = True
                            rook_pos2.change(all_images[6])
                            rook_pos2.type = 7
                            Gameboard[rook_pos2.board_pos[0]][rook_pos2.board_pos[1]] = 0
                            castling = 0

                        if promotion == 1:
                            promoting = True
                            s.change(all_images[change_val-1])
                            s.type = change_val
                            Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                            original_piece.change(transparent_img)
                            original_piece.type = 0
                            Gameboard[original_piece.board_pos[0]][original_piece.board_pos[1]] = 0
                            while promoting:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        playing = False
                                        promoting = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos = pygame.mouse.get_pos()
                                        clicked_sprites = [sp for sp in all_promotion_buttons if sp.rect.collidepoint(pos)]
                                        for sp in clicked_sprites:
                                            for button in all_promotion_buttons:
                                                if sp == button:
                                                    s.change(all_images[button.piece-1])
                                                    s.type = button.piece
                                                    Gameboard[s.board_pos[0]][s.board_pos[1]] = button.piece
                                                    promoting = False
                                    dis.fill(dark_blue)
                                    dis.blit(chess_board_img, [100, 100])
                                    all_sprites.draw(dis)
                                    all_promotion_buttons.draw(dis)
                                    all_buttons.draw(dis)
                                    pygame.display.flip()
                                    clock.tick(30)
                            promotion = 0
                            piece_chosen = False
                            white_move = False


                    elif i == s and not white_move and 0 < s.type < 7:
                        change_val = s.type
                        piece_chosen = True
                        original_piece = s
                    elif i == s and not white_move and piece_chosen:
                        if s.type >= 7 or s.type == 0:
                            valid_move = False
                            if not adjusting:
                                check_move(2, original_piece.type, original_piece.board_pos, s.board_pos, original_piece.been_moved)
                            elif adjusting:
                                valid_move = True
                            if valid_move:
                                s.change(all_images[change_val-1])
                                s.type = change_val
                                Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                                original_piece.change(transparent_img)
                                original_piece.type = 0
                                Gameboard[original_piece.board_pos[0]][original_piece.board_pos[1]] = 0
                                piece_chosen = False
                                white_move = True
                        if castling == 1:
                            for piece in all_sprites:
                                if piece.board_pos == (0, 5):
                                    rook_pos2 = piece
                                if piece.board_pos == (0, 7):
                                    rook_moving = piece
                            rook_moving.been_moved = True
                            rook_moving.change(transparent_img)
                            rook_moving.type = 0
                            Gameboard[rook_moving.board_pos[0]][rook_moving.board_pos[1]] = 0
                            rook_pos2.been_moved = True
                            rook_pos2.change(all_images[0])
                            rook_pos2.type = 1
                            Gameboard[rook_pos2.board_pos[0]][rook_pos2.board_pos[1]] = 0
                            castling = 0
                            
                        if castling == 2:
                            for piece in all_sprites:
                                if piece.board_pos == (0, 3):
                                    rook_pos2 = piece
                                if piece.board_pos == (0, 0):
                                    rook_moving = piece
                            rook_moving.been_moved = True
                            rook_moving.change(transparent_img)
                            rook_moving.type = 0
                            Gameboard[rook_moving.board_pos[0]][rook_moving.board_pos[1]] = 0
                            rook_pos2.been_moved = True
                            rook_pos2.change(all_images[0])
                            rook_pos2.type = 1
                            Gameboard[rook_pos2.board_pos[0]][rook_pos2.board_pos[1]] = 0

                            castling = 0
                        if promotion == 2:
                            promoting = True
                            s.change(all_images[change_val-1])
                            s.type = change_val
                            Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                            original_piece.change(transparent_img)
                            original_piece.type = 0
                            Gameboard[original_piece.board_pos[0]][original_piece.board_pos[1]] = 0
                            while promoting:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        playing = False
                                        promoting = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos = pygame.mouse.get_pos()
                                        clicked_sprites = [sp for sp in all_promotion_buttons2 if sp.rect.collidepoint(pos)]
                                        for sp in clicked_sprites:
                                            for button in all_promotion_buttons2:
                                                if sp == button:
                                                    s.change(all_images[button.piece-1])
                                                    s.type = button.piece
                                                    Gameboard[s.board_pos[0]][s.board_pos[1]] = button.piece
                                                    promoting = False
                                    dis.fill(dark_blue)
                                    dis.blit(chess_board_img, [100, 100])
                                    all_sprites.draw(dis)
                                    all_promotion_buttons2.draw(dis)
                                    all_buttons.draw(dis)
                                    pygame.display.flip()
                                    clock.tick(30)
                            promotion = 0
                            piece_chosen = False
                            white_move = True
                        
            for i in clicked_sprites2:
                for s in all_buttons:
                    if i == s:
                        if s.button_type == 1:
                            if not agreed_draw1:
                                agreed_draw1 = True
                            else:
                                agreed_draw1 = False
                        if s.button_type == 2:
                            dis.blit(all_end_images[1], [90, 240])
                            pygame.display.flip()
                            playing = False
                        if s.button_type == 4:
                            if not agreed_draw2:
                                agreed_draw2 = True
                            else:
                                agreed_draw2 = False
                        if s.button_type == 3:
                            dis.blit(all_end_images[2], [90, 240])
                            pygame.display.flip()
                            playing = False
                        if agreed_draw1 and agreed_draw2:
                            agreed_draw = True
                        if s.button_type == 5:
                            if not adjusting:
                                adjusting = True
                            else:
                                adjusting = False
            while adjusting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                        promoting = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                        clicked_sprites2 = [s for s in all_buttons if s.rect.collidepoint(pos)]
                        clicked_sprites3 = [s for s in all_promotion_buttons2 if s.rect.collidepoint(pos)]
                        clicked_sprites4 = [s for s in all_promotion_buttons if s.rect.collidepoint(pos)]
                        for sp in clicked_sprites:
                            for s in all_sprites:
                                if sp == s and piece_chosen:
                                    # original_piece.been_moved = True
                                    if change_val != 0:
                                        s.been_moved = True
                                        s.change(all_images[change_val-1])
                                        s.type = change_val
                                        Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                                        # original_piece.change(transparent_img)
                                        # original_piece.type = 0
                                        # Gameboard[original_piece.board_pos[0]][original_piece.board_pos[1]] = 0
                                        piece_chosen = False
                                    elif change_val == 0:
                                        s.been_moved = True
                                        s.change(transparent_img)
                                        s.type = change_val
                                        Gameboard[s.board_pos[0]][s.board_pos[1]] = change_val
                                        piece_chosen = False
                                elif sp == s:
                                    # print("works")
                                    change_val = s.type
                                    piece_chosen = True
                                    original_piece = s
                        for sp in clicked_sprites4:
                            for s in all_promotion_buttons:
                                if sp == s and piece_chosen:
                                    # print("works")
                                    change_val = s.piece
                                    piece_chosen = True
                                    original_piece = s
                        for sp in clicked_sprites3:
                            for s in all_promotion_buttons2:
                                if sp == s and piece_chosen == False:
                                    # print("works")
                                    change_val = s.piece
                                    piece_chosen = True
                                    original_piece = s
                        for sp in clicked_sprites2:
                            for s in all_buttons:
                                if sp == s:
                                    if s.button_type == 5:
                                        if not adjusting:
                                            adjusting = True
                                        else:
                                            adjusting = False
                dis.fill(dark_blue)
                dis.blit(chess_board_img, [100, 100])
                all_sprites.draw(dis)
                all_promotion_buttons2.draw(dis)
                all_promotion_buttons.draw(dis)
                all_buttons.draw(dis)
                pygame.draw.rect(dis, green, [18, 302, 52, 52], 2)
                pygame.display.flip()
                clock.tick(30)
    if playing:
        update_dis()
        clock.tick(30)