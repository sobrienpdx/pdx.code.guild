# NUMBER TO PHRASE
# LAB: NUMBER TO PHRASE
# Convert a given number into its english representation. For example: 67 becomes ‘sixty-seven’. Handle numbers from 0-99.
#
# Hint: you can use modulus to extract the ones and tens digit.
#
# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings.
#
# VERSION 2
# Handle numbers from 100-999.
#
# VERSION 3 (OPTIONAL)
# Convert a number to roman numerals.
#
# VERSION 4 (OPTIONAL)
# Convert a time given in hours and minutes to a phrase.
digits = []
chunks = []

ones_dictionary = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
"7": "seven", "8": "eight", "9": "nine", "10": "ten"}
tens_dictionary = {"1": "one", "2": "twenty", "3": "thirty", "4": "fourty", "5": "fifty", "6": "sixty",
"7": "seventy", "8": "eighty", "9": "ninety"}
teens_dictionary = {"1": "eleven", "2": "twelve", "3": "thirteen", "4": "fourteen", "5": "fifteen", "6": "sixteen", "7": "seventeen", "8": "eighteen", "9": "nineteen" }


# takes user input and makes digits into separate items in list
def separate_columns(number):
    for i in number:
        digits.append(i)
    return digits

# these functions find the one, ten, and hundred digit
def convert1():
    ones = ones_dictionary[(digits[-1])]
    return ones

def convert2():
    tens = tens_dictionary[(digits[-2])]
    return tens

def convert3():
    hundreds = (ones_dictionary[(digits[-3])])
    return hundreds

def convert_teen():
    teens = teens_dictionary[(digits[-1])]
    return teens

#puts together the "between comma" words for 3 places at a time
def chunk_of_three():
    if len(digits) >= 1:
        ones = convert1()
        tens = ""
        space = ""
        hundreds = ""
        say_hundred = ""
        if len(digits) >= 2:
            if digits[-2] != "1":
                tens = convert2()
                space = " "
            else:
                tens = convert_teen()
                ones = ""
            if len(digits) >= 3:
                hundreds = convert3()
                say_hundred = " hundred "
        if len(digits) >= 3:
            digits.pop()
            digits.pop()
            digits.pop()
        elif len(digits) >= 2:
            digits.pop()
            digits.pop()
        elif len(digits) >= 1:
            digits.pop()
        chunk = "{}{}{}{}{}".format(hundreds, say_hundred, tens, space, ones)
        return chunk


number = (input("What number shall we convert? "))
separate_columns(number)

while len(digits) > 0:
    new_chunk = chunk_of_three()
    chunks.insert(0, new_chunk)

if len(chunks) == 1:
    print("{} would be written out as {}.".format(number, chunks[0]))
elif len(chunks) == 2:
    print("{} would be written out as {} thousand, {}.".format(number, chunks[0], chunks[1]))
elif len(chunks) == 3:
    print("{} would be written out as {} million, {} thousand, {}.".format(number, chunks[0], chunks[1], chunks[2]))
elif len(chunks) == 4:
    print("{} would be written out as {} billion, {} million, {} thousand, {}.".format(number, chunks[0], chunks[1], chunks[2], chunks[3]))
elif len(chunks) == 5:
    print("{} would be written out as {} trillion, {} billion, {} million, {} thousand, {}.".format(number, chunks[0], chunks[1], chunks[2], chunks[3], chunks[4]))
else:
    print("Nobody knows what happens after trillion.")
