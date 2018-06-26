# average numbers

print('This is an average number calculator. You can enter numbers to get the average. When you have no more numbers to add, type "done".')
number = input("Number or done? ")

nums = []


while number != "done":
    nums.append(int(number))
    length = (len(nums))
    number = input("Number or done? ")

total = 0

for i in nums:
    total += i


length = len(nums)
average = total / length

print("The average of those numbers is {}".format(average))
