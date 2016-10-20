
board_global = [1,2,3,4,5,6,7,8,9]
import random

# board:
def board_status(board):
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print("-----------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("-----------------")
    print(" ", board[0], " | ", board[1], " | ", board[2])

# print on the board what number did player choose:
def player_what_number(player_pick, board, player):
    player_pick = player_pick - 1
    if board[player_pick] == "\033[93m" + "\033[1m" + "x" + "\033[0m" or board[player_pick] == "\033[91m" + "\033[1m" + "o" + "\033[0m":
        return False
    else:
        if player == "player1":               
            board[player_pick] = "\033[93m" + "\033[1m" + "x" + "\033[0m"
        else:
            board[player_pick] = "\033[91m" + "\033[1m" + "o" + "\033[0m"
    return True

# when a player wins:
def player_wins(board_globalwin, sign): 
    if ((board_globalwin[0] == sign and board_globalwin[1] == sign and board_globalwin[2] == sign) or
       (board_globalwin[3] == sign and board_globalwin[4] == sign and board_globalwin[5] == sign) or
       (board_globalwin[6] == sign and board_globalwin[7] == sign and board_globalwin[8] == sign) or
       (board_globalwin[0] == sign and board_globalwin[3] == sign and board_globalwin[6] == sign) or
       (board_globalwin[1] == sign and board_globalwin[4] == sign and board_globalwin[7] == sign) or
       (board_globalwin[2] == sign and board_globalwin[5] == sign and board_globalwin[8] == sign) or
       (board_globalwin[2] == sign and board_globalwin[4] == sign and board_globalwin[6] == sign) or
       (board_globalwin[0] == sign and board_globalwin[4] == sign and board_globalwin[8] == sign)):
        return True

# when draw
def board_is_full():
    if all(isinstance(i, str) for i in board_global):
        print("It's a draw!")
        return True
        
# player picks number
def player_picks_location(player_location, player):
        print(player, end="")
        player_location = int(input(" : Use your numerical keyboard to pick a location: "))
        return player_location
 
# AI picks location
def computer_picks_location(board):
    choose = random.randrange(10) 
    if board[choose - 1] == "\033[93m" + "\033[1m" + "x" + "\033[0m" or board[choose - 1] == "\033[91m" + "\033[1m" + "o" + "\033[0m":
        return False
    else:
        board[choose - 1] = "\033[91m" + "\033[1m" + "o" + "\033[0m"
    return True

# This function returns True if the player wants to play again, otherwise it returns False.
def playAgain():
    play_again = " "
    while not (play_again == "y" or play_again == "n"):
        play_again = input("Do you want to play again? (y or n): ")
    if play_again == "y":
        return True
    else:
        return False

# player chooses if he wants to play with AI or Human
def choose_mode():
    mode = " "
    while not (mode == "a" or mode == "h"):
        mode = input("For AI opponent press a, for Human opponent press h: ")
    if mode == "a":
        return "a"
    else:
        return "h"   

# game starts, menu
print("__          __  _                           ")
print("\ \        / / | |                          ")
print(" \ \  /\  / /__| | ___ ___  _ __ ___   ___  ")
print("  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
print("   \  /\  /  __/ | (_| (_) | | | | | |  __/ ")
print("    \/  \/ \___|_|\___\___/|_| |_| |_|\___|")
if choose_mode() == "a":
    choose_mode = "ai"
else:
    choose_mode = "human"
board_status(board_global)
counter_global = 0
player_X_location = 0

while True:
    # check if player 1 or player 2 or AI
    if counter_global % 2 == 0:
        player = "player1"
        sign = "\033[93m" + "\033[1m" + "x" + "\033[0m"
    else:
        if choose_mode == "human":
            player = "player2"     
        elif choose_mode == "ai":
            player = "Computer"
        sign = "\033[91m" + "\033[1m" + "o" + "\033[0m"

    # player picks a number and examine if it is a proper choice in Human mode
    if choose_mode == "human":
        try:
            player_X_location = player_picks_location(player_X_location, player)           
        except ValueError:
            print("1-9 please!")
            continue
        if player_X_location > 9 or player_X_location < 1:
            print("1-9 please!")
            continue
        
        # modify board
        if player_what_number(player_X_location, board_global, player) == False:
            print("Please choose a free slot!")
            continue       
    
    # player / AI picks a number
    elif choose_mode == "ai":
        if player == "player1":
            try:
                player_X_location = player_picks_location(player_X_location, player)           
            except ValueError:
                print("1-9 please!")
                continue
            if player_X_location > 9 or player_X_location < 1:
                print("1-9 please!")
                continue
            
            # modify board
            if player_what_number(player_X_location, board_global, player) == False:
                print("Please choose a free slot!")
                continue   
        else:
            if computer_picks_location(board_global) == False:
                continue
            print("Computer: ")
    
    # print board
    board_status(board_global)

    # check if player won or game is draw
    if player_wins(board_global, sign) == True:
        print(player, "won!")
        board_global = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if playAgain() == True:
            board_status(board_global)
            continue
        else:
            break

    if board_is_full() == True:
        board_global = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if playAgain() == True:
            board_status(board_global)
            continue
        else:
            break

    # set the counter
    counter_global += 1

        