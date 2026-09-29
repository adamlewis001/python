import requests  # the library that lets Python make a web request

# Open-Meteo needs a latitude/longitude instead of a city name.
# These are the coordinates for Chicago — swap for any city you want.
latitude = 41.85
longitude = -87.65

# This is the actual API request. "url" is the address of Open-Meteo's server.
# "params" is a dictionary of options we're sending along with the request —
# here, we're asking for current temperature and windspeed.
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

response = requests.get(url, params=params)  # this line actually sends the request

data = response.json()  # convert the raw response text into a Python dictionary

print(data)  # print it so we can see exactly what came back
