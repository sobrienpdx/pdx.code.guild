
#opens file and reads it (not by line!!!)
with open("quijote_backup.text", "r") as quijote_text:
    book = quijote_text.read()


import string #imports some mysterious magic

list_of_words = book.split() #splits book by spaces and makes into list
list_of_words = [element.lower() for element in list_of_words] # makes all elements in list lowercaser - I don't completely grock this
list_of_words = [element.rstrip(string.punctuation) for element in list_of_words] # got the format thing to strip all punctuation from the list


from collections import Counter #more magic
list_most_common = Counter(list_of_words).most_common(10)
print(list_most_common)
