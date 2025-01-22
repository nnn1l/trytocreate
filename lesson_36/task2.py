import asyncio
import aiohttp
import json
from datetime import datetime, timedelta


async def fetch_apod(session, api_key, date):

    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "date": date}
    try:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            data = await response.json()
            return data
    except aiohttp.ClientError as e:
        print(f"Failed to fetch data for {date}: {e}")
        return None


async def fetch_all_apods(api_key, start_date, end_date):

    date_list = [
        (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((end_date - start_date).days + 1)
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_apod(session, api_key, date) for date in date_list]
        responses = await asyncio.gather(*tasks)
        return [resp for resp in responses if resp is not None]


def save_to_file(data, filename):

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")


async def main():
    API_KEY = "Mwlas3zKibf1RZ6BP5OWVCc3OkHhYHXVhviB1qdq"
    START_DATE = datetime(2023, 1, 1)
    END_DATE = datetime(2023, 1, 10)

    print("Fetching APOD data...")
    apod_data = await fetch_all_apods(API_KEY, START_DATE, END_DATE)


    sorted_data = sorted(apod_data, key=lambda x: x["date"])


    OUTPUT_FILE = "apod_data.json"
    save_to_file(sorted_data, OUTPUT_FILE)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProcess interrupted.")
