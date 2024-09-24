import pygame
import random
import spritesheet
import math

pygame.init()

ss = spritesheet.spritesheet('cards.png')
ss2 = spritesheet.spritesheet('chip_spritesheet.png')
end_turn_img = pygame.image.load('end_turn_button.png')
fold_button_img = pygame.image.load('fold_button.png')

# Create the lists that will hold the images for the chips and cards. Also list define the image sizes.
card_images = []
chip_images = []

image_width = 61.5
image_height = 81

image_width2 = 65
image_height2 = 65

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
pygame.display.set_caption('Poker')

# Create the variables needed for the program such as card properties, chip properties, and hands.
clock = pygame.time.Clock()

playing = True
player_turn = True

player_hand = []
chip_values = [10, 50, 100, 300]
player_chip_total = [15, 10, 10, 3]
player_chip_value = 0
opponent_hand = []
enemy_chip_total = [15, 10, 10, 3]
cards = []
cards_in_play = []
card_val_list = []
chips_in_play = [0, 0, 0, 0]
player_chips_in_play = [0, 0, 0, 0]
suits = ['S', 'C', 'D', 'H']
card_dict = {}
chip_string = ''
chips_in_total = 0
player_chips_in_total = 0
spade_count = 0
club_count = 0
diamond_count = 0
heart_count = 0
e_bet = False
p_bet = False
e_bet_amount = 0
sector = 0

pcard1_val = 0
pcard2_val = 0
ecard1_val = 0
ecard2_val = 0
icard1_val = 0
icard2_val = 0
icard3_val = 0
icard4_val = 0
icard5_val = 0
iteration = 0
p_total = 0
e_total = 0
winner = ''


def load_images(image_list, num, x, y, ck, sprite_sheet, img_width, img_height):
    # Crops a spritesheet and adds the cropped image to a list
    global card_images
    global chip_images
    global image_height
    global image_width
    correction = 1
    if y == 0:
        correction2 = 0
    else:
        correction2 = 1
    for item in range(0, num):
        image = sprite_sheet.image_at(((x + item) * img_width + correction, y * img_height + correction2, img_width,
                                       img_height), colorkey=ck)
        image_list.append(image)


# loads all images needed for the program
for number in range(4):
    load_images(card_images, 13, 0, number, (1, 1, 1), ss, image_width, image_height)
load_images(chip_images, 4, 0, 0, black, ss2, image_width2, image_height2)
chip_images.append(end_turn_img)
chip_images.append(fold_button_img)


def deal_hand(hand):
    global player_hand
    global opponent_hand
    global cards
    # Add 2 random cards to either the opponent or player hand.
    # if hand == 1:
    #     hand_type = player_hand
    if hand == 2:
        hand_type = opponent_hand
    else:
        hand_type = player_hand
    for num in range(2):
        random_card = random.choice(cards)
        hand_type.append(random_card)
        cards.remove(random_card)


def count_chip_values():
    # Counts the amount of chips the player has and finds the total value of all chips
    global chip_values
    global player_chip_total
    global player_chip_value
    player_chip_value = 0
    itera = -1
    for num in player_chip_total:
        itera += 1
        player_chip_value += (num * chip_values[itera])


def add_cards(num):
    # Adds 5 random cards to the list of cards in play then remove those cards from the list of cards.
    global cards
    global cards_in_play
    for c in range(num):
        random_card = random.choice(cards)
        cards_in_play.append(random_card)
        cards.remove(random_card)


