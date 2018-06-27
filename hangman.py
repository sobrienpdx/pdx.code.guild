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

with open("english.text") as f:
    word_list = f.read()
    list_of_words = word_list.split()

hangman_list = []
for i in list_of_words:
    if len(i) > 5:
        hangman_list.append(i)

word = random.choice(hangman_list)
print(word)

guesses = 10
already_guessed = []
print("_ " * len(word))
letter_list = []

for i in word:
    letter_list.append(i)
print(letter_list)
joined_word = "".join(letter_list)
print(joined_word)


while guesses > 0:
    guessed_letter = input("What is your guess? ")
    while not (guessed_letter.isalpha() and len(guessed_letter) ==1):
        guessed_letter = input("What is your guess? ")
    if guessed_letter in already_guessed:
        print("You already guessed {}. Try again".format(guessed_letter))
    already_guessed.append(guessed_letter)
    print("Already guessed: {}".format(already_guessed))
