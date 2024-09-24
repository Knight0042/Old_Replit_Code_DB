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
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (75, 75, 75)
gray2 = (100, 100, 100)
brown = (165, 42, 42)

using_color = black

dis.fill(white)

clear_icon = pygame.image.load('clear.png')
backround_icon = pygame.image.load('backround.png')


class ColorPicker(pygame.sprite.Sprite):
    def __init__(self, color, x, y, picker_list, type):
        super().__init__()
        if type == 0:
            self.image = pygame.Surface([50, 50])
            self.image.fill((1, 1, 1))
            self.image.set_colorkey((1, 1, 1))
            pygame.draw.rect(self.image, color, [0, 0, 50, 50])
        elif type == 1:
            self.image = clear_icon
        elif type == 2:
            self.image = backround_icon
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        picker_list.add(self)


class TextBox(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, picker_list):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((1, 1, 1))
        self.image.set_colorkey((1, 1, 1))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        picker_list.add(self)


# def text_input(string_, x, y):
#   inputting = True
#   while inputting:
#     event = pygame.event.poll()
#     # keys = pygame.key.get_pressed()

#     if event.type == pygame.KEYDOWN:
#       key = pygame.key.name(event.key)  # Returns string id of pressed key.
#       for num in range(0, 10):
#         if key == str(num):
#           string_ = string_+key
#       if key == 'backspace':
#         string_ = ''
#       if key == 'return':
#         inputting = False
#     mesg_ = font2.render(string_, True, black)
#     pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
#     all_sprites.draw(dis)
#     dis.blit(mesg_, [x, y])
#     pygame.display.flip()

all_sprites = pygame.sprite.Group()

blue_selector = ColorPicker(blue, 50, 50, all_sprites, 0)

yellow_selector = ColorPicker(yellow, 125, 50, all_sprites, 0)

green_selector = ColorPicker(green, 50, 125, all_sprites, 0)

red_selector = ColorPicker(red, 125, 125, all_sprites, 0)

violet_selector = ColorPicker(violet, 50, 200, all_sprites, 0)

orange_selector = ColorPicker(orange, 125, 200, all_sprites, 0)

gray_selector = ColorPicker(gray2, 50, 275, all_sprites, 0)

black_selector = ColorPicker(black, 125, 275, all_sprites, 0)

white_selector = ColorPicker(white, 50, 350, all_sprites, 0)

brown_selector = ColorPicker(brown, 125, 350, all_sprites, 0)

clear_selector = ColorPicker(white, 125, 425, all_sprites, 1)

backround_selector = ColorPicker(white, 50, 425, all_sprites, 2)

thickness_controller = TextBox(white, 25, 500, 175, 50, all_sprites)

red_controller = TextBox(white, 42, 560, 40, 25, all_sprites)

green_controller = TextBox(white, 92, 560, 40, 25, all_sprites)

blue_controller = TextBox(white, 142, 560, 40, 25, all_sprites)

thickness = 10

mouse_x = 0
mouse_y = 0
mouse_pressed = False
mouse_x_previous = 0
mouse_y_previous = 0
assist_x = 0
assist_y = 0
assist_x2 = 0
assist_y2 = 0
distance = 0
x_distance = 0
y_distance = 0

thickness_string = '10'
red_string = '0'
green_string = '0'
blue_string = '0'
typed = False
custom_color = white