def start_game():
    # This function resets all hands and the cards in play. Then it deals the hands and adds the cards in play. It also
    # resets the winner and level
    # then calculates the overall chip values of the enemy and player.
    global enemy_chip_total
    global player_chip_total
    global player_chips_in_play
    global chips_in_play
    global winner
    global level
    global cards_in_play
    global player_hand
    global cards
    global opponent_hand
    global lose_message
    opponent_hand = []
    player_hand = []
    cards = []
    cards_in_play = []
    card_num = -1
    # Creates the list of all cards. Cards look like: S12 (Queen of Spades), H2 (2 of Hearts), C9 (9 of clubs) etc.
    # They are created by moving through
    # the list of suits and adding a value 1-13 to represent each card. For example, the list ['S', 'C', 'D', 'H'] will
    # take the first value 'S' and
    # add '1' to the string which gives the result of 'S1' meaning this card is the Ace of Spades. So,
    # ('S' + '1' = 'S1'). Then this string is added to
    # the list of cards and the next card is created. ('S' + '2' = 'S2') This process repeats for all cards.
    # until you end with ('H' + '13' = 'H13')
    # or the king of hearts.
    for suit in suits:
        for card in range(1, 14):
            card_num += 1
            cards.append(f'{suit + str(card)}')
            card_dict[cards[card_num]] = card_num
    level = 0
    winner = ''
    deal_hand(1)
    deal_hand(2)
    add_cards(5)
    count_chip_values()
    # Conducts the initial ante up for both players by removing $10 worth of chips and adding it to the amount of chips
    # in play. If out of $10 chips
    # then the other chips you have will be converted into $10 chips and one of those chips will be used. If either
    # player runs out of chips then they
    # lose the overall game.
    # I am also aware that real poker may not be played this way but this is how I've always played poker which is why
    # it is like this.
    if enemy_chip_total[0] > 0:
        enemy_chip_total[0] -= 1
    elif enemy_chip_total[1] > 0:
        enemy_chip_total[1] -= 1
        enemy_chip_total[0] += 4
    elif enemy_chip_total[2] > 0:
        enemy_chip_total[2] -= 1
        enemy_chip_total[0] += 9
    elif enemy_chip_total[3] > 0:
        enemy_chip_total[3] -= 1
        enemy_chip_total[0] += 29
    else:
        lose_message = font3.render('enemy loses', False, white)
    if player_chip_total[0] > 0:
        player_chip_total[0] -= 1
    elif player_chip_total[1] > 0:
        player_chip_total[1] -= 1
        player_chip_total[0] += 4
    elif player_chip_total[2] > 0:
        player_chip_total[2] -= 1
        player_chip_total[0] += 9
    elif player_chip_total[3] > 0:
        player_chip_total[3] -= 1
        player_chip_total[0] += 29
    else:
        lose_message = font3.render('Player loses', False, white)

    chips_in_play[0] += 2
    player_chips_in_play[0] += 1


class Chip(pygame.sprite.Sprite):
    # This is the class that creates the chips displayed on the screen that are clicked to bet chips.
    def __init__(self, x, y, chip_num, sprt_list):
        super().__init__()
        self.image = chip_images[chip_num]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprt_list.add(self)


def render_hand(hand, pos1, pos2):
    # This function updates the display to show the players cards.
    global card_dict
    global card_images
    global iteration
    iteration = 0
    card1 = chip_images[0]
    card2 = chip_images[0]
    for a_card in hand:
        iteration += 1
        a_card_number = card_dict[a_card]
        if iteration == 1:
            card1 = card_images[a_card_number]
        if iteration == 2:
            card2 = card_images[a_card_number]
    dis.blit(card1, pos1)
    dis.blit(card2, pos2)
    iteration = 0


