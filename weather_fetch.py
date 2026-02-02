
# def test_api_calls():
#     print("Testing 200 OK ...")
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#     print(f"Status Code: {response.status_code}")
#     print(f"JSON: {response.json()}\n")


#     print("Testing 404 not found ...")
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
#     print(f"Status code: {response.status_code}")
#     print(f"Data: {response.json()}\n")

#     print("Error Handling ..")
#     response = requests.get("https://httpbin.org/status/500")
#     if response.status_code == 200:
#         print("Success?")
#         print(f"Response code: {response.status_code}")
        
#     else:
#         print("Error")

    # response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,population")

# if code == 200
#  print len(countries)

#     if response.status_code == 200:
#         print(f"Country total: {len(response.json())}")
#     else:
#         print(f"Error - {response.status_code}")
# test_api_calls()

# x = True

# def true(x):
#     if x is True:
#         return None
#     else:
#         print("bendani")

# true(x)

import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHERSTACK_API_KEY")

if not API_KEY:
    raise ValueError("WEATHERSTACK_API_KEY not found")

def get_weather(city):
    """ Featch weather data for a city """
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")

def extract_data(weather_data):
    if not weather_data:
        return None
    
    return {
        "timestamp": datetime.now().isoformat(),
        "city": weather_data['location']['name'],
        "temperature": weather_data['current']['temperature'],
        "feels_like": weather_data['current']['feelslike'],
        "humidity": weather_data['current']['humidity'],
        "weather": weather_data['current']['weather_descriptions'],
        "air_quality": weather_data['current']['air_quality']['us-epa-index']
    }


def save_to_file(record, filename = "weather_data.json"):
    with open(filename, "a") as f:
        f.write(json.dumps(record) + "\n")
    print(f"✓ Saved record: {record['city']} - {record['temperature']}°C")

if __name__ == "__main__":
    data = get_weather("Kuala Lumpur")
    clean_data = extract_data(data)

    if clean_data:
        save_to_file(clean_data)
        print(clean_data)