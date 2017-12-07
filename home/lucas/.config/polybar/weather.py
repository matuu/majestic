#!/bin/python
# -*- coding: utf-8 -*-

import requests
import datetime

CITY = "3467747"
API_KEY = "3dedab9a1e2b6e1cb120ae2f421b477d"
UNITS = "Metric"
UNIT_KEY = "C"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}".format(CITY, API_KEY, UNITS))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        ID = int(float(REQ.json()["weather"][0]["id"]))
        TEMP = int(float(REQ.json()["main"]["temp"]))
        HOUR = datetime.datetime.now().hour
        
        if CURRENT == "Scattered clouds":
            CURRENT = "Nuvens dispersas"
        elif CURRENT == "Thunderstorm":
            CURRENT = "Trovoada"
        elif CURRENT == "Thunderstorm with light rain":
            CURRENT = "Trovoada com chuva fina"
        elif CURRENT == "Few clouds":
            CURRENT = "Poucas nuvens"
        elif CURRENT == "Broken clouds":
            CURRENT = "Nuvens esparsas" 
        elif CURRENT == "Clear sky":
            CURRENT = "Céu claro"                        
        
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")

if ID >= 200 and ID <= 232:
    ICON = ""
elif ID >= 310 and ID <= 531:
    ICON = ""
elif ID >= 600 and ID <= 622:
    ICON = ""
elif ID >= 701 and ID <= 761:
    ICON = ""
elif ID >= 801 and ID <= 804:
    if HOUR >= 6 and HOUR <= 19:
        ICON = ""
    else:
        ICON = ""
elif ID >= 900 and ID <= 902 or ID >= 957 and ID <= 962:
	ICON = ""
elif ID == 903 or ID == 906:
	ICON = ""
elif ID == 904:
	ICON = ""
elif ID == 905 or ID >= 951 and ID <= 956:
	ICON = ""
else:
    if HOUR >= 6 and HOUR <= 19:
        ICON = ""
    else:
        ICON = ""
#print("%%{F#555}%s %%{F-}%i °%s" % (ICON, TEMP, UNIT_KEY)) # Icon without description
print("%%{F#FFF}%s %%{F-}%s, %i°%s" % (ICON, CURRENT, TEMP, UNIT_KEY)) # Icon with description
