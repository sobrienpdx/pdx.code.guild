# Have the computer play pick6 many times and determine net balance.
#


# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance


# imports
import random

# constants

# Functions

#makes a list of 6 numbers
def pick6(top_range):
    i = 0
    numbers = []
    while i < 6:
        numbers.append(random.choice(range(1, top_range)))
        i += 1
    return numbers




# compares the ticket to the winning numbers
def compare_numbers(winning, ticket):
    matches = 0
    i = 0
    while i < 6:
        if ticket[i] == winning [i]:
            matches +=1
        i += 1
    return matches

# calculates dollar value of ticket after purchase price
def money_won(matches):
    if matches == 1:
        winnings = 4
    elif matches == 2:
        winnings = 7
    elif matches == 3:
        winnings = 100
    elif matches == 4:
        winnings = 50000
    elif matches == 5:
        winnings = 1000000
    elif matches == 6:
        winnings = 25000000
    elif matches == 0:
        winnings = 0
    winnings = winnings - 2
    return winnings

def find_net_gain(top_range):
    a = 0
    net_gain = 0
    while a < 5000:
        winning = pick6(top_range)
        # print("Winning numbers are {}".format(winning))
        ticket = pick6(top_range)
        # print("Ticket  numbers are {}".format(ticket))
        matches = compare_numbers(winning, ticket)
        winnings = money_won(matches)
        net_gain = net_gain + winnings
        #print("There are {} matches. Net gain is {}".format(matches, net_gain))
        a += 1
    print(net_gain)
    print(top_range)
    return net_gain

top_range = 20
net_gain = 10000
winning = pick6(top_range)
#print("Winning numbers are {}".format(winning))
ticket = pick6(top_range)
print(find_net_gain(top_range))
print("Ticket  numbers are {}".format(ticket))
while net_gain < -2000 or net_gain > 2000:
    if net_gain < 2000:
        top_range = top_range - 1
    if net_gain > 2000:
        top_range += 1
    net_gain = find_net_gain(top_range)
    print(net_gain)
    print(top_range)
    continue

#print("Your lifetime profit is {}".format(net_gain))
