#!/usr/bin/python
import requests



def weather_info(city_name):
    api_key = '4045035cf84faa15b6b3e43c5c8d5ae5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        weather_details = {
            'Country':data['sys']['country'],
            'Temperature': data['main']['temp'],
            'Description': data['weather'][0]['description'],
            'Humidity': data['main']['humidity']
        }
        return weather_details
    
    else:
        print("Failed to retrieve weather data. Status code:", response.status_code)
        return None


def main():
    try:
        print()
        city = input('Enter City Name: ')
        weather = weather_info(city)

        if weather:
            print(f'Weather Information About {city} City\n')

        for key,value in weather.items():
            print(f'{key}: {value}')
        print()
    except AttributeError:
        return None

if '__main__'==__name__:
    main() 

