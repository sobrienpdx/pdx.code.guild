# mad_lib2.py
# greeting = "hi"
# name = "Shaunna"
#




def  execute_mad_lib():

    noun1 = input("give me a plural noun with 2 syllables ")
    adjective1 = input("give me an adjective with 3 syllables ")
    adjective2 = input("another adjective with 3 syllables ")

    animal1 = input("give me a single syllable animal ")
    noun2 = input("another noun that's 2 syllables ")
    adverb1 = input("and a two-syllable adverb? ")

    print("Yesterday, All my {} seemed so {}, Now it looks as though they're {}, Oh, I believe in yesterday. Suddenly, I'm not half the {} I used to be. There's a {} hanging over me. Oh, yesterday came {}".format(noun1, adjective1, adjective2, animal1, noun2,adverb1))

play_or_no = input("Want to do a mad lib? Y/N ")
if play_or_no in ["Y", "y"]:
    execute_mad_lib()
play_again =input("Want to try the same one with different words? ")
while play_again in ["Y", "y"]:
    execute_mad_lib()
    play_again = input("One more time? ")
else:
    print("Thanks for playing! Bye!")
