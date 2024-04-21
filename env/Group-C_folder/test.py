import requests # Import the requests library to make HTTP requests

def fetch_weather(city):  
  
  MY_API_KEY = '555a6cd4025d5a22e5851ab0a2c2ddf2' # Define the API key provided by OpenWeatherMap
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={MY_API_KEY}'  # Construct the URL to make the API request using the provided City,and API key

  response = requests.get(url)  # Send a GET request to the API URL and store the response
  if response.status_code == 200:  # Check if the response status code is 200 (OK)
        data = response.json() # If the response is successful, parse the JSON data from the response
        weather_info = {   # Extract relevant weather information from the JSON data
            'Temperature': data['main']['temp'],
            'Description': data['weather'][0]['description'],
            'Humidity': data['main']['humidity']
        }
        return weather_info   # Return the weather information
  else:
        print('Failed to fetch weather data.')   # If the response status code is not 200, print an error message
        return None

def main():
    city = input('Enter city name: ')   # Prompt the user to city Name
    weather = fetch_weather(city)   # Call the fetch_weather function with the provided Ci
    if weather:
        print(f'Weather in {city}:')  # If weather data is successfully fetched, print the weather information
        for key, value in weather.items():
            print(f'{key}: {value}')   # Print each weather parameter and its value

if __name__ == "__main__":
    main() # Call the main function when the script is executed directly


  
# import requests
# def fetch_weather(lat, lon):
    
#   MY_API_KEY = '555a6cd4025d5a22e5851ab0a2c2ddf2'                 
#   url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={MY_API_KEY}'

#   response = requests.get(url)
#   if response.status_code == 200:
#         data = response.json()
#         weather_info = {
#             'Temperature': data['main']['temp'],
#             'Description': data['weather'][0]['description'],
#             'Humidity': data['main']['humidity']
