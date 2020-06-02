# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - API KEY - SWAGGER PETSTORE
https://petstore.swagger.io/v2/pet/

'''
# Importando librerías manejo Tiempo
import time

# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

id = 1

url_pet_id = f"https://petstore.swagger.io/v2/pet/{id}"

print(url_pet_id)

response = requests.get(url_pet_id)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))

time.sleep(1)

# Validaciones sobre la REQUEST
assert json_response['id'] == 1, "El id no coincide"

# Validación de DICCIONARIO {} en el JSON
#assert json_response['category']['id'] == 0, "El category id no coincide"

#assert json_response['status'] != "sold", "El status no es SOLD"

#assert json_response['category']['name'] == 'dogs', "El category name no coincide"

#assert json_response['name'] == 'teroSr', "El name no coincide"

# Validación de ARRAYS [] en el JSON
#assert json_response['photoUrls'][0] == 'string', "El URL no coincide"

# Validación de DICCIONARIO {} contenido en ARRAY []
#assert json_response['tags'][0]['id'] == 1, "El tag id no coincide"

#assert json_response['tags'][0]['name'] == 'streetdog', "El tag name no coincide"

#assert json_response['status'] == 'available', "El status no coincide"

# Validar un campo que tiene dato, por si el dato no es único
#assert json_response['id'] != None, "El id está vacio"

status = "sold"

url_pet_status = f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}"

print(url_pet_status)

response = requests.get(url_pet_status)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))