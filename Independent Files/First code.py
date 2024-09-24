import random

def tictactoe_game():
   running = True
   while running:
       norow = True
       one = "_"
       two = "_"
       three = "_"
       four = "_"
       five = "_"
       six = "_"
       seven = " "
       eight = " "
       nine = " "
       end = 0
       xmove = ''
       omove = ''
       board_posibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
       def gameboard():
           print("_" + one + "_|_" + two + "_|_" + three + "_")
           print("_" + four + "_|_" + five + "_|_" + six + "_")
           print(" " + seven + " | " + eight + " | " + nine)
       print("TIC TAC TOE")
       answer = input("Do you want instructions? If so, type yes: ")
       if answer == "yes":
           print("~~~Instructions~~~")
           print("The first person will be X and the second will be O")
           print("In order to pick where you want the x or o to go, you have to type a certain number.")
           print("So its a grid like this, you type the number that corresponds to that grid slot.")
           print("_1_|_2_|_3_")
           print("_4_|_5_|_6_")
           print(" 7 | 8 | 9 ")
           print("DO NOT USE THE SAME NUMBER TWICE")
       while norow:
           xmove = random.choice(board_posibilities)
           print('X MOVE')
           if xmove == 1 and one == '_':
               one = "x"
               board_posibilities.remove(1)
           elif xmove == 2 and two == '_':
               two = "x"
               board_posibilities.remove(2)
           elif xmove > 9:
               print("Invalid")
               norow = False
           elif xmove < 1:
               print("Invalid")
               norow = False
           elif xmove == 3 and three == '_':
               three = "x"
               board_posibilities.remove(3)
           elif xmove == 4 and four == '_':
               four = "x"
               board_posibilities.remove(4)
           elif xmove == 5 and five == '_':
               five = "x"
               board_posibilities.remove(5)
           elif xmove == 6 and six == '_':
               six = "x"
               board_posibilities.remove(6)
           elif xmove == 7 and seven == ' ':
               seven = "x"
               board_posibilities.remove(7)
           elif xmove == 8 and eight == ' ':
               eight = "x"
               board_posibilities.remove(8)
           elif xmove == 9 and nine == ' ':
               nine = "x"
               board_posibilities.remove(1)
           end += 1
           gameboard()
           if one == "x" and two == "x" and three == "x":
               print("X WINS!")
               norow = False
           elif one == "x" and four == "x" and seven == "x":
               print("X WINS!")
               norow = False
           elif one == "x" and five == "x" and nine == "x":
               print("X WINS!")
               norow = False
           elif two == "x" and five == "x" and eight == "x":
               print("X WINS!")
               norow = False
           elif three == "x" and six == "x" and nine == "x":
               print("X WINS!")
               norow = False
           elif three == "x" and five == "x" and seven == "x":
               print("X WINS!")
               norow = False
           elif four == "x" and five == "x" and six == "x":
               print("X WINS!")
               norow = False
           elif seven == "x" and eight == "x" and nine == "x":
               print("X WINS!")
               norow = False
           if end == 9:
               print("TIE")
               norow = False
           if norow:
               omove = int(input("O Choose a Space: "))
               if omove == 1 and one == '_':
                   one = 'o'
               elif omove == 2 and two == '_':
                   two = "o"
               elif omove > 9:
                   print("Invalid")
                   norow = False
               elif xmove < 1:
                   print("Invalid")
                   norow = False
               elif omove == 3 and three == '_':
                   three = "o"
               elif omove == 4 and four == '_':
                   four = "o"
               elif omove == 5 and five == '_':
                   five = "o"
               elif omove == 6 and six == '_':
                   six = "o"
               elif omove == 7 and seven == ' ':
                   seven = "o"
               elif omove == 8 and eight == ' ':
                   eight = "o"
               elif omove == 9 and nine == ' ':
                   nine = "o"
               board_posibilities.remove(omove)
               end += 1
               gameboard()
               if one == "o" and two == "o" and three == "o":
                   print("O WINS!")
                   norow = False
               elif one == "o" and four == "o" and seven == "o":
                   print("O WINS!")
                   norow = False
               elif one == "o" and five == "o" and nine == "o":
                   print("O WINS!")
                   norow = False
               elif two == "o" and five == "o" and eight == "o":
                   print("O WINS!")
                   norow = False
               elif three == "o" and six == "o" and nine == "o":
                   print("O WINS!")
                   norow = False
               elif three == "o" and five == "o" and seven == "o":
                   print("O WINS!")
                   norow = False
               elif four == "o" and five == "o" and six == "o":
                   print("O WINS!")
                   norow = False
               elif seven == "o" and eight == "o" and nine == "o":
                   print("O WINS!")
                   norow = False
               if end == 9:
                   print("TIE")
                   norow = False
       again = input('Would you like to play again? If so type yes: ')
       if again == "yes":
           running = True
       else:
           running = False
tictactoe_game()
