
board_global = [1,2,3,4,5,6,7,8,9]

# board:
def board_status(board):
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print("-----------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("-----------------")
    print(" ", board[0], " | ", board[1], " | ", board[2])

# print on the board what number did player choose:
def player_what_number(player_pick, board_1, player):
    for i in range(len(board_1)):
        if player_pick == board_1[i] and type(board_1[i]) is int:
            if player == "player1":               
                board_1[i] = "x"
            else:
                board_1[i] = "o"

# when a player wins:
def player_wins(board_globalwin, player, sign): 
    if board_globalwin[0] == sign and board_globalwin[1] == sign and board_globalwin[2] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[3] == sign and board_globalwin[4] == sign and board_globalwin[5] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[6] == sign and board_globalwin[7] == sign and board_globalwin[8] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[0] == sign and board_globalwin[3] == sign and board_globalwin[6] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[1] == sign and board_globalwin[4] == sign and board_globalwin[7] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[2] == sign and board_globalwin[5] == sign and board_globalwin[8] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[2] == sign and board_globalwin[4] == sign and board_globalwin[6] == sign:
        print(player, "won!")
        return 1
    elif board_globalwin[0] == sign and board_globalwin[4] == sign and board_globalwin[8] == sign:
        print(player, "won!")
        return 1

board_status(board_global)
while True:
    #player 01 picks a number
    player_01_location = int(input("Player1: Use your numerical keyboard to pick a location: "))
    player_what_number(player_01_location, board_global, "player1")
    board_status(board_global)
    if player_wins(board_global, "player1", "x") == 1:
        break
    #player 2 picks a number
    player_02_location = int(input("Player2: Use your numerical keyboard to pick a location: "))
    player_what_number(player_02_location, board_global, "player2")
    board_status(board_global)
    if player_wins(board_global, "player2", "o") == 1:
        break


