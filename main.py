import requests
import json
import os
import win32com.client as wc

if __name__ == '__main__':
    speak = wc.Dispatch("SAPI.SpVoice")

    city = input("enter the city: ")
    url = f"http://api.weatherapi.com/v1/current.json?key=f9ee6feb01f146a2a61164007231708&q={city}&aqi=no"
    r = requests.get(url)
    word = json.loads(r.text)
    text = word["current"]["temp_c"]
    print(f'{text} degree celsius in {city}')
    speak.Speak(f"{text} degree celsius in {city}")


