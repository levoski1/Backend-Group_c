#!/usr/bin/python
import requests

API_key = '4045035cf84faa15b6b3e43c5c8d5ae5'

def weather(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        data = data['weather']
        print(data)
    else:
        print("Failed to retrieve weather data. Status code:", response.status_code)



weather('benin city', API_key)  # Note: City name should start with capital letter (optional)