while running:
    if int(red_string) > 255 or int(red_string) < 0:
        red_string = '255'
    if int(green_string) > 255 or int(green_string) < 0:
        green_string = '255'
    if int(blue_string) > 255 or int(blue_string) < 0:
        blue_string = '255'
    custom_color = (int(red_string), int(green_string), int(blue_string))
    custom_selector = ColorPicker(custom_color, 87, 620, all_sprites, 0)
    inputting = False
    thickness = int(thickness_string)
    thickness_mesg = font2.render(thickness_string, True, black)
    red_mesg = font4.render(red_string, True, black)
    green_mesg = font4.render(green_string, True, black)
    blue_mesg = font4.render(blue_string, True, black)
    iteration = 0
    all_sprites.update()
    pos = pygame.mouse.get_pos()
    for i in pos:
        iteration += 1
        if iteration == 1:
            mouse_x = i
        if iteration == 2:
            mouse_y = i
    if mouse_pressed and not typed:
        # distance = math.sqrt( ((mouse_x-mouse_x_previous)**2)+((mouse_y-mouse_y_previous)**2) )
        for num in range(2, 10):
            if mouse_x > mouse_x_previous:
                # distance = abs(distance)
                x_distance = mouse_x - mouse_x_previous
            if mouse_x < mouse_x_previous:
                x_distance = mouse_x_previous - mouse_x
                x_distance = -1 * x_distance

            if mouse_y < mouse_y_previous:
                # distance = abs(distance)
                y_distance = mouse_y - mouse_y_previous
            if mouse_y > mouse_y_previous:
                y_distance = mouse_y_previous - mouse_y
                y_distance = -1 * y_distance
        #   if mouse_x > mouse_x_previous and mouse_y > mouse_y_previous:
        #     assist_x = mouse_x_previous + int(x_distance/num)
        #     assist_y = mouse_y_previous + int(y_distance/num)
        #     assist_x2 = mouse_x_previous + int((x_distance/num)*(num-1))
        #     assist_y2 = mouse_y_previous + int((y_distance/num)*(num-1))
        #   if mouse_x < mouse_x_previous and mouse_y > mouse_y_previous:
        #     assist_x = mouse_x_previous + int(x_distance/num)
        #     assist_y = mouse_y_previous + int(y_distance/num)
        #     assist_x2 = mouse_x_previous + int((x_distance/num)*(num-1))
        #     assist_y2 = mouse_y_previous + int((y_distance/num)*(num-1))
        #   if mouse_x > mouse_x_previous and mouse_y < mouse_y_previous:
        #     assist_x = mouse_x_previous + int(x_distance/num)
        #     assist_y = mouse_y_previous + int(y_distance/num)
        #     assist_x2 = mouse_x_previous + int((x_distance/num)*(num-1))
        #     assist_y2 = mouse_y_previous + int((y_distance/num)*(num-1))
        #   if mouse_x < mouse_x_previous and mouse_y < mouse_y_previous:
        assist_x = mouse_x_previous + int(x_distance / num)
        assist_y = mouse_y_previous + int(y_distance / num)
        assist_x2 = mouse_x_previous + int((x_distance / num) * (num - 1))
        assist_y2 = mouse_y_previous + int((y_distance / num) * (num - 1))

        #   pygame.draw.rect(dis, using_color, [assist_x, assist_y, thickness, thickness])
        #   pygame.draw.rect(dis, using_color, [assist_x2, assist_y2, thickness, thickness])
        pygame.draw.circle(dis, using_color, [assist_x, assist_y], thickness)
        pygame.draw.circle(dis, using_color, [assist_x2, assist_y2], thickness)
    typed = False
    mouse_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse = pygame.mouse.get_pressed()
    if mouse[0] == True:
        pos = pygame.mouse.get_pos()
        for i in pos:
            iteration += 1
            if iteration == 1:
                mouse_x = i
            if iteration == 2:
                mouse_y = i
        mouse_x_previous = mouse_x
        mouse_y_previous = mouse_y
        clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
        for i in clicked_sprites:
            if i == blue_selector:
                using_color = blue
                typed = True
            if i == red_selector:
                using_color = red
                typed = True
            if i == yellow_selector:
                using_color = yellow
                typed = True
            if i == black_selector:
                using_color = black
                typed = True
            if i == white_selector:
                using_color = white
                typed = True
            if i == gray_selector:
                using_color = gray2
                typed = True
            if i == green_selector:
                using_color = green
                typed = True
            if i == violet_selector:
                using_color = violet
                typed = True
            if i == orange_selector:
                using_color = orange
                typed = True
            if i == brown_selector:
                using_color = brown
                typed = True
            if i == custom_selector:
                using_color = custom_color
                typed = True
            if i == backround_selector:
                dis.fill(using_color)
                typed = True
            if i == clear_selector:
                dis.fill(white)
                typed = True
            if i == thickness_controller:
                # text_input(thickness_string, 50, 505)
                # typed = True
                inputting = True
                while inputting:
                    event = pygame.event.poll()
                    # keys = pygame.key.get_pressed()

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)  # Returns string id of pressed key.
                        for num in range(0, 10):
                            if key == str(num):
                                thickness_string += key
                        if key == 'backspace':
                            thickness_string = ''
                        if key == 'return':
                            typed = True
                            inputting = False
                    thickness_mesg = font2.render(thickness_string, True, black)
                    pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
                    all_sprites.draw(dis)
                    dis.blit(thickness_mesg, [50, 505])
                    pygame.display.flip()
            if i == red_controller:
                # text_input(thickness_string, 50, 505)
                # typed = True
                inputting = True
                while inputting:
                    event = pygame.event.poll()
                    # keys = pygame.key.get_pressed()

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)  # Returns string id of pressed key.
                        for num in range(0, 10):
                            if key == str(num):
                                red_string += key
                        if key == 'backspace':
                            red_string = ''
                        if key == 'return':
                            if red_string == '':
                                red_string = '0'
                            typed = True
                            inputting = False
                    red_mesg = font4.render(red_string, True, black)
                    pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
                    all_sprites.draw(dis)
                    dis.blit(red_mesg, [42, 565])
                    pygame.display.flip()
            if i == green_controller:
                # text_input(thickness_string, 50, 505)
                # typed = True
                inputting = True
                while inputting:
                    event = pygame.event.poll()
                    # keys = pygame.key.get_pressed()

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)  # Returns string id of pressed key.
                        for num in range(0, 10):
                            if key == str(num):
                                green_string += key
                        if key == 'backspace':
                            green_string = ''
                        if key == 'return':
                            if green_string == '':
                                green_string = '0'
                            typed = True
                            inputting = False
                    green_mesg = font4.render(green_string, True, black)
                    pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
                    all_sprites.draw(dis)
                    dis.blit(green_mesg, [92, 565])
                    pygame.display.flip()
            if i == blue_controller:
                # text_input(thickness_string, 50, 505)
                # typed = True
                inputting = True
                while inputting:
                    event = pygame.event.poll()
                    # keys = pygame.key.get_pressed()

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)  # Returns string id of pressed key.
                        for num in range(0, 10):
                            if key == str(num):
                                blue_string += key
                        if key == 'backspace':
                            blue_string = ''
                        if key == 'return':
                            if blue_string == '':
                                blue_string = '0'
                            typed = True
                            inputting = False
                    blue_mesg = font4.render(blue_string, True, black)
                    pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
                    all_sprites.draw(dis)
                    dis.blit(blue_mesg, [142, 565])
                    pygame.display.flip()
        mouse_pressed = True
        mouse_pressed = True
        if not typed:
            #   pygame.draw.rect(dis, using_color, [mouse_x, mouse_y, thickness, thickness])
            pygame.draw.circle(dis, using_color, [mouse_x, mouse_y], thickness)
    #         mouse_pressed = True
    # if mouse_pressed:
    pygame.draw.rect(dis, gray, [0, 0, 225, dis_height])
    all_sprites.draw(dis)
    dis.blit(thickness_mesg, [50, 505])
    dis.blit(red_mesg, [42, 565])
    dis.blit(green_mesg, [92, 565])
    dis.blit(blue_mesg, [142, 565])
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
