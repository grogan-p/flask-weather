import os
from dotenv import load_dotenv
from typing import Any
from pprint import pprint
import requests

load_dotenv()

DEFAULT_CTY = "Boston"

def get_current_weather(city: str = "Boston") -> Any:
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_json = requests.get(request_url).json()

    return weather_json

if __name__ == "__main__":
    print('/n*** Get Current Weather Conditions ***\n')

    city = input("Please enter a city name: ")

    # Check for empty string or string with only spaces

    if not city.strip():
        city = DEFAULT_CTY  # pylint: disable=invalid-name

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)