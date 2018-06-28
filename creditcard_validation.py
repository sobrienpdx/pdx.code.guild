# LAB: CREDIT CARD VALIDATION
# Let’s write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:


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
doubled_list = []
# get user input and convert to integer:
card_number = (input("Card number? "))
for i in card_number:
    num_list.append(int(i))
print(num_list)
# Slice off the last digit. That is the check digit:
check_number = num_list[-1]
print(check_number)
num_list.pop()
print(num_list)
# Reverse the digits:
num_list.reverse()
print(num_list)
# Double every other element in the reversed list:
for index, number in enumerate(num_list):
    if index % 2 == 0:
        number = number * 2
    else:
        number = number
    doubled_list.append(number)
print(doubled_list)
# Subtract nine from numbers over nine:
under_10 = []
for i in doubled_list:
    if i > 9:
        adjusted_num = i - 9
    else:
        adjusted_num = i
    under_10.append(adjusted_num)
print(under_10)
# Sum all values:
total = 0
for i in under_10:
    total += i
print(total)
# Take the second digit of that sum:
string_total = str(total)
second_digit = string_total[1]
print(second_digit)
if int(second_digit) == check_number:
    print("Credit card validated")
else:
    print("Invalid card number")
