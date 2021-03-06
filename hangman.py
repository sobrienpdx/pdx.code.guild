# _ _ _ _ _ _ _ _ _
# # of guesses remaining: 10
# already guessed:
#
# Guess a letter: a
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a
#
# Guess a letter: a
# You've already guessed that
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a
#
# Guess a letter: k
# _ a _ _ _ _ a _ _
# # of guesses remaining: 9
# already guessed: a, k
# Guess a letter:
import random

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

guesses = 10
already_guessed = []
letter_list = []
blanks = []

# uses text to select target word
def target_word():
    with open("english.text") as f:
        word_list = f.read()
        list_of_words = word_list.split()
    hangman_list = []
    for i in list_of_words:
        if len(i) > 5:
            hangman_list.append(i)
    word = random.choice(hangman_list)
    for i in word:
        letter_list.append(i)
    for i in word:
        blanks.append("_ ")
    # print(letter_list)

def replace_good_guess(guessed_letter, letter_list):
    if guessed_letter in letter_list:
        index = 0
        for letter in letter_list:
            if letter == guessed_letter:
                blanks[index] = guessed_letter
                # print(blanks)
            index += 1
    return blanks



# print(blanks)
def play_full_game():
    guesses = 10
    while guesses > 0:
        cls()
        print("Already guessed: {}".format(already_guessed))
        print("You have {} guesses left".format(guesses))
        joined_blanks = "".join(blanks)
        print(joined_blanks)
        guessed_letter = input("What is your guess? ")
        while not (guessed_letter.isalpha() and len(guessed_letter) ==1):
            guessed_letter = input("What is your guess? ")
        if guessed_letter in already_guessed:
            print("You already guessed {}. Try again".format(guessed_letter))
            guessed_letter = input("What is your guess? ")
        else:
            already_guessed.append(guessed_letter)
        if guessed_letter in letter_list:
            replace_good_guess(guessed_letter, letter_list)
        else:
            guesses -= 1
        win = False
        if "_ " not in blanks:
            win = True
            break
    if win == True:
        print("You win!")
        word = "".join(letter_list)
        print('the word was ""{}"".'.format(word))
    else:
        print("sorry! you lose!")
        word = "".join(letter_list)
        print('the word was ""{}"".'.format(word))


while True:
    go_agin = input("would you like to play hangman? ")
    if go_agin == "y":
        blanks = []
        already_guessed = []
        letter_list = []
        target_word()
        play_full_game()
    else:
        break
