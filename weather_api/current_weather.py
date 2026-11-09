import requests
from pprint import pprint
import os

url = f'http://api.openweathermap.org/data/2.5/weather'
key = os.environ.get('WEATHER_KEY')
# print(key)

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print(f"Error: {error}")
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature in {location} is {current_temp} degrees Fahrenheit.')
        
def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter a city name: ').strip()
    while len(country) == 0:
        country = input('Enter a country code (e.g., us, jp, in): ').strip()
    
    location = f'{city},{country}'
    return location

def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex
    
def get_temp(weather_data):
    try: 
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print("Error: 'main' or 'temp' key not found in the weather data.")
        return 'Unknown'
    
if __name__ == '__main__':
    main()
    
location = get_location()
weather_data, error = get_current_weather(location, key)

# {'base': 'stations',
#  'clouds': {'all': 20},
#  'cod': 200,
#  'coord': {'lat': 44.9773, 'lon': -93.2655},
#  'dt': 1794260701,
#  'id': 5037649,
#  'main': {'feels_like': 59.09,
#           'grnd_level': 981,
#           'humidity': 55,
#           'pressure': 1013,
#           'sea_level': 1013,
#           'temp': 60.73,
#           'temp_max': 63.1,
#           'temp_min': 58.98},
#  'name': 'Minneapolis',
#  'sys': {'country': 'US',
#          'id': 2012563,
#          'sunrise': 1794229351,
#          'sunset': 1794264680,
#          'type': 2},
#  'timezone': -21600,
#  'visibility': 10000,
#  'weather': [{'description': 'few clouds',
#               'icon': '02d',
#               'id': 801,
#               'main': 'Clouds'}],
#  'wind': {'deg': 250, 'speed': 9.22}}

# temp = response['main']['temp']
# city = response['name']
# print(f'The current temperature in {city} is {temp} degrees Fahrenheit.')
# The current temperature in Minneapolis is 60.73 degrees Fahrenheit.
