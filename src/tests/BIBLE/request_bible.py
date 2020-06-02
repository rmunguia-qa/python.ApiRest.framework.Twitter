# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - API KEY - BIBLE
https://docs.api.bible/reference#rate-limiting

API-KEY en el HEADER

Declaramos un HEADER nuevo con la info de la API-KEY y hacemos el get de la API
'''
# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

api_key = 'cea6f41028cfc89e73f6ad596dad45c0'

new_header = {'api-key': api_key}

url = "https://api.scripture.api.bible/v1/bibles"

response = requests.get(url, headers=new_header)

print(response.text)

_response = json.loads(response.text)

print(json.dumps(_response, indent=3))




