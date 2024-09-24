
import pygame
import math
import random

pygame.init()
# Define colors and fonts
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 120, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)
lose_message = font3.render('', False, white)

# Create the window
dis_width = 1000
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('A World')

# Create the variables needed for the program
clock = pygame.time.Clock()

working = True
prey_coords = []
predator_coords = []
plant_coords = []
prey_awareness = 500

directions = ['up', 'down']
directions2 = ['left', 'right']
prey_directions = ['']
prey_directions2 = ['']
predator_directions = ['']
predator_directions2 = ['']
direction_timer = 181
time = 0
id_ = 0
id_pd = 0


class Predator(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, id_num):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.id = id_num
        all_sprites.add(self)
        all_predators.add(self)

    def move_up(self, pixels):
        self.rect.centery -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.centery += pixels
        if self.rect.y > (dis_height - self.rect.height - 50):
            self.rect.y = (dis_height - self.rect.height - 50)

    def move_left(self, pixels):
        self.rect.centerx -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.centerx += pixels
        if self.rect.x > (dis_width - self.rect.width):
            self.rect.x = (dis_width - self.rect.width)

    def live(self, prey_location):
        global id_
        global prey_directions
        global prey_directions2
        global direction_timer
        global predator_directions
        global predator_directions2
        iteration = 0
        prey_x = 0
        shortest_distance = 999_999
        nearest_x = 0
        nearest_y = 0
        for coord in prey_location:
            iteration += 1
            if iteration == 1:
                prey_x = coord
            if iteration == 2:
                prey_y = coord
                new_distance = math.dist([prey_x, prey_y], [self.rect.centerx, self.rect.centery])
                if new_distance < shortest_distance:
                    shortest_distance = new_distance
                    nearest_x = prey_x
                    nearest_y = prey_y
                iteration = 0
        predator_speed = self.rect.width*0.05
        if shortest_distance < 500:
            if nearest_x < self.rect.centerx:
                self.move_left(predator_speed)
            elif nearest_x > self.rect.centerx:
                self.move_right(predator_speed)
            if nearest_y < self.rect.centery:
                self.move_up(predator_speed)
            elif nearest_y > self.rect.centery:
                self.move_down(predator_speed)
        else:
            if direction_timer > 180:
                direction = random.choice(directions)
                direction2 = random.choice(directions2)
                predator_directions = []
                predator_directions2 = []
                predator_directions.append(direction)
                predator_directions2.append(direction2)
            direct = predator_directions2[self.id]
            direct2 = predator_directions[self.id]
            if direct == 'left':
                self.move_left(predator_speed)
            elif direct == 'right':
                self.move_right(predator_speed)
            if direct2 == 'up':
                self.move_up(predator_speed)
            elif direct2 == 'down':
                self.move_down(predator_speed)
        for the_prey in all_prey:
            if self.rect.colliderect(the_prey):
                x = self.rect.x
                y = self.rect.y
                if self.rect.width <= 95:
                    self.rect.width += 5
                    self.rect.height += 5
                    self.image = pygame.Surface([self.rect.width, self.rect.height])
                    self.image.fill(black)
                    pygame.draw.rect(self.image, self.color, [0, 0, self.rect.width, self.rect.height])
                    self.rect = self.image.get_rect()
                    self.rect.x = x
                    self.rect.y = y
                the_prey.kill()

                direction_timer = 181
                new_prey = Prey(blue, 15, 15, random.randint(50, dis_width-50), random.randint(50, dis_height-50), id_)


