import requests            

# --- BUILD URL + SEND REQUEST in one call ---
url = "https://example.com/api"
params = {"key": "value"}
response = requests.get(url, params=params)

# --- PARSE JSON ---
data = response.json()

print(data)
