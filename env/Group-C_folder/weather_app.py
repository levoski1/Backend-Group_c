#!/usr/bin/python
import requests

API_key = '4045035cf84faa15b6b3e43c5c8d5ae5'

def weather_info(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
                
      
        weather_details = {
            'Temperature': data['main']['temp'],
            'Description': data['weather'][0]['description'],
            'Humidity': data['main']['humidity']
        }
        return weather_details
    
    else:
        print("Failed to retrieve weather data. Status code:", response.status_code)
        return None
# print(f"{weather_info('Enugu',API_key)} \t")

def main():
    city = input('Enter City Name: ')
    save = weather_info(city,API_key)

    if save:
        print(f'WEATHER INFORMATION ABOUT {city.upper()}')

    for key,value in weather.items():
        print(f'{key}: {value}')

if '__main__'==__name__:
    main() 
