# -*- coding: utf-8 -*-
'''
Created on 24 abr. 2020

@author: MuNGuia10

API Rest - API KEY - NASA
https://api.nasa.gov/planetary/earth/imagery?lon={LONGITUD}&lat={LATITUD}&date={DATE}&api_key={API_KEY}

EARTH _ IMAGERY

Query Parameters
Parameter	    Type	        Default	        Description
lat	            float	        n/a	            Latitude
lon	            float	        n/a	            Longitude
dim	            float	        0.025	        width and height of image in degrees
date	        YYYY-MM-DD	    today	        date of image; if not supplied, then the most recent image (i.e., closest to today) is returned
cloud_score	    bool	        False	        [NOT CURRENTLY AVAILABLE!!!!] calculate the percentage of the image covered by clouds
api_key	        string	        DEMO_KEY	    api.nasa.gov key for expanded usage

API KEY: xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX
'''
# Importando librerías manejo Fechas
import datetime

# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

DateFormat = "%Y-%m-%d"

BackDay = datetime.date.today() - datetime.timedelta(days=2)
Day = BackDay.strftime(DateFormat)

lon = "10.75"

lat = "10.5"

dim = "0.10"

api_key = 'xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX'

url = f"https://api.nasa.gov/planetary/earth/assets?lon={lon}&lat={lat}&date={Day}&api_key={api_key}"

print(url)

response = requests.request("GET", url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))
