from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    print("API Key is missing!")

def get_current_weather(city="Ahmedabad"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data= requests.get(request_url).json()
    return weather_data
if __name__ == "__main__":
    print("\n***Get Weather conditions***\n")
    city=input("Please enter city name: ")
    if not bool(city.strip()):
        city="Ahmedabad"
    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)