def update_dis():
    # This function updates the display with all necessary information such as displaying the chips, cards, values of
    # things, and winners.
    global chips_in_total
    global player_chips_in_total
    global iteration
    dis.blit(message1, (dis_width / 2 - 40, dis_height - 150))
    chips_in_total = 0
    player_chips_in_total = 0
    render_hand(player_hand, (dis_width / 2 - 81, dis_height - 100), (dis_width / 2 + 20, dis_height - 100))

    iteration = 0
    card1_in = chip_images[0]
    card2_in = chip_images[0]
    card3_in = chip_images[0]
    card4_in = chip_images[0]
    card5_in = chip_images[0]
    for a_card_in in cards_in_play:
        iteration += 1
        a_card_number_in = card_dict[a_card_in]
        if iteration == 1:
            card1_in = card_images[a_card_number_in]
        if iteration == 2:
            card2_in = card_images[a_card_number_in]
        if iteration == 3:
            card3_in = card_images[a_card_number_in]
        if iteration == 4:
            card4_in = card_images[a_card_number_in]
        if iteration == 5:
            card5_in = card_images[a_card_number_in]
    if level > 0:
        dis.blit(card1_in, (dis_width / 2 - 253, dis_height - 350))
        dis.blit(card2_in, (dis_width / 2 - 140, dis_height - 350))
        dis.blit(card3_in, (dis_width / 2 - 28, dis_height - 350))
    if level > 1:
        dis.blit(card4_in, (dis_width / 2 + 92, dis_height - 350))
    if level > 2:
        dis.blit(card5_in, (dis_width / 2 + 204, dis_height - 350))
    iteration = 0
    for value in chip_values:
        iteration += 1
        value_mesg = font4.render(f'${value}', False, white)
        dis.blit(value_mesg, (dis_width / 2 + iteration * 75 + 50, dis_height - 40))
    iteration = 0
    for total in player_chip_total:
        iteration += 1
        total_mesg = font4.render(f'{total}', False, white)
        dis.blit(total_mesg, (dis_width / 2 + (iteration * 75) + 70, dis_height - 140))
    iteration = 0
    for chips_in in player_chips_in_play:
        iteration += 1
        player_chips_in_total += chips_in * chip_values[iteration - 1]
        chips_in_mesg = font4.render(f'{chips_in}', False, white)
        dis.blit(chips_in_mesg, (dis_width / 2 + iteration * 40 - 450, dis_height - 75))
    iteration = 0
    for chips_in in chips_in_play:
        iteration += 1
        chips_in_total += chips_in * chip_values[iteration - 1]
        chips_in_mesg = font4.render(f'{chips_in}', False, white)
        dis.blit(chips_in_mesg, (dis_width / 2 + iteration * 40 - 450, 125))

    player_chips_total_mesg = font4.render(f'${player_chips_in_total}', False, white)
    chips_total_mesg = font4.render(f'${chips_in_total}', False, white)
    dis.blit(player_chips_total_mesg, (dis_width / 2 - 375, dis_height - 125))
    dis.blit(chips_total_mesg, (dis_width / 2 - 375, 175))

    if player_turn:
        dis.blit(message2, (dis_width / 2 - 250, dis_height - 75))
    pygame.draw.line(dis, white, (0, dis_height - 220), (dis_width, dis_height - 220), 5)
    winner_mesg = font4.render(f'{winner}', False, white)
    dis.blit(winner_mesg, (dis_width / 2 - 20, 100))
    dis.blit(lose_message, (dis_width / 2 - 20, dis_height / 2 - 20))
    if winner != '':
        render_hand(opponent_hand, (dis_width / 2 - 200, 100), (dis_width / 2 - 100, 100))

    all_sprites.update()
    all_sprites.draw(dis)
    pygame.display.flip()


def typing_input(chip_num):
    # This function allows the user to type a number to represent the number of chips they wish to bet. If the number
    # typed is greater than the
    # number of chips the player has then the number bet is set to the number of chips the player has. If delete is
    # pressed the string is set to '0'
    # and when enter is pressed the loop ends.
    global chip_string
    global choice
    inputting = True
    chip_string = '0'
    while inputting:
        event_ = pygame.event.poll()

        if event_.type == pygame.KEYDOWN:
            key = pygame.key.name(event_.key)  # Returns string id of pressed key.
            for num in range(0, 10):
                if key == str(num):
                    chip_string += key
            if key == 'backspace':
                chip_string = '0'
            if key == 'return':
                inputting = False

        chip_mesg = font2.render(chip_string, True, white)
        update_dis()
        dis.blit(chip_mesg, (dis_width / 2 + 250, dis_height - 200))
        choice = int(chip_string)
        if choice > player_chip_total[chip_num]:
            choice = player_chip_total[chip_num]
        clock.tick(60)


