# -*- coding: utf-8 -*-
'''
Created on 24 abr. 2020

@author: MuNGuia10

API Rest - API KEY - NASA
https://api.nasa.gov/EPIC/api/natural/images?api_key={API_KEY}

EPIC - Earth Polychromatic Imaging Camera

Querying by Date(s)
Parameter	        Type	        Default	                        Description
natural	            string	        Most Recent Natural Color	    Metadata on the most recent date of natural color imagery.
natural/date	    YYYY-MM-DD	    Most Recent Available	        Metadata for natural color imagery available for a given date.
natural/all	        string	        Dates for Natural Color	        A listing of all dates with available natural color imagery.
natural/available	string	        Dates for Natural Color	        Alternate listing of all dates with available natural color imagery.
enhanced	        string	        Most Recent Enhanced Color	    Metadata on the most recent date of enhanced color imagery.
enhanced/date	    YYYY-MM-DD	    Most Recent Available	        Metadata for enhanced color imagery for a given date.
enhanced/all	    string	        Dates for Enhanced Imagery	    A listing of all dates with available enhanced color imagery.
enhanced/available	string	        Dates for Enhanced Imagery	    Alternate listing of all dates with available enhanced color imagery.
api_key	            string	        DEMO_KEY	                    API key from api.nasa.gov for expanded usage

API KEY: xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX
'''
# Importando librerías básicas de API REST
import requests

year = "2019"
month = "05"
day = "30"

hour = "011359"

api_key = 'xxmHu7Aohyq2l1htswuHDSJ7W3b79yp5nIawKBhX'

url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/epic_1b_{year}{month}{day}{hour}.png?api_key={api_key}"

print(url)

response = requests.request("GET", url)