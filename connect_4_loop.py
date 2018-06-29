import os
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

row1 = [" ", " ", " ", " ", " ", " ", " ", ]
row2 = [" ", " ", " ", " ", " ", " ", " ", ]
row3 = [" ", " ", " ", " ", " ", " ", " ", ]
row4 = [" ", " ", " ", " ", " ", " ", " ", ]
row5 = [" ", " ", " ", " ", " ", " ", " ", ]
row6 = [" ", " ", " ", " ", " ", " ", " ", ]
row7 = [" ", " ", " ", " ", " ", " ", " ", ]
row_names = [row1, row2, row3, row4, row5, row6, row7]

def did_ya_win_across(player):
    n = 0
    while n < 7:
        which_row = row_names[n]
        for index, marker in enumerate(which_row):
            if marker == player:
                try:
                    if (which_row[index +1] == player) and (which_row[index +2] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!!!!!!!!!!".format(player))
                        break
                except IndexError:
                    continue
        n += 1

def check_columns(player):
    column_number = 0
    while column_number < 7:
        row = 0
        while row < 5:
            if row_names[row][column_number] == player:
                try:
                    if (row_names[row + 1][column_number] == player) and (row_names[row + 2][column_number] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!".format(player))
                except IndexError:
                    pass
            row +=1
        column_number += 1
def refresh_board():
    print(row7)
    print(row6)
    print(row5)
    print(row4)
    print(row3)
    print(row2)
    print(row1)
# refresh_board(column1, column2, column3)
cls()
refresh_board()
while True:
    player1 = int(input("Player 1: Which column? "))
    n = 0
    while n < 7:
        row = row_names[n]
        if row[player1 - 1] == " ":
            row[player1 - 1] = "X"
            break
        n += 1
    else:
        print("row full: you lose a turn")
        time.sleep(1.5)
    # clear the screen and reprint with new play. Check to see if there are any winners yet
    cls()
    refresh_board()
    did_ya_win_across("X")
    check_columns("X")

    player2 = int(input("Player 2: Which column? "))
    n = 0
    while n < 7:
        row = row_names[n]
        if row[player2 - 1] == " ":
            row[player2 - 1] = "O"
            break
        n += 1
    else:
        print("row full: you lose a turn")
        time.sleep(1.5)

    # clear the screen and reprint with new play. Check to see if there are any winners yet
    cls()
    refresh_board()
    did_ya_win_across("O")
    check_columns("O")
