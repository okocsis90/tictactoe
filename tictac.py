
board_global = [1,2,3,4,5,6,7,8,9]

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
    if board[player_pick] == "x" or board[player_pick] == "o":
        return False
    else:
        if player == "player1":               
            board[player_pick] = "x"
        else:
            board[player_pick] = "o"
    return True

# when a player wins:
def player_wins(board_globalwin, player, sign): 
    if board_globalwin[0] == sign and board_globalwin[1] == sign and board_globalwin[2] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[3] == sign and board_globalwin[4] == sign and board_globalwin[5] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[6] == sign and board_globalwin[7] == sign and board_globalwin[8] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[0] == sign and board_globalwin[3] == sign and board_globalwin[6] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[1] == sign and board_globalwin[4] == sign and board_globalwin[7] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[2] == sign and board_globalwin[5] == sign and board_globalwin[8] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[2] == sign and board_globalwin[4] == sign and board_globalwin[6] == sign:
        print(player, "won!")
        return True
    elif board_globalwin[0] == sign and board_globalwin[4] == sign and board_globalwin[8] == sign:
        print(player, "won!")
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
 
board_status(board_global)
counter_global = 0
player_X_location = 0

while True:

    # player picks a number and examine if it is a proper choice
    try:
        if counter_global % 2 == 0:
            player_X_location = player_picks_location(player_X_location, "player1")        
        elif counter_global % 2 != 0:
            player_X_location = player_picks_location(player_X_location, "player2")            
    except ValueError:
        print("1-9 please!")
        continue
    if player_X_location > 9 or player_X_location < 1:
        print("1-9 please!")
        continue
  
    # modify board
    if counter_global % 2 == 0:
        if player_what_number(player_X_location, board_global, "player1") == False:
            print("Please choose a free slot!")
            continue       
    elif counter_global % 2 != 0:
        if player_what_number(player_X_location, board_global, "player2") == False:
            print("Please choose a free slot!")
            continue
           
    # print board
    board_status(board_global)

    # check if player won or game is draw
    if player_wins(board_global, "player1", "x") == True or player_wins(board_global, "player2", "o") == True or board_is_full() == True:
        break
    # set the counter
    counter_global += 1
    
