import random
import pygame

pygame.init()

dis_width = 1000
dis_height = 690
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()
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
gray = (50, 50, 50)
gray2 = (100, 100, 100)


def gameloop():
    # INITIAL VARIABLES
    # Lists, variables, word list, etc

    word_possibilities = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player',
                          'condition', 'reverse', 'water', 'board', 'geeks', ]
    # word_possibilities = ['YOUR WORD']
    word = random.choice(word_possibilities)
    running = 0
    progress = 0
    correct = 61
    incorrect = 61
    word_list = []
    for position in range(len(word)):
        word_list.append(word[position])
    incorrect_list = []
    presenting_list = []

    # This determines the amount of slots/letters needed in the preesenting list

    for letter_count in range(len(word)):
        presenting_list.append('_')
    del presenting_list[len(word):]

    # The main program starts by asking for a guess and checking if it is in the word

    # print('HANGMAN')
    while running < 6:
        dis.fill(black)
        hangman_mesg = font2.render('Hangman', True, white)
        simplified_presenting_list = ''
        simplified_incorrect_list = ''
        for letter in presenting_list:
            simplified_presenting_list = simplified_presenting_list + f' {letter} '
        presenting_mesg = font2.render(f'{simplified_presenting_list}', True, white)
        for letter in incorrect_list:
            simplified_incorrect_list = simplified_incorrect_list + f' {letter} '
        incorrect_guesses_mesg = font2.render(f'Incorrect guesses {simplified_incorrect_list}', True, white)
        correct_mesg = font2.render('Correct', True, green)
        incorrect_mesg = font2.render('Incorrect', True, red)

        dis.blit(incorrect_guesses_mesg, [300, 500])
        dis.blit(presenting_mesg, [440 - len(presenting_list) * 10, 400])
        dis.blit(hangman_mesg, [435, 100])

        if correct < 1:
            dis.blit(correct_mesg, [450, 150])
        if incorrect < 1 and correct != 0:
            dis.blit(incorrect_mesg, [450, 150])

        lose_mesg = font1.render('You Lose', True, red)
        win_mesg = font1.render('You Win', True, green)
        pygame.draw.line(dis, white, (800, 60), (870, 30), 5)
        pygame.draw.line(dis, white, (870, 30), (940, 60), 5)
        pygame.draw.line(dis, white, (940, 60), (940, 400), 5)
        pygame.draw.line(dis, white, (870, 400), (1000, 400), 5)
        if running >= 1 and running != 11:
            pygame.draw.circle(dis, white, (800, 100), 40)
        if running >= 2 and running != 11:
            pygame.draw.line(dis, white, (800, 100), (800, 250), 5)
        if running >= 3 and running != 11:
            pygame.draw.line(dis, white, (800, 250), (850, 350), 5)
        if running >= 4 and running != 11:
            pygame.draw.line(dis, white, (750, 350), (800, 250), 5)
        if running >= 5 and running != 11:
            pygame.draw.line(dis, white, (750, 200), (800, 150), 5)
        if running >= 6 and running != 11:
            pygame.draw.line(dis, white, (800, 150), (850, 200), 5)

        pygame.display.flip()
        dis.fill(black)
        correct += 1
        incorrect += 1
        simplified_incorrect_list = ''
        simplified_presenting_list = ''

        def lose_message():
            losing = 0
            while losing < 300:
                pygame.draw.line(dis, white, (800, 60), (870, 30), 5)
                pygame.draw.line(dis, white, (870, 30), (940, 60), 5)
                pygame.draw.line(dis, white, (940, 60), (940, 400), 5)
                pygame.draw.line(dis, white, (870, 400), (1000, 400), 5)
                if running >= 1 and running != 11:
                    pygame.draw.circle(dis, white, (800, 100), 40)
                if running >= 2 and running != 11:
                    pygame.draw.line(dis, white, (800, 100), (800, 250), 5)
                if running >= 3 and running != 11:
                    pygame.draw.line(dis, white, (800, 250), (850, 350), 5)
                if running >= 4 and running != 11:
                    pygame.draw.line(dis, white, (750, 350), (800, 250), 5)
                if running >= 5 and running != 11:
                    pygame.draw.line(dis, white, (750, 200), (800, 150), 5)
                if running >= 6 and running != 11:
                    pygame.draw.line(dis, white, (800, 150), (850, 200), 5)
                losing += 1
                dis.blit(lose_mesg, [50, 200])
                pygame.display.flip()

        def win_message():
            win = 0
            while win < 300:
                pygame.draw.line(dis, white, (800, 60), (870, 30), 5)
                pygame.draw.line(dis, white, (870, 30), (940, 60), 5)
                pygame.draw.line(dis, white, (940, 60), (940, 400), 5)
                pygame.draw.line(dis, white, (870, 400), (1000, 400), 5)
                if running >= 1 and running != 11:
                    pygame.draw.circle(dis, white, (800, 100), 40)
                if running >= 2 and running != 11:
                    pygame.draw.line(dis, white, (800, 100), (800, 250), 5)
                if running >= 3 and running != 11:
                    pygame.draw.line(dis, white, (800, 250), (850, 350), 5)
                if running >= 4 and running != 11:
                    pygame.draw.line(dis, white, (750, 350), (800, 250), 5)
                if running >= 5 and running != 11:
                    pygame.draw.line(dis, white, (750, 200), (800, 150), 5)
                if running >= 6 and running != 11:
                    pygame.draw.line(dis, white, (800, 150), (850, 200), 5)
                dis.blit(win_mesg, [100, 200])
                win += 1
                pygame.display.flip()

        # guess = input('Guess a letter: ')
        inputting = True
        while inputting:
            event = pygame.event.poll()
            # keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)  # Returns string id of pressed key.

                if len(key) == 1:  # This covers all letters and numbers not on numpad.
                    # guess = key
                    for letter in word_list:
                        print(key)
                        if key == letter:
                            letter_index = word_list.index(letter)
                            word_list[letter_index] = '_'
                            presenting_list[letter_index] = key
                            progress += 1
                            correct = 0
                            inputting = False
                        elif key != letter:
                            incorrect = 0

                    if incorrect == 0 and correct != 0:
                        incorrect_list.append(key)
                        inputting = False
                # thing = 1

        # This prints if you are correct or incorrect and adds incorrect guesses to the incorrect list
        # dis.blit(dis, (100, 100))
        # pygame.display.flip()

        # This controls the end the program by printing win or lose then ending the program
        if correct < 1:
            dis.blit(correct_mesg, [450, 150])
        if incorrect < 1 and correct != 0:
            dis.blit(incorrect_mesg, [450, 150])
            running += 1
        for letter in incorrect_list:
            simplified_incorrect_list = simplified_incorrect_list + f' {letter} '
        incorrect_guesses_mesg = font2.render(f'Incorrect guesses {simplified_incorrect_list}', True, white)
        dis.blit(incorrect_guesses_mesg, [300, 500])
        for letter in presenting_list:
            simplified_presenting_list = simplified_presenting_list + f' {letter} '
        presenting_mesg = font2.render(f'{simplified_presenting_list}', True, white)
        dis.blit(presenting_mesg, [440 - len(presenting_list) * 10, 400])
        dis.blit(hangman_mesg, [435, 100])
        if progress == len(word):
            win_message()
            running = 11
        if running == 6:
            lose_message()
        lose_mesg = font1.render('You Lose', True, red)
        win_mesg = font1.render('You Win', True, green)
        pygame.draw.line(dis, white, (800, 60), (870, 30), 5)
        pygame.draw.line(dis, white, (870, 30), (940, 60), 5)
        pygame.draw.line(dis, white, (940, 60), (940, 400), 5)
        pygame.draw.line(dis, white, (870, 400), (1000, 400), 5)
        if running >= 1 and running != 11:
            pygame.draw.circle(dis, white, (800, 100), 40)
        if running >= 2 and running != 11:
            pygame.draw.line(dis, white, (800, 100), (800, 250), 5)
        if running >= 3 and running != 11:
            pygame.draw.line(dis, white, (800, 250), (850, 350), 5)
        if running >= 4 and running != 11:
            pygame.draw.line(dis, white, (750, 350), (800, 250), 5)
        if running >= 5 and running != 11:
            pygame.draw.line(dis, white, (750, 200), (800, 150), 5)
        if running >= 6 and running != 11:
            pygame.draw.line(dis, white, (800, 150), (850, 200), 5)
        pygame.display.flip()
        clock.tick(60)


gameloop()
pygame.quit()