# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - API KEY - NASA
https://api.nasa.gov/planetary/apod?api_key={API_KEY}

Astronomy Picture of the Day
Parameter	Type	        Default	        Description
date	    YYYY-MM-DD	    today	        The date of the APOD image to retrieve
hd	        bool	        False	        Retrieve the URL for the high resolution image
api_key	    string	        DEMO_KEY	    api.nasa.gov key for expanded usage

API KEY: xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX

'''
# Importando librerías manejo Fechas
import datetime

# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

DateFormat = "%Y-%m-%d"
BackDay = datetime.date.today() - datetime.timedelta(days=0)
Day = BackDay.strftime(DateFormat)

api_key = 'xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX'

hd = "False"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={Day}&hd={hd}"

response = requests.request("GET", url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))
