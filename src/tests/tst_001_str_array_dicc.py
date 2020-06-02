# -*- coding: utf-8 -*-
'''
Created on 21 abr. 2020

@author: MuNGuia10

Formateo strings: test_001_string

Arreglo de Datos: test_001_arrays
https://devcode.la/tutoriales/listas-python/

Diccionario Datos: test_001_dictionary
https://devcode.la/tutoriales/diccionarios-en-python/

'''
# Importando librerías básicas de Selenium
import unittest

class Test_001(unittest.TestCase):

    def setUp(self):
        pass

    # Formateando strings
    def test_001_string(self):
        NombreStr = "Ruben"
        print(f'Hola {NombreStr}')

        Nombre = 205
        print(f'Hola {(str(Nombre))}') # Convertir la variable con un entero (por ejemplo) a string con "str"

    """ Trabajamos con arrays
    # Array es una estructura de datos y un tipo de dato en python con carecterísticas especiales. Nos permiten
    # almacenar cualquier tipo de valor: enteros, cadenas y hasta otras funciones, ejemplo... 
    """
    def test_001_arrays(self):
        Nombre = "Ruben"
        Nombre2 = "Juanito Valderrama"
        array = ['Venezuela', 'Argentina', 'Chile', 'Perú']
        array.append('Bolivia') # añadir valor a un array

        #print(array)
        #print(array[0])
        #print(array[4])
        i = 0
        for pais in array:
            print(pais)
            if pais == "Argentina":
                print(f'{Nombre}, vive en {pais}')
                continue  # se pasa al siguiente elemento

            if pais == "Chile":
                array[i] = "Aguante Chile!!!"
                print(array[i])
                continue  # se pasa al siguiente elemento
            if pais == "Perú":
                print(f'{Nombre2}, vive en {pais}')
                break # rompe el bucle
            i++1
        # Validar = isinstance(array, list)

    """ Trabajamos con diccionarios de datos
    # Diccionario es una estructura de datos y un tipo de dato en Python con características especiales. Nos permite 
    # almacenar cualquier tipo de valor: enteros, cadenas, listas y hasta otras funciones. También nos permiten 
    # identificar cada elemento por una clave (Key).
    """
    def test_001_dictionary(self):
        diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript']}

        Nombre = diccionario['nombre']
        print(f'Hola, {Nombre}')

        diccionario['nombre'] = "Ruben" # Actualizamos el valor de la key 'nombre' y se imprime

        Nombre = diccionario['nombre']
        print(f'Hola, {Nombre}')

        print(diccionario)

    def tearDown(self):
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
