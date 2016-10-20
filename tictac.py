
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
        

board_status(board_global)
while True:
    #player 01 picks a number  
    try:
        player_01_location = int(input("Player1: Use your numerical keyboard to pick a location: "))    
        pass
    except ValueError:
        print("1-9 please!")
        continue
    if player_01_location > 9 or player_01_location < 1:
        print("1-9 please!")
        continue
    
    #modify board
    if player_what_number(player_01_location, board_global, "player1") == False:
        print("Please choose a free slot!")
        continue
    #print board
    board_status(board_global)
    #check if player won or game is draw
    if player_wins(board_global, "player1", "x") == True or board_is_full() == True:
        break
    

    x = 1
    while x == 1:           
        try:
            #player 2 picks a number
            player_02_location = int(input("Player2: Use your numerical keyboard to pick a location: "))    
            if player_02_location > 9 or player_02_location < 1:
                print("1-9 please!")
                continue
            else:
                #player 2 changes board
                if player_what_number(player_02_location, board_global, "player2") == False:
                    print("Please choose a free slot!")
                    continue
                x = 2
        except ValueError:
            print("1-9 please!")
            continue        
    
    #print board
    board_status(board_global)
    #check if player won
    if player_wins(board_global, "player2", "o") == True or board_is_full() == True:
        break
    