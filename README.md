# Weather Forecasting tool using Python and Github Copilot


The [Python](https://www.python.org/) script fetches weather data for the given city and generates a conversational response with temperature information and weather description with [Github Copilot](https://github.com/features/copilot).

# Brief Explanation:

The script starts by importing the necessary modules: argparse for parsing command-line arguments, requests for making HTTP requests, openai for using the OpenAI API, json for working with JSON data, time for adding delays in printing, and re for regular expression operations .
## Installation

Install the packages using [pip](https://pip.pypa.io/en/stable/getting-started/) from your favorite Terminal and run these commands.
```sh
pip install requests
```
```sh
pip install regex
```
```sh
pip install argparse
```
```sh
pip install openai
```
```sh
pip install json
```

## Getting started
Run this command in your terminal to start
```sh
python final.py "<city_name>"
```

## Working

### Fetching Hyderabad weather
![Example 1](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/ex1.png)

### Fetching Mumbai weather
![Example 2](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/ex2.png)
> Note: Replace <city_name> with the input
## WorkFlow:
![work flow](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/workflow.png)
- Parses the command-line argument for the city name provided by the user.
- Sets the [OpenAI API](https://platform.openai.com/) key and defines the initial message for the GPT-3.5 Turbo model.
- Sets the weather API key of open weather website and constructs the URL to fetch weather data for the specified city.
- Sends a GET request to the [OpenWeatherMap API](https://openweathermap.org/api) and checks the response status code.
- If the response is successful (status code:200), it retrieves the weather data, converts the temperature to Celsius, and creates a JSON string prompt for the GPT-3.5 Turbo model.
- Uses the OpenAI API to generate an appropriate response on weather based on the city of user's choice.
- Retrieves the reply from the model and prints it.
- If the response status code is not 200, it prints an error message.
## GitHub Copilot Usage

### GitHub Copilot can assist in various scenarios throughout the codebase


#### API Request URL Building:
Copilot can provide suggestions in constructing the API request URL, ensuring the correct formatting.
![suggestions](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/2.png)
# 
#### Error Handling and Exception Handling:
Copilot can provide suggestions for error handling and exception handling in the get_weather_data function, helping to handle different errors.
![data parsing](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/1.png)
# 
#### Weather Information Formatting:
Copilot can suggest improvements in formatting and displaying the weather information and suggest the code.
![code suggest](https://github.com/Fastest-Coder-First/Weather-Fetch-API-TEAM_KNY/blob/main/3.png)
#
#### Variable Naming and Code Organization:
Copilot can provide suggestions for variable naming and code organization, helping to improve the readability and maintainability of the codebase.
