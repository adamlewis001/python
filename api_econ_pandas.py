import requests
import pandas as pd

# Series ID for CPI-U, all items, US city average, not seasonally adjusted
series_id = "CUUR0000SA0"

# v1 of the BLS API: no key needed
url = f"https://api.bls.gov/publicAPI/v1/timeseries/data/{series_id}"

response = requests.get(url)
data = response.json()
print(data)

observations = data["Results"]["series"][0]["data"]
df = pd.DataFrame(observations)

# Column fine tuning
# Rename CPI Value
df = df.rename(columns={"value": "cpi_value"})
# Add calc field YYYY-MM
df["yearmonth"] = df["year"] + "-" + df["period"].str[1:]

# Output and save to test.csv on Desktop
print(df.dtypes)
print(df[['yearmonth', 'cpi_value']])
df[['yearmonth','cpi_value']].to_csv('C:\\Users\\User001\\Desktop\\test.csv',index=False)
