# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - ACCESS TOKEN - GO REST
https://gorest.co.in/

Se incluye el ACCESS TOKEN de OAUTH 1.0 en la URL
'''
# Importando librerías básicas de API REST
import requests

# Importando librerías JSON
import json

access_token = ""

url = f"https://gorest.co.in/public-api/users?_format=json&access-token={access_token}"

response = requests.get(url)

print(response.text)

_response = json.loads(response.text)

print(json.dumps(_response, indent=3))