def analyze_card(hand, numbe, test):
    # This function analyzes a card by moving through the string and responding to that character accordingly. If it is
    # a letter then the number of
    # that suit is increased. Ex. if it is 'S' then the spade count is increased by one. If the character is a number
    # then it is added to a number
    # string then that string is turned back into a value and set = to a specific value such as player card 1
    # represented as pcard1_val.
    global spade_count
    global club_count
    global diamond_count
    global heart_count
    global pcard1_val
    global pcard2_val
    global ecard1_val
    global ecard2_val
    global icard1_val
    global icard2_val
    global icard3_val
    global icard4_val
    global icard5_val
    global p_total
    global iteration
    global card_val_list
    iteration = 0
    ace = False
    card_val_str = '0'
    for character in hand[numbe]:
        iteration += 1
        if character == 'A':
            spade_count += 1
        elif character == 'C':
            club_count += 1
        elif character == 'D':
            diamond_count += 1
        elif character == 'H':
            heart_count += 1
        else:
            for numb in range(0, 14):
                if character == str(numb):
                    card_val_str += character
                    if character == '1':
                        ace = True
                    if iteration == 3:
                        ace = False
    if ace:
        card_val_list.append(14)
        iteration = 0
        for valu in card_val_list:
            iteration += 1
            if valu == 14:
                if iteration > 1:
                    card_val_list.remove(14)

    if test == 1:
        pcard1_val = int(card_val_str)
    if test == 2:
        pcard2_val = int(card_val_str)
    if test == 3:
        icard1_val = int(card_val_str)
    if test == 4:
        icard2_val = int(card_val_str)
    if test == 5:
        icard3_val = int(card_val_str)
    if test == 6:
        icard4_val = int(card_val_str)
    if test == 7:
        icard5_val = int(card_val_str)
    if test == 8:
        ecard1_val = int(card_val_str)
    if test == 9:
        ecard2_val = int(card_val_str)


def analyze_val_list(total_num):
    # This function analyzes the values of cards in the card value list. This checks if there are any pairs, straights,
    # triples, quadruples, and etc.
    global e_total
    global p_total
    global card_val_list
    previous_val = 0
    straight = 0
    straight_worth = 0
    p_straight = False
    total = 0
    first = True
    specific_card_amount = 0
    previous_val2 = 0
    previous_val3 = 0
    group_worth = 0
    for val in card_val_list:
        if val == previous_val:
            if val == previous_val2:
                specific_card_amount += 1
                group_worth = (val / 100)
            if val == previous_val3:
                specific_card_amount += 1
            specific_card_amount += 1
            straight += 0
        elif val - 1 == previous_val:
            straight += 1
        else:
            straight = 0
        previous_val3 = previous_val2
        previous_val2 = previous_val
        previous_val = val
        if straight == 5 and first:
            straight_worth = val / 50
            p_straight = True
            first = False
    # This calculates the worth of those cards in terms of a hand. Lower is better. Ex a straight has a value of 6 that
    # is then decreased further by
    # the worth of that straight as well as a high card. This value is then set equal to either the player total or
    # enemy total.

    card_worth = card_val_list[-1] / 10000
    if spade_count >= 5 and p_straight:
        total += (2.1 - card_worth - straight_worth)
    elif heart_count >= 5 and p_straight:
        total += (2.2 - card_worth - straight_worth)
    elif diamond_count >= 5 and p_straight:
        total += (2.3 - card_worth - straight_worth)
    elif club_count >= 5 and p_straight:
        total += (2.4 - card_worth - straight_worth)
    elif specific_card_amount == 6:
        total += (3 - card_worth)
    elif specific_card_amount == 4:
        total += (4 - card_worth)
    elif spade_count >= 5:
        total += (5.1 - card_worth)
    elif heart_count >= 5:
        total += (5.2 - card_worth)
    elif diamond_count >= 5:
        total += (5.3 - card_worth)
    elif club_count >= 5:
        total += (5.4 - card_worth)
    elif p_straight:
        total += (6 - card_worth - straight_worth)
    elif specific_card_amount == 3:
        total += (7 - card_worth - group_worth)
    elif specific_card_amount == 2:
        total += (8 - card_worth - group_worth)
    elif specific_card_amount == 1:
        total += (9 - card_worth - group_worth)
    else:
        total += (10 - card_worth)
    if total_num == 1:
        p_total = total
    if total_num == 2:
        e_total = total


