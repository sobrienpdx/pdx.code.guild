# check_palindrome



target_word = input("enter possible palindrome: ")
word_backward = ("".join(reversed(target_word)))
if word_backward.lower() == target_word.lower():
    print("Congratulations! You have a palindrome! ")
else:
    print("I'm so sorry. That's not a palindrome afterall.")

# print("".join(reversed(sorted_word)))


# reversed_word = (reversed(sorted_word))
# print(reversed_word)



#
#
# word = "ladlkadf"
# print(word.capitalize())
# print(word.center(100, "*"))
# print(word.count("a"))
# print(word.endswith("a" or "g"))
# print(word.find("d")) #(finds the first instance of the "d," prints its index, and stops. -1 means none)
# print(word.index("l")) #code breaks and doesn't work if not found
# print(word.isalnum()) #returns true if string has at least one character and all charaters are alphanumeric or returns false
# print(word.isdigit())
# print(word.islower())
# ''.join(x)
# print(word.replace("l", "I replaced l with this"))
# print(word.split()) #splits on space
