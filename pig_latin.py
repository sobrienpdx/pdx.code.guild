# If the first letter is a consonant, move it to the end.
# Add “ay” to the end of that.
# If the first letter is a vowel, just ad “yay” to the end.

target_word = input("This is a pig latin translator. What word would you like to translate? ")

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "m", "s", "p", "q", "r", "t", "v", "w", "x", "y", "z",]
vowels = ["a", "e", "i", "o", "u", ]

def convert_word_and_print():
    letter_list = list(target_word)

    for i in target_word:
        if i in consonants:
            letter_list.append(i)
            letter_list.remove(i)
        if i in vowels:
            break

    word_in_PL = ''.join(letter_list)
    word_with_capital = word_in_PL[0].upper() + word_in_PL[1:] +"ay"
    target_with_capital = target_word[0].upper() + target_word[1:] 

    print("{} in pig latin is {}.".format(target_with_capital, word_with_capital))

convert_word_and_print()
go_again = input("Want to do another? ")
while go_again.lower() == "y":
    target_word = input("What word would you like to translate? ")
    convert_word_and_print()
    go_again = input("Want to do another? ")
else:
    print("kay, bye!")
