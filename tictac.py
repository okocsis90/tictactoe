
board_global = [7, 8, 9, 4, 5, 6, 1, 2, 3]

# board
def board_status(board):
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print("-----------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("-----------------")
    print(" ", board[6], " | ", board[7], " | ", board[8])

#what number did player 1 choose
def player_01_what_number(player_01_pick, board_1):
    if player_01_pick == 1:
        board_1[6]="x"
    elif player_01_pick == 2:
        board_1[7]="x"
    elif player_01_pick == 3:
        board_1[8]="x"
    elif player_01_pick == 4:
        board_1[3]="x"
    elif player_01_pick == 5:
        board_1[4]="x"
    elif player_01_pick == 6:
        board_1[5]="x"
    elif player_01_pick == 7:
        board_1[0]="x"
    elif player_01_pick == 8:
        board_1[1]="x"
    elif player_01_pick == 9:
        board_1[2]="x"
    else:
        print("1-9 please")

#what did player 2 choose
def player_02_what_number(player_02_pick, board_1):
    if player_02_pick == 1:
        board_1[6]="o"
    elif player_02_pick == 2:
        board_1[7]="o"
    elif player_02_pick == 3:
        board_1[8]="o"
    elif player_02_pick == 4:
        board_1[3]="o"
    elif player_02_pick == 5:
        board_1[4]="o"
    elif player_02_pick == 6:
        board_1[5]="o"
    elif player_02_pick == 7:
        board_1[0]="o"
    elif player_02_pick == 8:
        board_1[1]="o"
    elif player_02_pick == 9:
        board_1[2]="o"
    else:
        print("1-9 please")

def player_01_wins(board_globalwin): 
    if board_globalwin[0] and board_globalwin[1] and board_globalwin[2] == "x":
        print("Player1 won!")
    elif board_globalwin[3] and board_globalwin[4] and board_globalwin[5] == "x":
        print("Player1 won!")
    elif board_globalwin[6] and board_globalwin[7] and board_globalwin[8] == "x":
        print("Player1 won!")

while True:
    board_status(board_global)
    #player 01 picks a number
    player_01_location = int(input("Player1: Use your numerical keyboard to pick a location: "))
    player_01_what_number(player_01_location, board_global)
    board_status(board_global)
    player_01_wins(board_global)
    #player 2 picks a number
    player_02_location = int(input("Player2: Use your numerical keyboard to pick a location: "))
    player_02_what_number(player_02_location, board_global)
    
    
