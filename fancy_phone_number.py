# GOAL
# Write a small app that asks the user for an all-digits phone number, Then ‘pretty prints’ it out.
#
# INSTRUCTIONS
# Use the the input() builtin function.
#
# Here is an example of the program’s expected output:
#
# > Please enter an all digits phone number. >> 5035551234
#
# > 503-555-1234
#
# or
#
# > (503) 555-1234


phone_number_simple = input("what is your phone number? ")
first_three = phone_number_simple[:3:]
next_three = phone_number_simple[3:6:]
last_four = phone_number_simple[6::]
print('Your phone number is ({}) {}-{}.'.format(first_three, next_three, last_four))

#[start:stop:skip]
