import requests
import json

api_key = ''

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    weather_data = get_weather_data(city_name)

    display_weather_data(weather_data)
