#ROT Cypher
#imports
#Constants
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
"i", "j", "k", "l", "m", "n",
"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#functions



def perform_cypher(string_to_cypher, rotation):
    cyphered_message = []
    message_list = list(string_to_cypher)
    for [i] in message_list:
        if i != " ":
            new_character_index = characters.index(i) + rotation
            cyphered_message.append(characters[new_character_index])
        else:
            cyphered_message.append(" ")
    zipped_cyphered_message = ("".join(cyphered_message))
    return zipped_cyphered_message


def perform_cypher_backwards(string_to_cypher, rotation):
    cyphered_message = []
    message_list = list(string_to_cypher)
    for [i] in message_list:
        if i != " ":
            new_character_index = characters.index(i) - rotation
            cyphered_message.append(characters[new_character_index])
        else:
            cyphered_message.append(" ")
    zipped_cyphered_message = ("".join(cyphered_message))
    return zipped_cyphered_message

#Classes
#setup code


rotation = input("This program will take a word or phrase and convert it to a cypher. \nThe default for the cypher rotation is 13. \nWould you like to use the default or set your own number? ")
if rotation == "default":
    rotation = 13
else:
    rotation = int(rotation)

string_to_cypher = input("Type the message you would like to encode: ")
message = perform_cypher(string_to_cypher.lower( ), rotation)
print('"{}" in cychper is "{}".'.format(string_to_cypher, message))


while True:
    other_action = input("Would you like to cypher another message (type 'cypher') or decode a cyphered message (type 'decode')? ")
    if other_action == "decode":
        string_to_cypher = input("input text to decode: ")
        message = (perform_cypher_backwards(string_to_cypher, rotation))
        print("that translates to {}".format(message))
    elif other_action == "cypher":
        string_to_cypher = input("enter text to cypher: ")
        message = perform_cypher(string_to_cypher, rotation)
        print("that becomes {}".format(message))
    else:
        break
print("bye!")

#why is this still printing the original message?!?!

#numbers_back_to_letters(cyphered_message)


#Testing
