# Possible modifications:
# - use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)
# - add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side
# - make what’s printed on the screen a part of a much larger map (with the player always shown at the center of the screen)
# - loading a text file containing the map, or procedurally generate things
# - walls / barriers
# - use different unicode characters (you can find lists online)
# - ascii art
# - colorama for custom colors, or curses for even more control of the terminal
# - add ‘fog of war’ - only show the elements of board immediately around the player (you can then find a torch item, which expands your visibility)
# - have enemies move around
# - add an inventory system
# - add player health, more complex encounters
# - add hidden treasure, make the objective to find all the treasure
# - add a ‘final boss’ that you can only face once collecting items
# - re-use previous labs (guess the number, rock-paper-scissors)

import os
import time
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import random

class Dude:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        # self.face = face




width = 10  # the width of the board
height = 10  # the height of the board
treasure_count = 0
enemies = []

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player = Dude(4, 4)

# add 4 enemies in random locations
for i in range(4):
    enemies.append(Dude(random.randint(0, height - 1), random.randint(0, width - 1)))

def sneak_around(dude):
    if dude.j < 0:
        dude.j = width -1
    if dude.j == width:
        dude.j = 0
    if dude.i < 0:
        dude.i = height -1
    if dude.i == height:
        dude.i = 0

def move_player():
    command = input('what is your command? ')  # get the command from the user
    if command == 'l':
        player.j -= 1  # move left
    elif command == 'r':
        player.j += 1  # move right
    elif command == 'u':
        player.i -= 1  # move up
    elif command == 'd':
        player.i += 1  # move down
    sneak_around(player)

# move enemies around a little
def move_enemies(enemies):
    for enemy in enemies:
        enemy.i += random.randint(-1, 1)
        enemy.j += random.randint(-1, 1)
        sneak_around(enemy)

def character_or_space(i, j):
    if i == player.i and j == player.j:
        return '🤓'
    n = len(enemies) -1
    while n > -1:
        if i == enemies[n].i and j == enemies[n].j:
            return "☠"
        n -= 1
    return board[i][j]

def print_board():
    for i in range(height):
        for j in range(width):
            print(character_or_space(i, j), end = ".")
        print()
            # if we're at the player location, print the player icon
        #         if i in enemies.i and j == enemies[n].j:
        #             print("☠", end=".")
        #         n -= 1
        #     if i == player.i and j == player.j
        #         print('🤓', end='.')
        #     else:
        #         print(board[i][j], end='.')  # otherwise print the board square
        # print()

# add treasures
for i in range(6):
    treasure_i = random.randint(0, height - 1)
    treasure_j = random.randint(0, width - 1)
    board[treasure_i][treasure_j] = "💎"

# loop until the user says 'done' or dies
while True:
        # print out the board
    cls() #keep the screen in the same place
    print("Treasures: {}".format(treasure_count))

    print_board()
    move_enemies(enemies)
    move_player()
    # check if the player is on the same space as an enemy
    for index, enemy in enumerate(enemies):
        if player.i == enemy.i and player.j == enemy.j:
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                print('you\'ve slain the enemy')
                enemies.pop(index)
            else:
                print('you hestitated and were slain')
                break
    # check if the player is on the same space as a treasure
    if board[player.i][player.j] == '💎':
        treasure_count += 1
        board[player.i][player.j] = ' '  # remove the treasure from the board
        print('you\'ve encountered a treasure!')
        time.sleep(2)
