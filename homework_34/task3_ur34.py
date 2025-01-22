import requests
import json
from datetime import datetime, timedelta
from threading import Thread
from queue import Queue

NASA_API_URL = "https://api.nasa.gov/planetary/apod"
OUTPUT_FILE = "apod_comments.json"
NASA_API_KEY = "8iYybckZ2JDeDmsse65kanuVrpqP1jgtmp72080Q"


def fetch_apod_data(date, queue):
    params = {
        "api_key": NASA_API_KEY,
        "date": date.isoformat(),
    }
    try:
        response = requests.get(NASA_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        queue.put(data)
    except requests.RequestException as e:
        print(f"Failed to fetch data for {date}: {e}")

# Prepare date range for the last 7 days
today = datetime.utcnow().date()
dates = [today - timedelta(days=i) for i in range(7)]

# Queue to store results
results_queue = Queue()
threads = []

# Create and start a thread for each date
for date in dates:
    thread = Thread(target=fetch_apod_data, args=(date, results_queue))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()


comments = []
while not results_queue.empty():
    comments.append(results_queue.get())

# Save comments to JSON
with open(OUTPUT_FILE, "w") as f:
    json.dump(comments, f, indent=4)

print(f"Data successfully saved to {OUTPUT_FILE}")
