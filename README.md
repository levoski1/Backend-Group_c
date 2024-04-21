# WEATHER APP

## A python program that utilizes an API to fetch weather data based on user input(e.g...city name) and display it

------

## preriquisite

In order to use this code, either for Testing purpose or Developing purpose, You must setup the following:

- install python
- install python library called requests: `pip install requests`
- Have an IDE for writing code (VSCode is a good one )


------

## Step by step Psuodo Code to achieve this project

- Import the requests library to make HTTP requests
- Construct the URL to make the API request using the provided City,and API key
- Send a GET request to the API URL and store the response
- Check if the response status code is 200 
- If the response is successful, parse the JSON data from the response
- Extract relevant weather information from the JSON data
- Return the weather information
- If the response status code is not 200, print an error message, print an error message
- Use try and except to handle errors
- Prompt the user to city Name
- Call the fetch_weather function with the provided City name
- If weather data is successfully fetched, print the weather information
- Call the main function when the script is executed directly

------

### CONTRIBUTORS
[Ugwoke Levi](https://twitter.com/Lsoromto)
[Link text](https://www.example.com)
[Link text](https://www.example.com)

![Wheather Image](image.png)

