import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city,"appid": API_KEY,"units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code != 200:
            if response.status_code == 404:
                return "City not found"
            if response.status_code == 401:
                return "Invalid API key"
            return f"Error: {response.status_code}"

        data = response.json()

        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return result

    except requests.exceptions.Timeout:
        return "Request timeout"
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    
    if not city:
        print("\nResult:")
        print(json.dumps({"error": "City name cannot be empty"}, indent=2))
    else:
        result = get_weather(city)
        print("\nResult:")
        
        if isinstance(result, dict):
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps({"error": result}, indent=2))