def analyze_hands():
    # This function analyzes the hands of the player as well as opponent then decides the winner. If the winner is 'tie'
    # that just means it hasn't
    # been coded thoroughly enough.
    global opponent_hand
    global player_hand
    global cards_in_play
    global card_dict
    global pcard1_val
    global pcard2_val
    global icard1_val
    global icard2_val
    global icard3_val
    global icard4_val
    global icard5_val
    global spade_count
    global club_count
    global diamond_count
    global heart_count
    global winner
    global card_val_list
    spade_count = 0
    heart_count = 0
    club_count = 0
    diamond_count = 0
    analyze_card(player_hand, 0, 1)
    analyze_card(player_hand, 1, 2)
    analyze_card(cards_in_play, 0, 3)
    analyze_card(cards_in_play, 1, 4)
    analyze_card(cards_in_play, 2, 5)
    analyze_card(cards_in_play, 3, 6)
    analyze_card(cards_in_play, 4, 7)
    card_val_list = []
    card_val_list.append(pcard1_val)
    card_val_list.append(pcard2_val)
    card_val_list.append(icard1_val)
    card_val_list.append(icard2_val)
    card_val_list.append(icard3_val)
    card_val_list.append(icard4_val)
    card_val_list.append(icard5_val)
    card_val_list.sort()
    analyze_val_list(1)
    card_val_list = []
    spade_count = 0
    heart_count = 0
    club_count = 0
    diamond_count = 0
    analyze_card(cards_in_play, 0, 3)
    analyze_card(cards_in_play, 1, 4)
    analyze_card(cards_in_play, 2, 5)
    analyze_card(cards_in_play, 3, 6)
    analyze_card(cards_in_play, 4, 7)
    analyze_card(opponent_hand, 0, 8)
    analyze_card(opponent_hand, 1, 9)

    card_val_list.append(ecard1_val)
    card_val_list.append(ecard2_val)
    card_val_list.append(icard1_val)
    card_val_list.append(icard2_val)
    card_val_list.append(icard3_val)
    card_val_list.append(icard4_val)
    card_val_list.append(icard5_val)
    card_val_list.sort()
    analyze_val_list(2)

    if e_total < p_total:
        winner = 'enemy'
    elif e_total > p_total:
        winner = 'player'
    elif e_total == p_total:
        winner = 'tie'
    check_winner()


def check_winner():
    # This interprets the winner string and responds based on that string.
    global winner
    global iteration
    global chips_in_play
    global player_chip_total

    if winner == 'player':
        iteration = 0
        for chip_tot in chips_in_play:
            iteration += 1
            player_chip_total[iteration - 1] += chip_tot
            chips_in_play[iteration - 1] = 0
    elif winner == 'enemy':
        iteration = 0
        for chip_tot in chips_in_play:
            iteration += 1
            enemy_chip_total[iteration - 1] += chip_tot
            chips_in_play[iteration - 1] = 0
    elif winner == 'tie':
        iteration = 0
        for _ in chips_in_play:
            iteration += 1
            chips_in_play[iteration - 1] = 0
    iteration = 0
    for _ in player_chips_in_play:
        iteration += 1
        player_chips_in_play[iteration - 1] = 0


