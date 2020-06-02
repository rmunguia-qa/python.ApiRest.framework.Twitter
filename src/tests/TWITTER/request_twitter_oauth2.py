# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - BEARER TOKEN - TWITTER
https://api.twitter.com/labs/1/users?usernames=TwitterDev&format=detailed


'''
# Importando librerías JSON
import json

# Importando librerías básicas de API REST
import requests

api_key = "D063saPRyoeH6u8Uy5vh05O5e"

api_key_secret = "cXF85ASryGk6cKxGZkrEe4wlzLfdT8NeCWwCTKCCM3zaTPiSBd"

# Solicitamos el token con la api_key: api_key_secret, como si fuera username/password
url_auth = 'https://api.twitter.com/oauth2/token'

body = {"grant_type": "client_credentials"}

bearer_response = requests.post(url_auth, auth=(api_key, api_key_secret), data=body)

auth_response = json.loads(bearer_response.text)

print(json.dumps(auth_response, indent=3))

# Una vez obtenido el BEARER TOKEN de acceso, se monta el HEADER para la siguiente consulta

header = {"Content-Type": "application/json", "Authorization": "Bearer " + auth_response['access_token']}

tweet_url = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'

tweet_response = requests.get(tweet_url, headers=header)

json_response = json.loads(tweet_response.text)

print(json.dumps(json_response, indent=3))
