import requests
from bs4 import BeautifulSoup
import pgeocode
import zipcodes

print('new branch ... djjw')

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

# create url
url = "https://www.google.com/search?q="+"weather"+zipcode

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')

# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags having particular class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all the data
print("Temperature: ", temp)
print("Time is", time)
print("Sky Description: ", sky)
print(other_data)