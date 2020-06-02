# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - BEARER TOKEN - GO REST
https://gorest.co.in/

Se incluye el BEARER TOKEN de OAUTH 2.0 en HEADER
'''
# Importando librerías básicas de API REST
import requests

# Importando librerías JSON
import json

url = "https://gorest.co.in/public-api/users"

header = {"Content-Type":"application/json", "Authorization": "Bearer "}

body = """{"first_name":"Ruben","last_name":"Munguia","gender":"male","email":"rmunguia100@hola.com","status":"active"}"""

response = requests.post(url, data=body, headers=header)

print(response.text)

url = "https://gorest.co.in/public-api/users"
response = requests.get(url, headers=header)

print(response.text)

_response = json.loads(response.text)

print(json.dumps(_response, indent=3))





