# -*- coding: utf-8 -*-

# Importando librería para el manejo de Directorios
import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    dateFormat = '%d/%m/%Y'
    hourFormat = "%H%M%S"

    # JsonData
    json_data = basedir + u"/data"
    data_body = basedir + u"/data/data_body"
    data_responses = basedir + u"/data/data_response"

    Environment = 'Twitter.test'

    if Environment == 'Twitter.test':
        # API
        API_hostAddressBase = "https://api.twitter.com/"

        # API_KEYS - OAUTH 1.0
        api_key = "D063saPRyoeH6u8Uy5vh05O5e"
        api_key_secret = "cXF85ASryGk6cKxGZkrEe4wlzLfdT8NeCWwCTKCCM3zaTPiSBd"

        # API KEYS - OAUTH 2.0
        access_token = "1253323820078780422-fkTbiuWXhZ11YWWrLQnzkXEe3SJN9k"
        access_token_secret = "K4PGf9yljxAGNBB5K5sDHhg838zcavzwLUr5Qyp0S7FFs"

        # API HEADERS
        API_headers = {}

        # API BODY
        API_body = {}

        # API SUB-BODY DICTIONARY
        API_subBody_dict = {}

        # API SUB-BODY ARRAY
        API_subBody_array = []

        Scenary = {
            'API_Labs1': 'labs/1',
            'API_Labs2': 'labs/2',
            'userbyId': '588227834',
            'tweetbyId': '1255874552187371525',
            'byUsername': 'by/username/assassinsspain',
            'byUsernames': 'by?usernames',
            'bySearch': 'search',
            'username1': 'Munguia12584444',
            'username2': 'assassinsspain',
            'queryUsername': 'user.fields=created_at,description,id,location,name,pinned_tweet_id,profile_image_url,'
                         'protected,public_metrics,url,username,verified',
            'queryTweet': 'tweet.fields=author_id,created_at,id,lang,possibly_sensitive,public_metrics,source,text',
            'querySearch': "Assasin's"
        }

        # DATABASE CONECTION
        DB_DRIVER = "{PostgreSQL Unicode}"
        DB_SERVER = "localhost"
        DB_PORT = "5432"
        DB_USER = "postgres"
        DB_PASS = "7434C6F7RTM"
        DB_DATABASE = "udemy_api"

    if Environment == 'Twitter.dev':
        # API
        API_hostAddressBase = "https://api.twitter.com/"

        # API KEYS - OAUTH 2.0
        api_key = "D063saPRyoeH6u8Uy5vh05O5e"
        api_key_secret = "cXF85ASryGk6cKxGZkrEe4wlzLfdT8NeCWwCTKCCM3zaTPiSBd"

        # API HEADERS
        API_headers = {}

        # API BODY
        API_body = {}

        # API SUB-BODY DICTIONARY
        API_subBody_dict = {}

        # API SUB-BODY ARRAY
        API_subBody_array = []

        Scenary = {}

        # DATABASE CONECTION
        DB_DRIVER = "{PostgreSQL Unicode}"
        DB_SERVER = "localhost"
        DB_PORT = "5432"
        DB_USER = "postgres"
        DB_PASS = "7434C6F7RTM"
        DB_DATABASE = "udemy_api"