class Prey(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, id_num):
        super().__init__()

        updated_width = width*(random.choice((1, 1.5, 2)))
        updated_height = updated_width
        if height != width:
            updated_height = width*(random.choice((0.5, 1, 2)))
        self.image = pygame.Surface([updated_width, updated_height])
        self.image.fill(black)
        pygame.draw.rect(self.image, color, [0, 0, updated_width, updated_height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.id = id_num
        self.confidence = random.randrange(0, 3)
        all_sprites.add(self)
        all_prey.add(self)

    def move_up(self, pixels):
        self.rect.centery -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.centery += pixels
        if self.rect.y > (dis_height - self.rect.height - 50):
            self.rect.y = (dis_height - self.rect.height - 50)

    def move_left(self, pixels):
        self.rect.centerx -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.centerx += pixels
        if self.rect.x > (dis_width - self.rect.width):
            self.rect.x = (dis_width - self.rect.width)

    def live(self, predator_location, plant_location):
        global directions
        global directions2
        global prey_directions
        global prey_directions2
        global prey_awareness
        global direction_timer
        iteration = 0
        predator_x = 0
        shortest_distance2 = 999_999
        nearest_x = 0
        nearest_y = 0
        for coord in predator_location:
            iteration += 1
            if iteration == 1:
                predator_x = coord
            if iteration == 2:
                predator_y = coord
                new_distance = math.dist([predator_x, predator_y], [self.rect.centerx, self.rect.centery])
                if new_distance < shortest_distance2:
                    shortest_distance2 = new_distance
                    nearest_x = predator_x
                    nearest_y = predator_y
                iteration = 0
        iteration = 0
        plant_x = 0
        shortest_distance = 999_999
        nearest_x1 = 0
        nearest_y1 = 0
        for coord in plant_location:
            iteration += 1
            if iteration == 1:
                plant_x = coord
            if iteration == 2:
                plant_y = coord
                new_distance = math.dist([plant_x, plant_y], [self.rect.centerx, self.rect.centery])
                if new_distance < shortest_distance:
                    shortest_distance = new_distance
                    nearest_x1 = plant_x
                    nearest_y1 = plant_y
                iteration = 0
        prey_speed = self.rect.width*0.067
        if self.confidence == 1:
            if shortest_distance2 < prey_awareness:
                if nearest_x < self.rect.centerx:
                    self.move_right(prey_speed)
                elif nearest_x > self.rect.centerx:
                    self.move_left(prey_speed)
                if nearest_y < self.rect.centery:
                    self.move_down(prey_speed)
                elif nearest_y > self.rect.centery:
                    self.move_up(prey_speed)
            elif shortest_distance < prey_awareness:
                if nearest_x1 < self.rect.centerx:
                    self.move_left(prey_speed)
                elif nearest_x1 > self.rect.centerx:
                    self.move_right(prey_speed)
                if nearest_y1 < self.rect.centery:
                    self.move_up(prey_speed)
                elif nearest_y1 > self.rect.centery:
                    self.move_down(prey_speed)
            else:
                if direction_timer > 180:
                    direction = random.choice(directions)
                    direction2 = random.choice(directions2)
                    prey_directions = []
                    prey_directions2 = []
                    prey_directions.append(direction)
                    prey_directions2.append(direction2)
                    direction_timer = 0
                direct = prey_directions2[self.id]
                direct2 = prey_directions[self.id]
                if direct == 'left':
                    self.move_left(prey_speed)
                elif direct == 'right':
                    self.move_right(prey_speed)
                if direct2 == 'up':
                    self.move_up(prey_speed)
                elif direct2 == 'down':
                    self.move_down(prey_speed)
        elif self.confidence == 0:
            if shortest_distance2 < prey_awareness:
                if nearest_x < self.rect.centerx:
                    self.move_right(prey_speed)
                elif nearest_x > self.rect.centerx:
                    self.move_left(prey_speed)
                if nearest_y < self.rect.centery:
                    self.move_down(prey_speed)
                elif nearest_y > self.rect.centery:
                    self.move_up(prey_speed)
            else:
                if direction_timer > 180:
                    direction = random.choice(directions)
                    direction2 = random.choice(directions2)
                    prey_directions = []
                    prey_directions2 = []
                    prey_directions.append(direction)
                    prey_directions2.append(direction2)
                    direction_timer = 0
                direct = prey_directions2[self.id]
                direct2 = prey_directions[self.id]
                if direct == 'left':
                    self.move_left(prey_speed)
                elif direct == 'right':
                    self.move_right(prey_speed)
                if direct2 == 'up':
                    self.move_up(prey_speed)
                elif direct2 == 'down':
                    self.move_down(prey_speed)
        elif self.confidence == 2:
            if shortest_distance < prey_awareness:
                if nearest_x1 < self.rect.centerx:
                    self.move_left(prey_speed)
                elif nearest_x1 > self.rect.centerx:
                    self.move_right(prey_speed)
                if nearest_y1 < self.rect.centery:
                    self.move_up(prey_speed)
                elif nearest_y1 > self.rect.centery:
                    self.move_down(prey_speed)
            elif shortest_distance2 < prey_awareness:
                if nearest_x < self.rect.centerx:
                    self.move_right(prey_speed)
                elif nearest_x > self.rect.centerx:
                    self.move_left(prey_speed)
                if nearest_y < self.rect.centery:
                    self.move_down(prey_speed)
                elif nearest_y > self.rect.centery:
                    self.move_up(prey_speed)
            else:
                if direction_timer > 180:
                    direction = random.choice(directions)
                    direction2 = random.choice(directions2)
                    prey_directions = []
                    prey_directions2 = []
                    prey_directions.append(direction)
                    prey_directions2.append(direction2)
                    direction_timer = 0
                direct = prey_directions2[self.id]
                direct2 = prey_directions[self.id]
                if direct == 'left':
                    self.move_left(prey_speed)
                elif direct == 'right':
                    self.move_right(prey_speed)
                if direct2 == 'up':
                    self.move_up(prey_speed)
                elif direct2 == 'down':
                    self.move_down(prey_speed)

        for the_plant in all_plants:
            if self.rect.colliderect(the_plant):
                x = self.rect.x
                y = self.rect.y
                self.rect.width += 5
                self.rect.height += 5
                self.image = pygame.Surface([self.rect.width, self.rect.height])
                self.image.fill(black)
                pygame.draw.rect(self.image, self.color, [0, 0, self.rect.width, self.rect.height])
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                the_plant.kill()
                direction_timer = 181
                new_prey = Prey(blue, 15, 15, random.randint(50, dis_width-50), random.randint(50, dis_height-50), id_)
                new_plant = Plant(green, 15, 15, random.randint(50, dis_width-50), random.randint(50, dis_height-50))


class Plant(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        all_sprites.add(self)
        all_plants.add(self)


all_sprites = pygame.sprite.Group()
all_predators = pygame.sprite.Group()
all_prey = pygame.sprite.Group()
all_plants = pygame.sprite.Group()
predator1 = Predator(black, 20, 20, 20, 20, id_pd)
prey1 = Prey(blue, 15, 15, 500, 500, id_)
plant1 = Plant(green, 15, 15, 400, 400)


def update_dis():
    dis.fill(white)
    all_sprites.draw(dis)
    dis.blit(prey_mesg, (50, dis_height-50))
    dis.blit(time_mesg, (300, dis_height - 50))
    pygame.display.flip()


def all_living():
    global directions
    global directions2
    for a_prey in all_prey:
        prey_coords.append(a_prey.rect.centerx)
        prey_coords.append(a_prey.rect.centery)
    for predators in all_predators:
        predator_coords.append(predators.rect.centerx)
        predator_coords.append(predators.rect.centery)
    for plant in all_plants:
        plant_coords.append(plant.rect.centerx)
        plant_coords.append(plant.rect.centery)
    for predator in all_predators:
        predator.live(prey_coords)
    for prey in all_prey:
        prey.live(predator_coords, plant_coords)
    all_sprites.update()


while working:
    prey_coords = []
    predator_coords = []
    plant_coords = []
    prey_count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                working = False
    for _ in all_prey:
        prey_count += 1
    prey_mesg = font4.render(f'Prey Total: {prey_count}', False, black)
    time_mesg = font4.render(f'Time: {math.floor(time)} seconds', False, black)
    all_living()
    update_dis()
    direction_timer += 1
    time += 1/30
    clock.tick(30)
