# -*- coding: utf-8 -*-
'''
Created on 23 abr. 2020

@author: MuNGuia10

API Rest - OAUTH TOKEN - TWITTER
https://api.twitter.com/labs/1/users?usernames={USERNAMES}&format=detailed

'''
# Importando librerías JSON
import json
# Importando librerías básicas de API REST
import requests

url = f"https://api.twitter.com/labs/1/users?usernames=TwitterDev&format=detailed"

Auth = """OAuth oauth_consumer_key="D063saPRyoeH6u8Uy5vh05O5e",oauth_token="1253323820078780422-fkTbiuWXhZ11YWWrLQnzkXEe3SJN9k",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1588408525",oauth_nonce="FpL8qUXuOWp",oauth_version="1.0",oauth_signature="JvZeiCMiBIORsHYqJGHGy7oUBaw%3D"""

headers = {"Content-Type": "application/json", "accept": "application/json", "Authorization": Auth}

response = requests.get(url, headers=headers)

json_response = json.loads(response.text)

print(json.dumps(json_response, indent=3))