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


    def move(self, player):
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


player1 = Player("Joe", " X")
player2 = Player("Sam", " O")
board = Board()
while True:
    print(board)
    board.move(player1)
    print(board)
    board.move(player2)

# " X̲|"
# O̲
