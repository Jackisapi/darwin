import pyowm
import news
import requests
import playsound
import os
# from duckduckgo_search import DDGS
from gpt4all import GPT4All


def weather(location, temp_type, key=os.getenv("open_weather")):
    owm = pyowm.OWM(key)
    weather_mgr = owm.weather_manager()
    observation = weather_mgr.weather_at_place(location)
    temperature = observation.weather.temperature(temp_type)["temp"]
    humidity = observation.weather.humidity
    wind = observation.weather.wind()['speed']
    return f"The temperature is {temperature}, With a Humidity of {humidity}% ,and a wind speed of {wind}"


def npr():
    newsFile = requests.get(news.xml2url(news.podFetch()))
    open('file.mp3', 'wb').write(newsFile.content)
    playsound.playsound('file.mp3', True)


def search(quere, model):
    model = GPT4All(model)
    with model.chat_session():
        response = model.generate(prompt=quere)
        return response

