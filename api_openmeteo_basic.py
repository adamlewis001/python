import urllib.request  # built into Python, no install needed
import urllib.parse    # helps build the URL with parameters
import json            # built into Python, converts JSON text to a dictionary

latitude = 41.85
longitude = -87.65

base_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

# urllib doesn't glue params onto the URL for you like requests does —
# you have to build the full address string yourself
query_string = urllib.parse.urlencode(params)
full_url = f"{base_url}?{query_string}"

# This sends the GET request and gives back a response object
with urllib.request.urlopen(full_url) as response:
    raw_bytes = response.read()          # the reply comes back as raw bytes, not text
    text = raw_bytes.decode("utf-8")     # decode those bytes into a text string
    data = json.loads(text)              # parse that text string as JSON into a dictionary

print(data)
