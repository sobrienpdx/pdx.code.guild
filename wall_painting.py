# wall-painting.py
# One gallon can of paint will cover up to 400 square feet
# Get user input
width = int(input("I hear you want to know how much it will cost to paint your wall. In feet, how wide is the wall? "))
height = int(input("And the height in feet? "))
another_wall = input("Do you have any other walls to paint? y/n ")

while another_wall == "y":
    width_other_wall = int(input("How wide is the other wall? "))
    width = width + width_other_wall
    height_other_wall = int(input("How high is the other wall? "))
    height = height + height_other_wall
    another_wall = input("Do you have any other walls to paint? y/n ")

windows = input("Are there any windows or doors that you aren't painting that need to be subtracted from the area of the wall? ")
if windows == "y":
    window_width = int(input("In feet, how wide is the window/door? "))
    window_height = int(input("And the height in feet? "))
    another_window = input("Do you have any other windows or doors to account for? y/n ")

    while another_window == "y":
        width_other_window = int(input("How wide is the other window/door? "))
        window_width = windw_width + width_other_window
        height_other_window = int(input("How high is the other window/door? "))
        window_height = widnow_height + height_other_window
        another_window = input("Do you have any other windows or doors to account for? y/n ")

def calculate_gallons():
    area = (width - window_width) * (height - window_height)
    gallons_needed = area // 400 + 1
    print("Your wall is {} sq ft. You will need {} gallon/s.".format(area, gallons_needed))
    return gallons_needed

calculate_gallons()
price_per_gallon = int(input("What is the price per gallon for the paint? "))
coat_number = int(input("How many coats of paint are you going to do? "))
total = price_per_gallon * calculate_gallons() * coat_number
print("It will cost about ${} bucks.".format(total))
