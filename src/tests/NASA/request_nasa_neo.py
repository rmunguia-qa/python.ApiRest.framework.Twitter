# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - API KEY - NASA
https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}

Query Parameters
Parameter	    Type	        Default	                    Description
start_date	    YYYY-MM-DD	    none	                    Starting date for asteroid search
end_date	    YYYY-MM-DD	    7 days after start_date	    Ending date for asteroid search
api_key	        string	        DEMO_KEY	                api.nasa.gov key for expanded usage

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

api_key = 'xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX'

date = str(datetime.date.today().strftime(DateFormat))

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}E&api_key={api_key}"

response = requests.request("GET", url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))