def enemy_move(move):
    # This function controls all enemy moves and functions.
    global opponent_hand
    global enemy_chip_total
    global card_val_list
    global icard1_val
    global icard2_val
    global icard3_val
    global icard4_val
    global icard5_val
    global spade_count
    global club_count
    global diamond_count
    global heart_count
    global ecard1_val
    global ecard2_val
    global chips_in_play
    global enemy_chip_total
    global level
    global e_total
    global e_bet
    global e_bet_amount
    global sector
    global p_bet
    global choice
    global winner

    card_val_list = []
    spade_count = 0
    club_count = 0
    diamond_count = 0
    heart_count = 0

    # Based on the level certain cards are analyzed and then added to the card value list for later analysis.
    analyze_card(opponent_hand, 0, 8)
    analyze_card(opponent_hand, 1, 8)

    card_val_list.append(ecard1_val)
    card_val_list.append(ecard2_val)
    if level > 1:
        analyze_card(cards_in_play, 0, 3)
        analyze_card(cards_in_play, 1, 4)
        analyze_card(cards_in_play, 2, 5)
        card_val_list.append(icard1_val)
        card_val_list.append(icard2_val)
        card_val_list.append(icard3_val)
    if level > 2:
        analyze_card(cards_in_play, 3, 6)
        card_val_list.append(icard4_val)
    if level > 3:
        analyze_card(cards_in_play, 4, 7)
        card_val_list.append(icard5_val)
    card_val_list.sort()
    analyze_val_list(2)
    should_fold = False
    # Decides if the enemy should fold if the player bets.
    if p_bet and move == 1 and ecard1_val != ecard2_val and sector > 0 and spade_count < 2 and club_count < 2 \
            and heart_count < 2 and diamond_count < 2:
        should_fold = True
    elif p_bet and move == 2 and e_total <= 9 and sector > 0 and spade_count < 5 and club_count < 5 \
            and heart_count < 5 and diamond_count < 5:
        should_fold = True
    elif p_bet and move == 3 and e_total <= 8 and sector > 0 and spade_count < 5 and club_count < 5 \
            and heart_count < 5 and diamond_count < 5:
        should_fold = True
    elif p_bet and move == 4 and e_total <= 8 and sector > 0 and spade_count < 5 and club_count < 5 \
            and heart_count < 5 and diamond_count < 5:
        should_fold = True
    if should_fold:
        winner = 'player'
        check_winner()
        level = 6
    # This responds to the player bet by matching it.
    if not should_fold:
        if p_bet and enemy_chip_total[sector] > choice:
            enemy_chip_total[sector] -= choice
            chips_in_play[sector] += choice
            p_bet = False
        elif p_bet and (sector - 1) == 2:
            if enemy_chip_total[sector - 1] >= 3 * choice:
                enemy_chip_total[sector - 1] -= 3 * choice
                chips_in_play[sector - 1] += 3 * choice
            p_bet = False
        elif p_bet and (sector - 1) == 1:
            if enemy_chip_total[sector - 1] >= 2 * choice:
                enemy_chip_total[sector - 1] -= 2 * choice
                chips_in_play[sector - 1] += 2 * choice
            p_bet = False
        elif p_bet and (sector - 1) == 0:
            if enemy_chip_total[sector - 1] >= 5 * choice:
                enemy_chip_total[sector - 1] -= 5 * choice
                chips_in_play[sector - 1] += 5 * choice
            p_bet = False
        elif p_bet and (sector - 2) == 1:
            if enemy_chip_total[sector - 2] >= 6 * choice:
                enemy_chip_total[sector - 2] -= 6 * choice
                chips_in_play[sector - 2] += 6 * choice
            p_bet = False
        elif p_bet and (sector - 2) == 0:
            if enemy_chip_total[sector - 2] >= 10 * choice:
                enemy_chip_total[sector - 2] -= 10 * choice
                chips_in_play[sector - 2] += 10 * choice
            p_bet = False
        elif p_bet and (sector - 3) == 0:
            if enemy_chip_total[sector - 3] >= 30 * choice:
                enemy_chip_total[sector - 3] -= 30 * choice
                chips_in_play[sector - 3] += 30 * choice
            p_bet = False
        elif p_bet and (sector + 1) == 3:
            if enemy_chip_total[sector + 1] >= math.ceil(choice / 3):
                enemy_chip_total[sector + 1] -= math.ceil(choice / 3)
                chips_in_play[sector + 1] += math.ceil(choice / 3)
            p_bet = False
        elif p_bet and (sector + 1) == 2:
            if enemy_chip_total[sector + 1] >= math.ceil(choice / 2):
                enemy_chip_total[sector + 1] -= math.ceil(choice / 2)
                chips_in_play[sector + 1] += math.ceil(choice / 2)
            p_bet = False
        elif p_bet and (sector + 1) == 1:
            if enemy_chip_total[sector + 1] >= math.ceil(choice / 5):
                enemy_chip_total[sector + 1] -= math.ceil(choice / 5)
                chips_in_play[sector + 1] += math.ceil(choice / 5)
            p_bet = False
        elif p_bet and (sector + 2) == 3:
            if enemy_chip_total[sector + 2] >= math.ceil(choice / 6):
                enemy_chip_total[sector + 2] -= math.ceil(choice / 6)
                chips_in_play[sector + 2] += math.ceil(choice / 6)
            p_bet = False
        elif p_bet and (sector + 2) == 2:
            if enemy_chip_total[sector + 2] >= math.ceil(choice / 10):
                enemy_chip_total[sector + 2] -= math.ceil(choice / 10)
                chips_in_play[sector + 2] += math.ceil(choice / 10)
            p_bet = False
        elif p_bet and (sector + 3) == 3:
            if enemy_chip_total[sector + 3] >= math.ceil(choice / 30):
                enemy_chip_total[sector + 3] -= math.ceil(choice / 30)
                chips_in_play[sector + 3] += math.ceil(choice / 30)
            p_bet = False
        elif p_bet:
            it = -1
            for n in enemy_chip_total:
                it += 1
                enemy_chip_total[it] -= n
                chips_in_play[it] += n
            p_bet = False
    chips_bet = 1
    e_bet_amount = chips_bet
    # Decides if the enemy should bet or not and if so how much.
    if move == 1:
        sector = 0
        if ecard1_val == ecard2_val:
            if enemy_chip_total[0] > 0:
                chips_in_play[0] += e_bet_amount
                enemy_chip_total[0] -= e_bet_amount
                e_bet = True
        elif spade_count >= 2:
            if enemy_chip_total[0] > 0:
                chips_in_play[0] += e_bet_amount
                enemy_chip_total[0] -= e_bet_amount
                e_bet = True
        elif club_count >= 2:
            if enemy_chip_total[0] > 0:
                chips_in_play[0] += e_bet_amount
                enemy_chip_total[0] -= e_bet_amount
                e_bet = True
        elif heart_count >= 2:
            if enemy_chip_total[0] > 0:
                chips_in_play[0] += e_bet_amount
                enemy_chip_total[0] -= e_bet_amount
                e_bet = True
        elif diamond_count >= 2:
            if enemy_chip_total[0] > 0:
                chips_in_play[0] += e_bet_amount
                enemy_chip_total[0] -= e_bet_amount
                e_bet = True
    if move == 2:
        analyze_val_list(2)
        if e_total <= 4:
            if enemy_chip_total[2] > 0:
                chips_in_play[2] += e_bet_amount
                enemy_chip_total[2] -= e_bet_amount
                sector = 2
                e_bet = True
        elif e_total <= 6:
            if enemy_chip_total[1] > 0:
                chips_in_play[1] += e_bet_amount
                enemy_chip_total[1] -= e_bet_amount
                sector = 1
                e_bet = True
        elif e_total <= 9:
            if enemy_chip_total[0] > 0:
                e_bet_decision = random.randint(1, 2)
                if e_bet_decision == 1:
                    sector = 0
                    chips_in_play[0] += e_bet_amount
                    enemy_chip_total[0] -= e_bet_amount
                    e_bet = True
    if move == 3:
        analyze_val_list(2)
        if e_total <= 4:
            if enemy_chip_total[2] > 0:
                sector = 2
                chips_in_play[2] += e_bet_amount
                enemy_chip_total[2] -= e_bet_amount
                e_bet = True
        elif e_total <= 6:
            if enemy_chip_total[1] > 0:
                sector = 1
                chips_in_play[1] += e_bet_amount
                enemy_chip_total[1] -= e_bet_amount
                e_bet = True
        elif e_total <= 9:
            if enemy_chip_total[0] > 0:
                sector = 0
                e_bet_decision = random.randint(1, 2)
                if e_bet_decision == 1:
                    chips_in_play[0] += e_bet_amount
                    enemy_chip_total[0] -= e_bet_amount
                    e_bet = True
    if move == 4:
        analyze_val_list(2)
        if e_total <= 4:
            if enemy_chip_total[2] > 0:
                sector = 2
                chips_in_play[2] += e_bet_amount
                enemy_chip_total[2] -= e_bet_amount
                e_bet = True
        elif e_total <= 6:
            if enemy_chip_total[1] > 0:
                sector = 1
                chips_in_play[1] += e_bet_amount
                enemy_chip_total[1] -= e_bet_amount
                e_bet = True
        elif e_total <= 9:
            if enemy_chip_total[0] > 0:
                e_bet_decision = random.randint(1, 2)
                if e_bet_decision == 1:
                    sector = 0
                    chips_in_play[0] += e_bet_amount
                    enemy_chip_total[0] -= e_bet_amount
                    e_bet = True


