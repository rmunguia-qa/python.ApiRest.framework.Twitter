# -*- coding: utf-8 -*-
'''
Created on 21 abr. 2020

@author: MuNGuia10

Regex - Expresiones Regulares
https://docs.hektorprofe.net/python/funcionalidades-avanzadas/expresiones-regulares/

'''
# Importando librerías básicas de Selenium
import unittest

import re
import datetime

class Test_002(unittest.TestCase):

    def setUp(self):
        pass

    # Formateando strings
    def test_002_regex(self):
        # FINDALL - re.findall: busca todas las coincidencias en una cadena
        text = "ID: 2541 Esta es una de las mejores clases de Testing en Udemy expresion 2541684"

        matching = re.findall('2541684|CLASES', text, re.IGNORECASE)

        for result in matching:
            print(result)

        print("########## REGEX FINDALL ##########")

        # SEARCH - re.search: busca un patrón en otra cadena

        text = "ID: 2541 Esta es una de las mejores clases de Testing en Udemy expresion 2541684"

        search = re.search('2541684', text, re.IGNORECASE)

        # Posición donde empieza la coincidencia
        print(search.start())
        # Posición donde termina la coincidencia
        print(search.end())
        # Tupla con posiciones donde empieza y termina la coincidencia
        print(search.span())
        # Cadena sobre la que se ha realizado la búsqueda
        # print(search.string)

        print(search)

        if search:
            print("Se ha encontrado el valor")
            # SUB - re.sub: sustituye todas las coincidencias en una cadena
            # Si se encuentra el valor, se reemplaza por *******
            text = re.sub('2541684', '*******', text, re.IGNORECASE)
            print(text)

        else:
            print("No se ha encontrado el valor")

        print("########## REGEX SEARCH ##########")

        # SPLIT - re.split: divide una cadena a partit de un patrón:
        text = "ID: 2541 Esta es una de las mejores clases de Testing en Udemy expresion 2541684"

        split = re.split('Udemy', text)

        for result in split:
            print(result)

            if result == '2541684':
                print("Se ha encontrado el código")
                break

        print("########## REGEX SPLIT ##########")

        Scenario = {}

        text = "Este texto contiene el valor del Id:5000 ahora"

        PatronBusqueda = r"(?<=Id:)\w+"

        variable = re.findall(str(PatronBusqueda), text, re.IGNORECASE)
        print(variable)

        Scenario['btpecnro'] = str(variable[0])

        print("Se ha almacenado btpecnro = " + Scenario['btpecnro'])

        print("########## REGEX PATRON BUSQUEDA 1 ##########")

        text = "Este texto contiene el valor del Scenario:HOY ahora"

        PatronBusqueda = r"(?<=Scenario:)\w+"

        variable = re.findall(str(PatronBusqueda), text, re.IGNORECASE)
        print(variable)

        for var in variable:

            if var == 'HOY':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
                text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
                continue

        print(text)

        print("########## REGEX PATRON BUSQUEDA 2 ##########")

    def tearDown(self):
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
