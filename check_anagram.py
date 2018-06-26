comparison_word = input("enter a word: ")
possible_anagram = input("enter a word that might be an anagram of the first word ")

comparison_sorted = (sorted(comparison_word.lower()))
possible_sorted = (sorted(possible_anagram.lower()))

if comparison_sorted == possible_sorted:
    print("{} is indeed an anagram of {}".format(possible_anagram, comparison_word))
else:
    print("Alas! {} is not an anagram of {}. :( ".format(possible_anagram.capitalize(), comparison_word))
