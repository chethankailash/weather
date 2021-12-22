import apikey
from geopy.geocoders import Nominatim

Url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=a61bc3a5290d560eb7362cd918d0b199"

def URL(city):
    City= getCity(city)
    # print("===")
    # print(City)
    Url = "http://api.openweathermap.org/data/2.5/weather?q={c}&appid={}".format(apikey.apiKey,c=City)
    return Url
    
def getCity(city):
    if city == "current":
        # Latitude = '41.8781'
        # Longitude = '87.6298'
        # geolocator = Nominatim(user_agent="geoapiForTemperatures")
        # location = geolocator.reverse("41.8781,87.6298")
        # return location
        return "Chicago"
    else:
        return city

