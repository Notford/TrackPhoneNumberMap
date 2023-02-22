import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

# taking input the phonenumber along with the country code
number = input("Enter the phone number with country code : ")

# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

# Storing the API Key in the Key variable
Key = "bda09742f8594a38b77c3b65f644c3b8"

# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_valid_number(phoneNumber,"en")
print("location : "+geolocation)

# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+service)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(geolocation)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)

# Adding a Marker on the map to show the location name
folium.Marker([lat,lng],popup=geolocation).add_to(myMap)

# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")