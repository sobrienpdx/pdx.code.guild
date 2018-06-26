#hammer_time.py

time = input("What time is it? ")

# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM

hour = int(time[:-2])
meridian = time[-2:].lower()

if hour in [7, 8, 9] and meridian == "am":
    print("Breakfast time!")

elif time in [12, 1, 2] and meridian == "pm":
    print("Lunchtime")

elif hour in [7, 8, 9] and meridian == "pm":
    print("Dinner time!")

elif (hour in [10, 11] and meridian == "pm") or (hour in [1, 2, 3, 4] and meridian == "am"):
    print("Hammer Time!")

else:
    print("Time to go do something with your life.")
#[start: stop: skip]
