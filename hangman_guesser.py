with open("english.text") as f:
    word_list = f.read()
    list_of_words = word_list.split()

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f",
"g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]


# blanks = []
length = int(input("How many letters is the word? "))
# for i in range(length):
#     blanks.append("_")

correct_number = []
for word in list_of_words:
    if len(word) == length:
        correct_number.append(word)


def choose_letter(current_list):
    guess = "?"
    best_count = -1
    for letter in letters:
        letter_count = 0
        for word in current_list:
            if letter in word:
                letter_count += 1
        if letter_count > best_count:
            guess = letter
            best_count = letter_count
    return guess


def get_letter_info(letter):
    positions = []
    position = int(input("What position does the first {} hold? ".format(letter)))
    positions.append(position)
    while True:
        another = input("Is there another one? ")
        if another == "n":
            break
        position = int(input("What position does the next {} hold? ".format(letter)))
        positions.append(position)
    return positions

def cull(letter, positions, current_list):
    new_list = []
    for word in current_list:
        if consider_letters_in_one_word(letter, positions, word):
            new_list.append(word)
    return new_list

def consider_letters_in_one_word(letter, positions, word):
    for index in positions:
        if word[index -1] != letter:
            return False
    for index, bad_letter in enumerate(word):
        index += 1
        if bad_letter == letter and index not in positions:
            return False
    return True


current_list = correct_number
while True:
    guess = choose_letter(current_list)
    letters.remove(guess)
    correct_or_no = input("is there a/n {}? ".format(guess))
    if correct_or_no == "y":
        positions = get_letter_info(guess)
        current_list = cull(guess, positions, current_list)
    else:
        current_list = cull(guess, [], current_list)
    if len(current_list) == 1:
        print("It's {}. I win. I am the best. I am so smart. S-M-R-T.".format(current_list))
        break
