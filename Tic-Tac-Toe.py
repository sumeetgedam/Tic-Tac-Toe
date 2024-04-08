import random


def scroll_window():
    print('\n')

def display_board(board):
    scroll_window()
    print("Board now:")
    for row in board:
        for item in row:
            print('|' + item + '|', end='')
        print()

def choose_first():
    return random.randint(1, 2)

def player_input():
    marker = ''
    while True:
        marker = input("Player 1 : Pick a marker 'X' or 'O' only: ")
        if marker.lower() in ['x', 'o']:
            break
        else:
            print("Please pick a marker out of X or O capital alphabets only")
    return ('X','O') if marker.lower() == 'x' else ('O', 'X')

def place_marker(board, marker, row, col):
    board[row-1][col-1] = marker
    # print("board was marked with "+ marker + " at location ("+str(row)+','+str(col)+")")

def win_check(board, mark):
    return (
        (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or
        (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark) or
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark)
    )

def space_check(board, row, col):
    return board[row-1][col-1] == ' '


def full_board_check(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if space_check(board, row, col):
                return False
        
    return True


def player_choice(board):
    while True:
        temp_position = list(map(int,input("Enter row col ( without space ) where you want to place your marker: ")))
        if len(temp_position) != 2:
            print("invalid location or that location is already filled ,Please enter a valid pair of row, col looking at the board.")
        else:
            if temp_position[0] not in [1, 2, 3] or temp_position[1] not in [1, 2, 3] or not space_check(board, temp_position[0], temp_position[1]):
                print("invalid location or that location is already filled ,Please enter a valid pair of row, col looking at the board.")
            else:
                break

    row, col = temp_position     
    return [row, col]

def replay():
    while True:
        play_again = input("Do you want to play again ? (Yes/No): ")
        if len(play_again) != 0 and play_again.lower() in ['yes', 'no']:
            break

    
    return True if play_again.lower().startswith('y') else False



print("Welcome! let's play a game of Tic Tac Toe:\n")

while True:
    test_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    player_1_marker, player_2_marker = player_input()
    turn = choose_first()
    print("Player "+str(turn)+" will go first")

    play_game = input("ready to play ? Yes/No. ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:

        if turn == 1:
            display_board(test_board)
            print("Player 1 Enter your positions : ")
            position_1, position_2 = player_choice(test_board)
            place_marker(test_board, player_1_marker, position_1, position_2)

            if win_check(test_board, player_1_marker):
                display_board(test_board)
                print("Congrats! You won the game")
                break
            else:
                turn = 2
        else:
            display_board(test_board)
            print("Player 2 Enter your position :")
            position_1, position_2 = player_choice(test_board)
            place_marker(test_board, player_2_marker, position_1, position_2)
            
            if win_check(test_board, player_2_marker):
                display_board(test_board)
                print("Player 2 has Won")
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("the game is draw")
                    break
                else:
                    turn  = 1
    
    if not replay():
        break