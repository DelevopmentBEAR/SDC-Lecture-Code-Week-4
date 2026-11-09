# Example URL
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

import os
import requests
from pprint import pprint
from datetime import date, datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'Minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()
#pprint(data)

list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date}, the temperature will be {temp} degrees Fahrenheit.')