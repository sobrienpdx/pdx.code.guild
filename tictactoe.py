# Tic Tac Toe is a game.

# You will write a Player class and Board class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.
#

# The Board class has the following methods:
# X __repr__() Returns a pretty string representation of the game board
# - move(x, y, player) Place a player’s token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# - calc_winner() What token character string has won or None if no one has.
# - is_full() Returns true if the game board is full.
# - is_game_over() Returns true if the game board is full or a player has won.
import os
import time
import random


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Player(): #Could also be written as named tuple
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Board():
    def __init__(self):
        # self.row0 = [" _|", "_", "|_"]
        # self.row1 = [" _|", "_", "|_"]
        # self.row2 = ["  |", " ", "| "]
        self.row0 = [" ", " ", " "]
        self.row1 = [" ", " ", " "]
        self.row2 = [" ", " ", " "]
        self.row_names = [self.row0, self.row1, self.row2]

    def __repr__(self):
        cls()
        outstring = ""
        for row in self.row_names:
            for space in row:
                outstring += space
            outstring += "\n"
        return outstring

    def check_for_winner(self, player):
        #check horizontal:
        for index, row in enumerate(self.row_names):
            if (row[0] == player.token) and (row[1] == player.token) and (row[2] == player.token):
                # print(f'{player.name} wins!')
                # time.sleep(1.5)
                game_over = True
                return game_over
        # check diagonal:
        if self.row0[0] == player.token and self.row1[1] == player.token and self.row2[2] == player.token:
            # print(f'{player.name} wins!')
            # time.sleep(1.4)
            game_over = True
            return game_over
        if self.row0[2] == player.token and self.row1[1] == player.token and self.row2[0] == player.token:
            # print(f'{player.name} wins!')
            # time.sleep(1.5)
            game_over = True
            return game_over
        # checks vertical:s
        index = 0
        while index <3:
            if (self.row0[index] == player.token) and (self.row1[index] == player.token) and (self.row2[index] == player.token):
                # print(f'{player.name} wins!')
                # time.sleep(1.5)
                game_over = True
                return game_over
            index += 1

    def move(self, player):
        if player.name != "computer":
            while True:
                try:
                    what_move = int(input(f"What move would you like to make, {player.name}? (number 1 - 9) \n: ").strip())
                    if not 0 < what_move < 10:
                        raise ValueError
                    else:
                        move = what_move
                        break
                except ValueError:
                    print("Please enter a number between 1 and 9.")
            while True:
                if move in [1, 2, 3]:
                    if self.row0[move -1] == " ":
                        self.row0[move -1] = player.token
                        break
                elif move in [4, 5, 6]:
                    if self.row1[move -4] == " ":
                        self.row1[move -4] = player.token
                        break
                elif move in [7, 8, 9]:
                    if self.row2[move -7] == " ":
                        self.row2[move -7] = player.token
                        break
                print("Space taken. Try again.")
                while True:
                    try:
                        what_move = int(input(f"What move would you like to make, {player.name}? (number 1 - 9) \n: ").strip())
                        if not 0 < what_move < 10:
                            raise ValueError
                        move = what_move
                        break
                    except ValueError:
                        print("Please enter a number between 1 and 9.")
        else:
            move = random.randint(1, 9)
            if move in [1, 2, 3]:
                if self.row0[move -1] == " ":
                    self.row0[move -1] = player.token
            elif move in [4, 5, 6]:
                if self.row1[move -4] == " ":
                    self.row1[move -4] = player.token
            elif move in [7, 8, 9]:
                if self.row2[move -7] == " ":
                    self.row2[move -7] = player.token



    def cats_game(self):
        for i in self.row_names:
            for index, space in enumerate(i):
                if space == " ":
                    full_board = False
                    return full_board
        full_board = True
        return full_board

#
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

    def play_through(self, player1, player2):
        while True:
            game_over = False
            print(board)
            board.move(player1)
            print(board)
            game_over = board.check_for_winner(player1)
            if game_over == True:
                return player1.name
            full_board = board.cats_game()
            if full_board == True:
                return "The cat"
            print(board)
            board.move(player2)
            print(board)
            game_over = board.check_for_winner(player2)
            if game_over == True:
                return player2.name
            full_board = board.cats_game()
            if full_board == True:
                return "The cat"

opponent = input("Would you like to play against the computer (c) or a human friend (h)? ")
if opponent == "h":
    player1_name = input("What is your name, player one? ")
    player1 = Player(player1_name, "X")
    player2_name = input("What is your name, player two? ")
    player2 = Player(player2_name, "O")
    board = Board()
elif opponent == "c":
    player1_name = input("What is your name, player one? ")
    player1 = Player(player1_name, "X")
    player2 = Player("computer", "O")
    board = Board()
while True:
    winner = board.play_through(player1, player2)
    print(f"{winner} wins!!!!!!!!!")
    print(f"{winner} wins!!!!!!!!!!!!!")
    print(f"{winner} wins!!!!!!!!!!!!!!!!!!")
    play_again = input("Would you like to play again? ")
    board = Board()
    if play_again == "n":
        break


print("ok, goodbye")
# " X̲|"
# O̲
