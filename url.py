import apikey
from geopy.geocoders import Nominatim

Url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=a61bc3a5290d560eb7362cd918d0b199"

def URL(city):
    City= getCity(city)
    Url = "http://api.openweathermap.org/data/2.5/weather?q={c}&appid={}".format(apikey.apiKey,c=City)
    return Url
    
def getCity(city):
    if city == "current":
        return "Chicago"
    else:
        return city

