import requests
import json

# enter your own key from the openweathermap website
api_key = ''

# function that gets the weather info about an input city from API request
def get_weather_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"API request failed with status code: {response.status_code}")
        print(response.text)  # prints the error for testing
        return None



# main
if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    weather_data = get_weather_data(city_name)

    display_weather_data(weather_data)
