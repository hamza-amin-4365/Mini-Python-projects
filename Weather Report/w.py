# -*- coding: utf-8 -*-
import requests

api_key = "055318d3b4aa39e2fa287820d724d412"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant weather information
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"The current temperature in {city} is {temperature}\u00b0C.")
        print(f"The weather is {description}.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while retrieving weather data:", e)

city = input("Enter the name of a city: ")
get_weather(city)
