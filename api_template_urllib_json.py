import urllib.request      # opens a network connection
import urllib.parse        # turns a dict of params into a URL query string
import json                 # turns JSON text into a Python dict

# --- BUILD URL ---
base_url = "https://example.com/api"
params = {"key": "value"}
query_string = urllib.parse.urlencode(params)
full_url = f"{base_url}?{query_string}"

# --- SEND REQUEST + READ RESPONSE ---
with urllib.request.urlopen(full_url) as response:
    raw_bytes = response.read()
    text = raw_bytes.decode("utf-8")

# --- PARSE JSON ---
data = json.loads(text)

print(data)
