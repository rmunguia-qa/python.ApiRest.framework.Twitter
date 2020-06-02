# -*- coding: utf-8 -*-
'''
Created on 21 abr. 2020

@author: MuNGuia10

Conexión a BBDD postgres con pyodbc

'''
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = 'localhost'
database = 'udemy_api'
username = 'postgres'
password = '7434C6F7RTM'
port = "5432"
cnxn = pyodbc.connect('DRIVER={PostgreSQL Unicode};SERVER=localhost;PORT=5432;DATABASE=udemy_api;UID=postgres;PWD=7434C6F7RTM')
cursor = cnxn.cursor()
print("Conexion OK")
