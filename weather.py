from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    print("API Key is missing!")

def get_current_weather(city="Ahmedabad"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data


