import requests

# Series ID for CPI-U, all items, US city average, not seasonally adjusted
series_id = "CUUR0000SA0"

# v1 of the BLS API: no key needed
url = f"https://api.bls.gov/publicAPI/v1/timeseries/data/{series_id}"

response = requests.get(url)
data = response.json()

# The observations are nested inside the response, newest first.
observations = data["Results"]["series"][0]["data"]

# Print the 3 most recent months: year, month, and the index value.
for obs in observations[:3]:
    print(obs["year"], obs["periodName"], obs["value"])
