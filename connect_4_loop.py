import os
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

row0 = [" ", " ", " ", " ", " ", " ", " ", ]
row1 = [" ", " ", " ", " ", " ", " ", " ", ]
row2 = [" ", " ", " ", " ", " ", " ", " ", ]
row3 = [" ", " ", " ", " ", " ", " ", " ", ]
row4 = [" ", " ", " ", " ", " ", " ", " ", ]
row5 = [" ", " ", " ", " ", " ", " ", " ", ]
row6 = [" ", " ", " ", " ", " ", " ", " ", ]
row_names = [row0, row1, row2, row3, row4, row5, row6]

win = False

def did_ya_win_across(player):
    n = 0
    while n < 7:
        which_row = row_names[n]
        for index, marker in enumerate(which_row):
            if marker == player:
                try:
                    if (which_row[index +1] == player) and (which_row[index +2] == player) and (which_row[index +3] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!!!!!!!!!!".format(player))
                        win = True
                        return win
                except IndexError:
                    continue
        n += 1

def diagonal_forward_slash(player):
    n = 0
    while n < 4:
        row = row_names[n]
        one_up = row_names[n +1]
        two_up = row_names [n +2]
        three_up = row_names [n +3]
        for index, marker in enumerate(row):
            if marker == player:
                try:
                    if (one_up[index +1] == player) and (two_up[index +2] == player) and (three_up[index +3] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!!!!!!!!!!".format(player))
                        win = True
                        return win
                except IndexError:
                    continue
        n += 1


def diagonal_back_slash(player):
    n = 6
    while n > 2:
        row = row_names[n]
        one_down = row_names[n -1]
        two_down = row_names [n -2]
        three_down = row_names [n -3]
        for index, marker in enumerate(row):
            if marker == player:
                try:
                    if (one_down[index +1] == player) and (two_down[index +2] == player) and (three_down[index +3] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!!!!!!!!!!".format(player))
                        win = True
                        return win
                except IndexError:
                    continue
        n -= 1


def check_columns(player):
    column_number = 0
    while column_number < 7:
        row = 0
        while row < 5:
            if row_names[row][column_number] == player:
                try:
                    if (row_names[row + 1][column_number] == player) and (row_names[row + 2][column_number] == player) and (row_names[row + 3][column_number] == player):
                        print("Player {} wins!".format(player))
                        print("Player {} wins!".format(player))
                        print("Player {} wins!!!!!!!!!!!!!!!!".format(player))
                        win = True
                        return win
                except IndexError:
                    pass
            row +=1
        column_number += 1

def refresh_board():
    print(row6)
    print(row5)
    print(row4)
    print(row3)
    print(row2)
    print(row1)
    print(row0)
# refresh_board(column1, column2, column3)
cls()
refresh_board()
while True:
    win = False
    player1 = (input("Player X: Which column? "))
    while not (player1.isdigit() and int(player1) < 8):
        print("Please use numbers 1 through 7.")
        player1 = (input("Player X: Which column? "))
    player1 = int(player1)
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
    win1 = did_ya_win_across("X")
    win2 = check_columns("X")
    win3 = diagonal_forward_slash("X")
    win4 = diagonal_back_slash("X")
    if win1 or win2 or win3 or win4:
        break
    player2 = (input("Player O: Which column? "))
    while not (player2.isdigit() and int(player2) < 8):
        print("Please use numbers 1 through 7.")
        player2 = (input("Player O: Which column? "))
    player2 = int(player2)
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
    win1 = did_ya_win_across("O")
    win2 = check_columns("O")
    win3 = diagonal_forward_slash("O")
    win4 = diagonal_back_slash("O")
    if win1 or win2 or win3 or win4:
        break

print("Good game. Goodbye!")
