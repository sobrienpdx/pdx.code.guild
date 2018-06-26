
# Get user input
raw_number = int(input("Enter a distance, number only: "))
from_measurement = input("Is that miles, km, meters, or ft?  ")
to_measurement = input("What do you want to convert it to? ")

def convert_distance():
    # converts input to meters
    if from_measurement == "miles":
        measurement_in_meters = raw_number * 1609.34
    elif from_measurement == "km":
        measurement_in_meters = raw_number * 1000
    elif from_measurement == "meters":
        measurement_in_meters = raw_number
    elif from_measurement == "ft":
        measurement_in_meters = raw_number * 0.3048
    
    # changes meters to target measurement
    if to_measurement == "miles":
        converted_number = measurement_in_meters * 0.000621371
    elif to_measurement == "km":
        converted_number = measurement_in_meters * 0.001
    elif to_measurement == "meters":
        converted_number = measurement_in_meters
    elif to_measurement == "ft":
        converted_number = measurement_in_meters * 3.28084
    print("{} {} would be {} {}.".format(raw_number, from_measurement, converted_number, to_measurement))

# Call funciton
convert_distance()
