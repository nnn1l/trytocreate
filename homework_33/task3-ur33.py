import requests


API_KEY = "16f64466de4b43e8850193541251001"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city_name: str) -> dict:
    params = {
        "key": API_KEY,
        "q": city_name,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def format_weather(data: dict) -> str:

    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]
    wind_speed = data["current"]["wind_kph"]

    return (
        f"Weather in {city}, {country}:\n"
        f"  Temperature: {temperature}°C\n"
        f"  Condition: {weather}\n"
        f"  Wind Speed: {wind_speed} km/h"
    )

try:
    city_name = input("Enter a city name: ").strip()
    weather_data = get_weather(city_name)
    weather_report = format_weather(weather_data)
    print(weather_report)
except requests.exceptions.HTTPError as e:
    print("Error fetching weather data. Please check the city name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
