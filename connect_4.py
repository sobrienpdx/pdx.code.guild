# CONNECT FOUR
# LAB: CONNECT FOUR
# Connect Four is a board game.
# Players take turns placing tokens of their color into a vertical grid.
# They drop to the bottom, and if anyone has four of their color in a straight line, they’ve won!
#
# Create a program that simulates the just playing moves of an existing Connect Four game.
# Do not concern yourself with figuring out who has won.
#
# It will read a file that contains a history of the moves in a game.
# Assume the playing board is made of columns numbered 1 through 7.
# The file will have one line for each move (players alternate).
# The number in that line is the column the current player placed a token in.
#
# Use the following example move file.
# Save it in something like connect-four-moves.txt
# This moves file recreates this game.
#
# Think about how to figure out how far that token will fall in a given column.
#
# Think about how to place a token in a column.
#
# Think about how to concisely store the tokens that have been dropped in the board.
#
# Read in moves from the file.
#
# After each move, print out a representation of the board.
# You can use R and Y to represent the pieces.
#
# ADVANCED
# Once all moves are done, also print out what player, if any, won.





row1 = [" ", " ", " ", " ", " ", " ", " ", ]
row2 = [" ", " ", " ", " ", " ", " ", " ", ]
row3 = [" ", " ", " ", " ", " ", " ", " ", ]
row4 = [" ", " ", " ", " ", " ", " ", " ", ]
row5 = [" ", " ", " ", " ", " ", " ", " ", ]
row6 = [" ", " ", " ", " ", " ", " ", " ", ]
row7 = [" ", " ", " ", " ", " ", " ", " ", ]
row_names = [row1, row2, row3, row4, row5, row6, row7]

def did_ya_win_across(row_number, player):
    for index, marker in enumerate(row_number):
        if marker == player:
            try:
                if (row1[index +1] == player) and (row1[index +2] == player):
                    print("Player {} wins!".format(player))
                    break
            except IndexError:
                continue
def check_column(column_number, player):
    if row1[column_number] == player:
        try:
            if (row2[column_number] == player) and (row3[column_number] == player):
                print("Player {} wins!".format(player))
        except IndexError:
            pass
    if row2[column_number] == player:
        try:
            if (row3[column_number] == player) and (row4[column_number] == player):
                print("Player {} wins!".format(player))
        except IndexError:
            pass
    if row3[column_number] == player:
        try:
            if (row4[column_number] == player) and (row5[column_number] == player):
                print("Player {} wins!".format(player))
        except IndexError:
            pass
    if row4[column_number] == player:
        try:
            if (row5[column_number] == player) and (row6[column_number] == player):
                print("Player {} wins!".format(player))
        except IndexError:
            pass
    if row5[column_number] == player:
        try:
            if (row6[column_number] == player) and (row7[column_number] == player):
                print("Player {} wins!".format(player))
        except IndexError:
            pass


def refresh_board(row1, row2, row3):
    print(row7)
    print(row6)
    print(row5)
    print(row4)
    print(row3)
    print(row2)
    print(row1)
# refresh_board(column1, column2, column3)
refresh_board(row1, row2, row3)
while True:
    player1 = int(input("Player 1: Which column? "))
    if row1[player1 - 1] == " ":
        row1[player1 - 1] = "X"
    elif row2[player1 - 1] == " ":
        row2[player1 - 1] = "X"
    elif row3[player1 - 1] == " ":
        row3[player1 - 1] = "X"
    elif row4[player1 - 1] == " ":
        row4[player1 - 1] = "X"
    elif row5[player1 - 1] == " ":
        row5[player1 - 1] = "X"
    elif row6[player1 - 1] == " ":
        row6[player1 - 1] = "X"
    elif row7[player1 - 1] == " ":
        row7[player1 - 1] = "X"
    else:
        print("row full")
    refresh_board(row1, row2, row3)
    did_ya_win_across(row1, "X")
    did_ya_win_across(row2, "X")
    did_ya_win_across(row3, "X")
    did_ya_win_across(row4, "X")
    did_ya_win_across(row5, "X")
    did_ya_win_across(row6, "X")
    did_ya_win_across(row7, "X")
    check_column(0, "X")
    check_column(1, "X")
    check_column(2, "X")
    check_column(3, "X")
    check_column(4, "X")
    check_column(5, "X")
    check_column(6, "X")
    player2 = int(input("Player 2: Which column? "))
    if row1[player2 - 1] == " ":
        row1[player2 - 1] = "O"
    elif row2[player2 - 1] == " ":
        row2[player2 - 1 ] = "O"
    elif row3[player2 - 1] == " ":
        row3[player2 - 1] = "O"
    elif row4[player2 - 1] == " ":
        row4[player2 - 1] = "O"
    elif row5[player2 - 1] == " ":
        row5[player2 - 1] = "O"
    elif row6[player2 - 1] == " ":
        row6[player2 - 1] = "O"
    elif row7[player2 - 1] == " ":
        row7[player2 - 1] = "O"
    else:
        print("row full")
    refresh_board(row1, row2, row3)
    did_ya_win_across(row1, "O")
    did_ya_win_across(row2, "O")
    did_ya_win_across(row3, "O")
    did_ya_win_across(row4, "O")
    did_ya_win_across(row5, "O")
    did_ya_win_across(row6, "O")
    did_ya_win_across(row7, "O")
    check_column(0, "O")
    check_column(1, "O")
    check_column(2, "O")
    check_column(3, "O")
    check_column(4, "O")
    check_column(5, "O")
    check_column(6, "O")
