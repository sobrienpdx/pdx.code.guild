# Open Weather Maps

import requests

city = input("What city would you like to check? ")
unit_type = input('Would you like that in Kelvin, Fahrenheit or Celsius? K/F/C : ')
if unit_type == "K":
     units = 'none'
elif unit_type == "F":
    units = "Imperial"
elif unit_type == "C":
    units = "Metric"

if unit_type == "K":
     unit = 'Kelvin'
elif unit_type == "F":
    unit = "Fahrenheit"
elif unit_type == "C":
    unit = "Celsius"
package = {
    'APPID': "376d39e1b99e5d606970839242793243",
    'q': city,
    "units": units
}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = package)

response = r.json()
# print(response)
# print(r.url)

description = response['weather'][0]['description']
temp = response['main']['temp']

print("The current temerature in {} is {} degrees {}.".format(city, temp, unit))
