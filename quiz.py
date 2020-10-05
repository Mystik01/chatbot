import requests
import time
from time import sleep
import os

from tqdm import tqdm 
from googlesearch import search

import sys

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

print("I can also tell you useful things like the weather!")
sleep(1.0)
weathercity = input("What town/city are you in? ")
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+',uk&units=metric&appid=886705b4c1182eb1c69f28eb8c520e20')


data = weather.json()

temp = data['main']['temp']
description = data['weather'][0]['description']
cityname = data['name']
weatherprint ="In {}, it is currently {}° with {}."
spinner = spinning_cursor()
for _ in range(25):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
print(weatherprint.format(cityname, temp, description))

sleep(2.0)

"""GOOGLE SEARCH"""

print("\nI can also make Google searches!")
sleep(0.5)
query = input("What do you wanna search? ")
for _ in range(25):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
print("Here are the top 5 results:")
for i in search(query, tld="co.in", num=5, stop=5):
    print(i)


musicreq = input("What song would you like to hear? Please copy the file path and paste it hear, if you need help go to:\nhttps://url.mystik01.me/help\nPlease paste file path here:  ")
os.startfile(musicreq)