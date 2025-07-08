import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_forecast(city: str) -> str:
    if not API_KEY:
        return "❌ API key not found. Set OPENWEATHER_API_KEY in your .env file."

    # Step 1: Geocoding
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(geocode_url)
    
    if response.status_code != 200:
        return "❌ Failed to reach OpenWeather geocoding API."

    geocode_data = response.json()

    if not geocode_data or len(geocode_data) == 0:
        return f"❌ City '{city}' not found."

    lat = geocode_data[0].get('lat')
    lon = geocode_data[0].get('lon')

    if not lat or not lon:
        return f"❌ Could not fetch coordinates for '{city}'."

    # Step 2: Weather
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return "❌ Failed to fetch weather data."

    weather_data = weather_response.json()

    try:
        desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        return f"🌤️ Weather in {city.title()}: {desc}, temperature: {temp}°C"
    except (KeyError, IndexError):
        return "❌ Weather data format error."
