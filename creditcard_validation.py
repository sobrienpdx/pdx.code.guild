# LAB: CREDIT CARD VALIDATION
# Let’s write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
#
# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:
#
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!

num_list = []
card_number = (input("Card number? "))
for i in card_number:
    num_list.append(int(i))
print(num_list)
check_number = num_list[-1]
print(check_number)
num_list.pop()
print(num_list)
num_list.reverse()
print(num_list)
for i in num_list[0: :2]:
    i = i * 2
    # if num_list[i] % 2 == 0:
    #     i = i + i
print(num_list)
