# -*- coding: utf-8 -*-
'''
Created on 24 abr. 2020

@author: MuNGuia10

API Rest - API KEY - SWAGGER PETSTORE
https://petstore.swagger.io/v2/store/

'''
# Importando librerías manejo Tiempo
import time

# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

url = f"https://petstore.swagger.io/v2/store/inventory"

response = requests.get(url)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))