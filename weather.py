import datetime as dt
import requests
import pgeocode
import zipcodes

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
#API_KEY = "82f12b4cfb2376c418f591263b75ec70"
API_KEY = open('api_key', 'r').read()

zipcode = input('Input zip code: ')

zip_info = zipcodes.matching(zipcode)
if zip_info:
    city = zip_info[0]['city']

print(f'City for zipcode {zipcode} is {city}')

# get geolocation coordinates (latitude/longitude) for requested zip code
nomi = pgeocode.Nominatim('us')
location = nomi.query_postal_code(zipcode)
print(f'Geolocation for {zipcode} is {location.latitude}, {location.longitude}')

#city = input("Enter City: ")
print('Chosen city is ' + city)
print("Current weather in " + city + ":")

def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit

#Getting response from openweathermap.org API
url = BASE_URL + "appid=" + API_KEY + "&q=" + city
response = requests.get(url).json()

#view full response file before reading final input
#print(response)
#input("Press enter to continue...")


temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature: {temp_celsius:.2f}C or {temp_farenheit:.2f}F")
print(f"Feels like: {feels_like_celsius:.2f}C or {temp_farenheit:.2f}F")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} m/s")
print(f"General weather: {description}")
#sunrise and sunset times are currently wrong
#print(f"Sun rise: {sunrise_time} UTC")
#print(f"Sun set: {sunset_time} UTC")
