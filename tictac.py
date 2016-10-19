
board_global = [1,2,3,4,5,6,7,8,9]

# board
def board_status(board):
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print("-----------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("-----------------")
    print(" ", board[0], " | ", board[1], " | ", board[2])

#what number did player 1 choose
def player__what_number(player__pick, board_1, player):
    for i in range(len(board_1)):
        if player__pick == board_1[i] and type(board_1[i]) is int:
            if player == "player1":               
                board_1[i] = "x"
            else:
                board_1[i] = "o"
        #else:
        #    print("1-9 please, choose an empty place")


def player_01_wins(board_globalwin): 
    if board_globalwin[0] == "x" and board_globalwin[1] == "x" and board_globalwin[2] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[3] == "x" and board_globalwin[4] == "x" and board_globalwin[5] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[6] == "x" and board_globalwin[7] == "x" and board_globalwin[8] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[0] == "x" and board_globalwin[3] == "x" and board_globalwin[6] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[1] == "x" and board_globalwin[4] == "x" and board_globalwin[7] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[2] == "x" and board_globalwin[5] == "x" and board_globalwin[8] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[2] == "x" and board_globalwin[4] == "x" and board_globalwin[6] == "x":
        print("Player1 won!")
        return 1
    elif board_globalwin[0] == "x" and board_globalwin[4] == "x" and board_globalwin[8] == "x":
        print("Player1 won!")
        return 1

while True:
    board_status(board_global)
    #player 01 picks a number
    player_01_location = int(input("Player1: Use your numerical keyboard to pick a location: "))
    player__what_number(player_01_location, board_global, "player1")
    board_status(board_global)
    if player_01_wins(board_global) == 1:
        break
    #player 2 picks a number
    player_02_location = int(input("Player2: Use your numerical keyboard to pick a location: "))
    player__what_number(player_02_location, board_global, "player2")