start_game()

# Creates all the chips as well as clickable button.

all_sprites = pygame.sprite.Group()
chip1 = Chip(dis_width / 2 + 125, dis_height - 100, 0, all_sprites)
chip2 = Chip(dis_width / 2 + 200, dis_height - 100, 2, all_sprites)
chip3 = Chip(dis_width / 2 + 275, dis_height - 100, 3, all_sprites)
chip4 = Chip(dis_width / 2 + 350, dis_height - 100, 1, all_sprites)
fold_button = Chip(dis_width / 2 + 425, dis_height - 200, 5, all_sprites)
end_turn_button = Chip(dis_width / 2 + 425, dis_height - 100, 4, all_sprites)

level = 0
choice = 1

while playing:
    # This controls the actions conducted while playing
    count_chip_values()
    dis.fill(green)
    message1 = font4.render(f'${player_chip_value}', False, white)
    message2 = font4.render('Your Turn', False, white)
    # This controls events that occur in the program such as bets, folds, and checks.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                if i == chip1 and not e_bet:
                    typing_input(0)
                    player_chip_total[0] -= choice
                    chips_in_play[0] += choice
                    player_chips_in_play[0] += choice
                    if choice > 0:
                        p_bet = True
                        sector = 0
                if i == chip2 and not e_bet:
                    typing_input(1)
                    player_chip_total[1] -= choice
                    chips_in_play[1] += choice
                    player_chips_in_play[1] += choice
                    if choice > 0:
                        p_bet = True
                        sector = 1
                if i == chip3 and not e_bet:
                    typing_input(2)
                    player_chip_total[2] -= choice
                    chips_in_play[2] += choice
                    player_chips_in_play[2] += choice
                    if choice > 0:
                        p_bet = True
                        sector = 2

                if i == chip4 and not e_bet:
                    typing_input(3)
                    player_chip_total[3] -= choice
                    chips_in_play[3] += choice
                    player_chips_in_play[3] += choice
                    if choice > 0:
                        p_bet = True
                        sector = 3

                if i == end_turn_button:
                    player_turn = False
                    if e_bet:
                        chips_in_play[sector] += e_bet_amount
                        player_chip_total[sector] -= e_bet_amount
                        player_chips_in_play[sector] += e_bet_amount
                        e_bet = False
                        player_turn = True
                        level += 1
                if i == fold_button:
                    e_bet_amount = 0
                    winner = 'enemy'
                    check_winner()
                    level = 6
    # Initiates enemy moves as well as the needed reactions to the enemy move. Also controls the reactions needed based
    # on the level of the game.
    if level == 0 and not player_turn:
        enemy_move(1)
        if not e_bet:
            level += 1
        player_turn = True
    if level == 1 and not player_turn:
        enemy_move(2)
        if not e_bet:
            level += 1
        player_turn = True
    if level == 2 and not player_turn:
        enemy_move(3)
        if not e_bet:
            level += 1
        player_turn = True
    if level == 3 and not player_turn:
        enemy_move(4)
        if not e_bet:
            level += 1
        player_turn = True
    if level == 7:
        pygame.time.wait(5000)
        player_turn = True
        start_game()
    if level == 6:
        level += 1
    if level == 5:
        pygame.time.wait(5000)
        start_game()
    if level == 4:
        analyze_hands()
        player_turn = True

        level += 1

    update_dis()
    clock.tick(60)

# Closes the window after the program is run
pygame.quit()
