
![Wheather Image](image.png)


--------

# Weather App

## Overview
This Python program leverages an API to fetch and display weather data based on user input, such as a city name.


------


## Prerequisites
Before using or contributing to this project, please ensure the following steps are completed:

- **Python Installation**: Make sure Python is installed on your system.
- **Library Installation**: Install the `requests` library using the command `pip install requests`.
- **Integrated Development Environment (IDE)**: It is recommended to use an IDE such as Visual Studio Code for code development.

## Implementation Steps
1. **Import Libraries**: Start by importing the `requests` library to enable HTTP requests.
2. **URL Construction**: Construct the API request URL with the provided city name and API key.
3. **API Request**: Send a GET request to the API and store the response.
4. **Response Validation**: Ensure the response status code is 200, indicating a successful request.
5. **Data Parsing**: If successful, parse the JSON data from the response.
6. **Information Extraction**: Extract relevant weather information from the JSON data.
7. **Error Handling**: Use try-except blocks to handle potential errors during the API request process.
8. **User Input**: Prompt the user to enter a city name.
9. **Function Execution**: Call the `fetch_weather` function with the user-provided city name.
10. **Display Results**: If weather data is successfully retrieved, display the weather information.
11. **Script Execution**: Ensure the main function is called when the script is executed directly.


------


## Contributors

[Ugwoke Levi](https://twitter.com/Lsoromto)
[Noah](noahayebu.na@gmail.com)
[Ernest](+234810154 0593)

## License
This project is open-sourced under the MIT license.

## Contact
For any inquiries or contributions, please contact Ugwoke Levi, Ernest, Noah.

