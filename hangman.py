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
        blanks.append("_")
    return



target_word()





print(letter_list)
print(blanks)
guessed_letter = input("What is your guess? ")


if guessed_letter in letter_list:
    index = 0
    for letter in letter_list:
        if letter == guessed_letter:
            blanks[index] = guessed_letter
        index += 1
print(blanks)


# joined_word = "".join(letter_list)
# print(joined_word)

# def play_round():
# while guesses > 0:
#     guessed_letter = input("What is your guess? ")
#     while not (guessed_letter.isalpha() and len(guessed_letter) ==1):
#         guessed_letter = input("What is your guess? ")
#     if guessed_letter in already_guessed:
#         print("You already guessed {}. Try again".format(guessed_letter))
#     already_guessed.append(guessed_letter)
#     print("Already guessed: {}".format(already_guessed))