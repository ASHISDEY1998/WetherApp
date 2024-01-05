import requests
import json
import pyttsx3

def getTemprature(city):
    engine=pyttsx3.init()
    url = f"https://api.weatherapi.com/v1/current.json?key=e99914ffbb924cd9ab381416240501&q={city}"
    r = requests.get(url)
    # print(r.text)
    wetherDic=json.loads(r.text)
    # print(wetherDic['current']['temp_c'])
    engine.say(f"temprature at {city} is {wetherDic['current']['temp_c']} degree celcios")
    engine.runAndWait()

if __name__ == "__main__":
    city = input('Enter the name of the city : ')
    getTemprature(city)