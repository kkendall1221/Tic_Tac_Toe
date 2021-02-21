# Kaleb Kendall
# January 2021


# ---global vairables----

# if game is still going
if __name__ == '__main__':
    print("Welcome to tic tac toe")

Stop_playing = False
game_still_going = True

# who won or tie
Winner = None
# who's turn is it
current_player = "X"

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# displayes board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# main game loop
def play_game():
    global game_still_going
    global board

    # display initial board
    display_board()
    while game_still_going:
        # handles a single turn of an arbitrary player

        handle_turn(current_player)
        # check if game has ended

        check_if_game_over()

        # flip to other player
        flip_player()

    # the game has ended
    if Winner == "X" or Winner == "O":
        print(Winner + " won. ")
    elif Winner is None:
        print("tie.")

    ready_to_Quit = input(" would you like to play again Yes or No?  ").lower()
    if ready_to_Quit != "no":
        print(" sorry were done")
        # clear board
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

    else:
        print("thanks for playing")
    game_still_going = False


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global Winner
    # check rows
    rows_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagoanl_winner = check_diagonals()

    if rows_winner:
        Winner = rows_winner

    elif column_winner:
        Winner = column_winner

    elif diagoanl_winner:
        Winner = diagoanl_winner

    else:
        Winner = None

    return


def check_rows():
    # set up global variables
    global game_still_going
    # check if rows have same value

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[8] == board[7] == board[6] != "-"
    # if any row does have a match then there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
        # return the winner( X or o)
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    # check if columns have same value

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if any row does have a match then there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
        # return the winner( X or o)
        if col_1:
            return board[0]
        elif col_2:
            return board[1]
        elif col_3:
            return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    # check if columns have same value

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    # if any diagonals does have a match then there is a win
    if diag_1 or diag_2:
        game_still_going = False
        # return the winner( X or o)
        if diag_1:
            return board[0]
        elif diag_2:
            return board[2]
    return


def flip_player():
    # change current player to other symbol
    global current_player
    if current_player == "X":
        current_player = "O"
        # if player was O change back to X
    elif current_player == "O":
        current_player = "X"
    return


def handle_turn(player):
    print(player + "'s turn")
    position = input("choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(" invalid input please put a number from 1 through 9   ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print(" you cant go there")

    board[position] = player

    display_board()


def check_if_tie():
    if "-" not in board:
        print("it is a tie, game over")
    return


play_game()
