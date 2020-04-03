print(" *** TIC TAC TOE *** ")

# ******Global Variables******

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# if game still going
game_is_still_going = True

# who won? or tie?
winner = None

# who's turn is this?
current_player = "X"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

def play_game():
    # to display the initial board
    display_board()

    # while the game is still going
    while game_is_still_going:

        # handle a single turn of a player
        handle_turn(current_player)

        # check if the game has ended
        check_game_over()

        # fil to the next player
        flip_player()

        # The game has ended

    if winner=="X" or winner=="O":
            print("********* "+ winner + " is the winner *********")
    elif winner == None:
            print("*** The match is tie ***")




def check_game_over():
    check_for_winner()
    check_tie()


def check_for_winner():

    # set global variable winner
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():

    # set a global variable
    global game_is_still_going

    # checking rows are equal or not
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_still_going = False

    # return winner X 0r O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set a global variable
    global game_is_still_going

    # checking columns are equal or not
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"


    if column_1 or column_2 or column_3:
        game_is_still_going = False

    # return winner X 0r O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set a global variable
    global game_is_still_going

    # checking diagonals are equal or not
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_is_still_going = False

    # return winner X 0r O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return


def check_tie():

    # set a global variable
    global game_is_still_going

    # checking for tie
    if "-" not in board:
        game_is_still_going = False
    return


def flip_player():

    # set a global variable
    global current_player

    # flip the turn from "X" to "O" and from "O" to "X"
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return



def handle_turn(player):

    print("*** " + player + "'s turn. ***")
    position = input("choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, please choose a position from 1 to 9: ")


        position = int(position) - 1

        if board [position] == "-":
            valid = True
        else:
            print(" ***over writing is not possible*** ")

    board[position] = player

    display_board()


play_game()

