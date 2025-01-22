import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from datetime import datetime, timedelta


def fetch_apod_data(api_key, date):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "date": date}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {date}: {e}")
        return None


def fetch_all_apod(api_key, start_date, end_date):
    date_list = [
        (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((end_date - start_date).days + 1)
    ]
    results = []

    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        futures = [executor.submit(fetch_apod_data, api_key, date) for date in date_list]
        for future in futures:
            data = future.result()
            if data:
                results.append(data)

    return results


def save_to_file(data, filename):
    """Save data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    API_KEY = "Mwlas3zKibf1RZ6BP5OWVCc3OkHhYHXVhviB1qdq"

    START_DATE = datetime(2023, 1, 1)
    END_DATE = datetime(2023, 1, 31)

    print("Fetching APOD data...")
    apod_data = fetch_all_apod(API_KEY, START_DATE, END_DATE)

    sorted_data = sorted(apod_data, key=lambda x: x["date"])

    OUTPUT_FILE = "apod_data.json"
    save_to_file(sorted_data, OUTPUT_FILE)
