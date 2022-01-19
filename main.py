import os
import requests
from datetime import datetime

user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")
#actual link = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check the City name".format(location))

else:
    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("------------------------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("------------------------------------------------------")

    print("Current temperature   : {:.2f} deg C".format(temp_city))
    print("Weather Desc          : ", weather_desc)
    print("Humidity              : ", humidity, '%')
    print("Wind Speed            : ", wind_spd, 'kmph')

