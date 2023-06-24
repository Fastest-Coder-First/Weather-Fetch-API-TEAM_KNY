import argparse
import requests
import openai
import json
import time
import re

def print_promt(reply):
     emoji_pattern = re.compile("[\U0001F300-\U0001F64F\u200d]|[\u2600-\u26FF]\uFE0F?|[\u2700-\u27BF]\uFE0F?|[\uD83C][\uDC00-\uDFFF]|\uD83D[\uDC00-\uDE4F\uDE80-\uDEFF]")
     for char in reply:
            if re.match(emoji_pattern, char):
                print(char, end=' ',flush = True)
            else:
                 print(char, end='',flush = True)
            #delay between each character
            time.sleep(0.03)

def main():
    #Argument parser for the input string from the user 
    parser = argparse.ArgumentParser(description='City name given by the user')
    parser.add_argument('input_string', type=str, help='City name in string')
    args = parser.parse_args()

    #This is the key for the gpt-3.5-turbo model
    openai.api_key = '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'

    #This is the prompt for the gpt-3.5-turbo model
    messages = [ {"role": "system", "content":"You are a intelligent assistant."} ]
    
    #This is the key for the openweathermap api
    weather_api_key = '9bdb65d4d211f2bb0d6b521b337dee28'

    #This is the city name given by the user
    city = args.input_string

    #This is the url for the openweathermap api
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'

    #This is the response from the openweathermap api
    response = requests.get(url)

    if response.status_code == 200:
        #This is the data from the openweathermap api
        data = response.json()

        data['main']['temp'] = (data['main']['temp'] - 273.15) #converting default kelvin value to Celcius

        message = json.dumps(data) #converting the json object into a string

        #This is the prompt for the gpt-3.5-turbo model
        message = message + " convert the temperature into celcius rounding of to two digits and create a narrative prompt with the temperature and with a bit of weather description and also what should i do and what should i carry with myself. keep the explanation concise under 40 words with emojis."

        if message :
                messages.append({"role": "user", "content": message},)

        #This is the response from the gpt-3.5-turbo model
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        #This is the reply from the gpt-3.5-turbo model
        reply = chat.choices[0].message.content

        #This is the output from the gpt-3.5-turbo model which prints the reply
        print_promt(reply)

    else:
        #This is the error message if the city name is not found
        print('Error fetching weather data')

if __name__ == '__main__':
    main()

    #//q: how to convert json object into python object in python
    #//a: https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    #// q: debug my code
    #// q: how to get weather data from openweathermap
    #// a: https://openweathermap.org/current
