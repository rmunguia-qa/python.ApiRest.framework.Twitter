# -*- coding: utf-8 -*-
'''
Created on 24 abr. 2020

@author: MuNGuia10

API Rest - API KEY - NASA
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={YYYY-M-D}&api_key={API_KEY}

Mars Rover Photos - This API is designed to collect image data gathered by NASA's Curiosity, Opportunity,
and Spirit rovers on Mars

Querying by Earth date
Parameter	        Type	        Default	        Description
earth_date	        YYYY-MM-DD	    none	        corresponding date on earth for the given sol
camera	            string	        all	            see table above for abbreviations
page	            int	            1	            25 items per page returned
api_key	            string	        DEMO_KEY	    api.nasa.gov key for expanded usage

API KEY: xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX
'''
# Importando librerías básicas de API REST
import requests

# Importando librerías JSON
import json

year = "2020"
month = "4"
day = "23"

api_key = 'xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX'

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={year}-{month}-{day}&api_key={api_key}"

print(url)

response = requests.request("GET", url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))