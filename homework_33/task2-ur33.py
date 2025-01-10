import requests
import json
from datetime import datetime, timedelta


NASA_API_URL = "https://api.nasa.gov/planetary/apod"
OUTPUT_FILE = "apod_data.json"


NASA_API_KEY = "8iYybckZ2JDeDmsse65kanuVrpqP1jgtmp72080Q"


today = datetime.utcnow().date()
start_date = today - timedelta(days=7)
end_date = today

# Fetch APOD data
params = {
    "api_key": NASA_API_KEY,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
}

print(f"Fetching APOD data from {start_date} to {end_date}...")

response = requests.get(NASA_API_URL, params=params)
response.raise_for_status()  # Raise an error if the request fails
apod_data = response.json()

print(f"Fetched {len(apod_data)} APOD entries.")

# Save data to JSON
with open(OUTPUT_FILE, "w") as f:
    json.dump(apod_data, f, indent=4)

print(f"Data successfully saved to {OUTPUT_FILE}")