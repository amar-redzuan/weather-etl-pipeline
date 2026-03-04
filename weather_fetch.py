import requests
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.weatherstack.com/current"

cities = [
    "Kuala Lumpur",
    "Putrajaya",
    "Kajang"
]

def get_weather(city):
    params = {
        "access_key": API_KEY,
        "query": city
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

def extract_data(weather_data):
    if not weather_data or "current" not in weather_data:
        return None

    location = weather_data["location"]
    current = weather_data["current"]

    return {
        "timestamp": datetime.now().isoformat(),
        "city": location["name"],
        "country": location["country"],
        "latitude": location["lat"],
        "longitude": location["lon"],

        "temperature": current["temperature"],
        "feels_like": current["feelslike"],
        "humidity": current["humidity"],
        "pressure": current["pressure"],

        "wind_speed": current["wind_speed"],
        "wind_direction": current["wind_dir"],

        "cloud_cover": current["cloudcover"],
        "precipitation": current["precip"],
        "uv_index": current["uv_index"],

        "weather": current["weather_descriptions"],
        "air_quality": current["air_quality"]["us-epa-index"]
    }

def save_to_file(record):
    with open("weather_data.json", "a") as f:
        f.write(json.dumps(record) + "\n")

def main():
    run_timestamp = datetime.now().isoformat()

    for city in cities:
        data = get_weather(city)
        if not data:
            print(f"Failed to get data for {city}")
            continue

        # Extract all fields, adding the run timestamp
        clean_data = extract_data(data)
        if clean_data:
            # Override the timestamp with batch timestamp
            clean_data["timestamp"] = run_timestamp

            save_to_file(clean_data)
            print(f"✓ Saved data for {city}")

if __name__ == "__main__":
    main()