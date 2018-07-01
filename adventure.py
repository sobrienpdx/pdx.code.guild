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

class Location:
    def __init__(self, i, j):
        self.i = i
        self.j = j

width = 10  # the width of the board
height = 10  # the height of the board
treasure_count = 0
enemy_locations = []

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_location = Location(4, 4)

# add 4 enemies in random locations
for i in range(4):
    enemy_locations.append(Location(random.randint(0, height - 1), random.randint(0, width - 1)))

# move enemies around a little
def move_enemies(enemy_locations):
    n = random.randint(-1, 1)
    for enemy_location in enemy_locations:
        enemy_location.i += n
        enemy_location.j += n

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
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_location.i and j == player_location.j:
                print('🤓', end='.')
            elif i == enemy_locations[0].i and j == enemy_locations[0].j:
                print("☠", end=".")
            elif i == enemy_locations[1].i and j == enemy_locations[1].j:
                print("☠", end=".")
            elif i == enemy_locations[2].i and j == enemy_locations[2].j:
                print("☠", end=".")
            elif i == enemy_locations[3].i and j == enemy_locations[3].j:
                print("☠", end=".")
            else:
                print(board[i][j], end='.')  # otherwise print the board square
        print()
    move_enemies(enemy_locations)

    command = input('what is your command? ')  # get the command from the user
    if command == 'done':
        break  # exit the game
    elif command == 'l':
        player_location.j -= 1  # move left
        if player_location.j < 0:
            player_location.j = width -1
    elif command == 'r':
        player_location.j += 1  # move right
        if player_location.j == width:
            player_location.j = 0
    elif command == 'u':
        player_location.i -= 1  # move up
        if player_location.i < 0:
            player_location.i = height -1
    elif command == 'd':
        player_location.i += 1  # move down
        if player_location.i == height:
            player_location.i = 0

    # check if the player is on the same space as an enemy
    if board[player_location.i][player_location.j] == '☠':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_l.ocationi][player_location.j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break
    # check if the player is on the same space as a treasure
    if board[player_location.i][player_location.j] == '💎':
        treasure_count += 1
        board[player_location.i][player_location.j] = ' '  # remove the treasure from the board
        print('you\'ve encountered a treasure!')
        time.sleep(2)
