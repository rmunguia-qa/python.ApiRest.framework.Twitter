# -*- coding: utf-8 -*-

# Importando clase Inicializar
from functions.Inicializar import Inicializar

# Importando librerías para Expresiones regulares
import re
# Importando librerías para Strings & Random
import string, random
# Importando librerías para Json
import json
# Importando librerías para las Requests a las APIs
import requests
# Importando librerías para TIME
import time
# Importando librerías para Pytest
import pytest
# Importando librerías para uso DataBase
import pyodbc as pyodbc
# Importando librerías para uso de datos Estructurados (JSON)
import objectpath as objectpath

# Declaramos variable del Scenario como diccionario de Datos
Scenary = {}

# Importando librería para el manejo de fecha y hora
import datetime

# Declaramos variable de Fecha Global con el formato AAAA/MM/DD
fechaGlobal = time.strftime(Inicializar.dateFormat)
# Declaramos variable de Hora Global con el formato HH:MM:SS
horaGlobal = time.strftime(Inicializar.hourFormat)


# Definimos la clase Functions para crear las funciones básicas que necesitamos
##################################################################
######################## - WEB API TEST - ########################
##################################################################
class Functions():

    ##################################################################
    ########################## - ENDPOINT - ##########################
    ##################################################################
    # Función para buscar el patrón de búsqueda Scenary (incluido en Inicializar) y traer el texto de la variable
    # que pasamos en el FEATURE
    def replace_with_context_values(self, text):
        patronBusqueda = r"(?<=Scenary:)\w+"

        variable = re.findall(str(patronBusqueda), text, re.IGNORECASE)

        for var in variable:

            if var == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
                text = re.sub('(Scenary:)' + var, dateToday, text, re.IGNORECASE)
                continue

            text = re.sub('(Scenary:)' + var, Inicializar.Scenary[var], text, re.IGNORECASE)

        return text

    # Función que devuelve el ENDPOINT completo que vamos a utilizar en el Test
    def get_full_host(self, host):
        regexHost = str(Functions.replace_with_context_values(self, host))
        self.endpoint = Inicializar.API_hostAddressBase + regexHost
        print(self.endpoint)

        return self.endpoint

    ##################################################################
    ######################## - GET  REQUEST - ########################
    ##################################################################
    # Función que devuelve un RESPONSE de la petición GET (READ FROM DATABASE) que se solicita
    # en el FEATURE
    def get_request(self):
        new_headers = Inicializar.API_headers
        self.response = requests.get(self.endpoint, headers=new_headers)

        return self.response

    ##################################################################
    ####################### - PRINT RESPONSE - #######################
    ##################################################################
    # Función que imprime por pantalla el RESPONSE de una PETICION
    def print_api_response(self):
        self.json_response = json.loads(self.response.text)

        json_string = json.dumps(self.json_response, ensure_ascii=False, indent=3).encode('utf8')

        print(json_string.decode())


    ##################################################################
    #################### - VALIDATE STATUS CODE - ####################
    ##################################################################
    # Función que realiza la validación del código de RESPONSE
    def response_is(self, code):
        print("El status code de la RESPONSE es: " + str(self.response.status_code))

        assert self.response.status_code == int(
            code), f'El status code no es el esperado {self.response.status_code} != {code}'

    # Función que realiza la validación del código de RESPONSE (200)
    def response_is_200(self):
        print("El status code de la RESPONSE es: " + str(self.response.status_code))

        assert self.response.status_code == 200, f'El status code no es el esperado {self.response.status_code} != 200'

    # Función que realiza la validación del código de RESPONSE (403)
    def response_is_404(self):
        print("El status code de la RESPONSE es: " + str(self.response.status_code))

        assert self.response.status_code == 404, f'El status code no es el esperado {self.response.status_code} != 404'

    # RESPONSE STATUS CODES:
    # 200 (OK) / 201 (CREATED) / 202 (ACCEPTED) / 204 (NO CONTENT)
    # 301 (MOVED PERMANENTLY) / 302 (FOUND) / 303 (SEE OTHER) / 304 (NOT MODIFIED) / 307 (TEMPORARY REDIRECT)
    # 400 (BAD REQUEST) / 401 (UNAUTHORIZED) / 403 (FORBIDDEN) / 404 (NOT FOUND) / 405 (METHOD NOT ALLOWED)
    # 406 (NOT ACCEPTABLE) / 412 (PRECONDITION FAILED) / 415 (UNSUPPORTED MEDIA TYPE)
    # 500 (INTERNAL SERVER ERROR) / 501 (NOT IMPLEMENTED)

    ##################################################################
    ######################## - BODY  VALUES - ########################
    ##################################################################
    # Función que devuelve el BODY seteado correctamente de una PETICION
    def set_body_values(self, entity, value):
        # Función que asigna valores RANDOM
        def set_random_values(self):
            letters = string.ascii_lowercase

            return ''.join(random.choice(letters) for i in range(10))

        value = Functions.replace_with_query_values(self, value)

        if value.lower() == "random":
            value = set_random_values(self)
            if entity.lower() == "email":
                value = set_random_values(self) + "@gmail.com"
            # AÑADIR ENTIDADES QUE SEAN MÁS UTILIZADAS

        Inicializar.API_body[entity] = value

        self.new_body = Inicializar.API_body

        json_string = json.dumps(self.new_body, ensure_ascii=False, indent=4).encode('utf8')

        print(json_string.decode())

        return self.new_body

    # Función que devuelve los valores de un DICCIONARIO de DATOS seteado
    def set_sub_body_dict_values(self, entity, value):
        Inicializar.API_subBody_dict[entity] = value
        print((json.dumps(Inicializar.API_subBody_dict, indent=4)))

        return Inicializar.API_subBody_dict

    # Función que devuelve el DICCIONARIO de DATOS seteado con los valores de la función
    # anterior "set_sub_body_dict_values"
    def set_sub_body_dict(self, key):
        Inicializar.API_body[key] = Inicializar.API_subBody_dict
        print((json.dumps(self.new_body, indent=4)))

        Inicializar.API_subBody_dict = {}

        return Inicializar.API_subBody_dict

    # Función que devuelve los valores de un ARRAY de DATOS seteado
    def set_sub_body_array_values(self, value):
        Inicializar.API_subBody_array.append(value)

        print(Inicializar.API_subBody_array)

        return Inicializar.API_subBody_array

    # Función que devuelve el ARRAY de DATOS seteado con los valores de la función
    # anterior "set_sub_body_array_values"
    def set_sub_body_array(self, key):
        Inicializar.API_body[key] = Inicializar.API_subBody_array
        print((json.dumps(self.new_body, indent=4)))

        Inicializar.API_subBody_array = []

        return Inicializar.API_subBody_array

    ##################################################################
    ######################### - JSON  DATA - #########################
    ##################################################################
    # Función que devuelve un JSON formateado para realizar una PETICION
    def get_json_data(self, file):
        json_path = Inicializar.json_data + '/' + file + '.json'
        try:
            with open(json_path, "r", encoding='utf-8') as read_file:
                self.json_strings = json.loads(read_file.read())
                print("Función get_json_data: Directorio JSON file es " + json_path)
                return self.json_strings

        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"Función get_json_data: No se ha encontrado el fichero " + file)

    # Función que setea el API BODY de la PETICION como un JSON
    def set_initial_json_body(self, file):
        self.new_json_body = Functions.get_json_data(self, file)

        Inicializar.API_body = self.new_json_body

        print((json.dumps(Inicializar.API_body, indent=4)))


    # Función que realiza la comparación de valores del RESPONSE (JSON)
    def new_compare_entity_values(self, path, expected):
        expected = str(expected)

        try:
            tree_obj = objectpath.Tree(self.json_response)
            path_Value = tree_obj.execute('$.' + path)

            if "generator object Tree.execute" in str(path_Value):
                entity = tuple(tree_obj.execute('$.' + path))
                path_Value = ','.join(map(str, entity))

            print(path_Value)

        except TypeError:
            entity = tuple(str(tree_obj.execute('$.' + path)))
            path_Value = ''.join(map(str, entity))

        except SyntaxError:
            path_Value = str(None)

            print("Función new_compare_entity_values: No se ha podido obtener ningún valor en la búsqueda!")

        if expected == "NOT NULL":
            assert str(path_Value) != None, f"El valor de la entidad es NULL: {path_Value} != {expected}"
            return

        elif expected == "NULL":
            assert str(path_Value) == None, f"El valor de la entidad no es NULL: {path_Value} != {expected}"
            return

        else:
            assert str(path_Value) == str(expected), f"El valor no es el esperado {path}: {path_Value} != {expected}"


    ##################################################################
    ####################### - ASSERT  VALUES - #######################
    ##################################################################
    # Función que valida una entidad concreta del JSON RESPONSE de la PETICION que se solicita en el FEATURE
    def assert_json_response_expected(self, entity, expected, subPath=0):
        self.json_response = json.loads(self.response.text)
        path_Value = self.json_response[entity]

        if expected == "NOT NULL":
            assert str(path_Value) != None, f"El valor de la entidad es NULL: {path_Value} != {expected}"
            return

        if expected == "NULL":
            assert str(path_Value) == None, f"El valor de la entidad no es NULL: {path_Value} != {expected}"
            return

        lists = isinstance(path_Value, list)
        dicts = isinstance(path_Value, dict)

        if lists:
            path_Value = self.json_response[entity][int(subPath)]

        if dicts:
            path_Value = self.json_response[entity][subPath]

        assert str(path_Value) == expected, f"El valor de la entidad no es el esperado: {path_Value} != {expected}"

    # Función que valida el JSON RESPONSE de la PETICION que se solicita en el FEATURE
    def expected_results_value(self, file):
        self.json_strings = Functions.get_json_data(self, file)

        try:
            assert self.json_strings == self.json_response
            print(u"Se ha comprobado el valor esperado")

            verify = True

        except AssertionError:
            verify = False

            print("La respuesta del servicio ha sido: ")
            print(json.dumps(self.json_response, indent=4))
            print("La respuesta almacenada debe tener algún error, revísalo: ")
            print(json.dumps(self.json_strings, indent=4))

            assert verify == True

    ##################################################################
    ######################## - POST REQUEST - ########################
    ##################################################################
    # Función que devuelve un RESPONSE de la petición POST (CREATE A NEW RECORD IN THE DATABASE) que se solicita
    # en el FEATURE
    def post_request(self):
        new_headers = Inicializar.API_headers

        print(self.new_json_body)
        self.response = requests.post(self.endpoint, headers=new_headers, data=json.dumps(self.new_json_body))

        return self.response

    ##################################################################
    ######################## - PUT  REQUEST - ########################
    ##################################################################
    # Función que devuelve un RESPONSE de la PETICION PUT (UPDATE/REPLACE ROW IN DATABASE) que se solicita
    # en el FEATURE
    def put_request(self):
        new_headers = Inicializar.API_headers

        print(self.new_body)
        self.response = requests.put(self.endpoint, headers=new_headers, data=json.dumps(self.new_body))

        return self.response

    ##################################################################
    ####################### - PATCH  REQUEST - #######################
    ##################################################################
    # Función que devuelve un RESPONSE de la PETICION PATCH (UPDATE/MODIFY ROW IN DATABASE) que se solicita
    # en el FEATURE
    def patch_request(self):
        new_headers = Inicializar.API_headers

        print(self.new_body)
        self.response = requests.patch(self.endpoint, headers=new_headers, data=json.dumps(self.new_body))

        return self.response

    ##################################################################
    ####################### - DELETE REQUEST - #######################
    ##################################################################
    # Función que devuelve un RESPONSE de la PETICION DELETE (DELETE FROM THE DATABASE) que se solicita
    # en el FEATURE
    def delete_request(self):
        new_headers = Inicializar.API_headers
        self.response = requests.delete(self.endpoint, headers=new_headers)

        return self.response

    ##################################################################
    # ##### ##### ##### #####  - DATABASE -  # ##### ##### ##### #####
    ##################################################################
    # Función que sirve para realizar uns QUERY sobre una DATABASE externa (Ejemplo PostgreSQL)
    def pyodbc_query(self, _query):
        self.conn = Functions.pyodbc_conn(self)

        if self.conn is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.description

                columns = [column[0] for column in self.Result]
                result = []

                for row in self.cursor.fetchall():
                    result.append(dict(zip(columns, row)))
                print(result[0])

                self.QUERY = result[0]

                return self.QUERY

            except (pyodbc.Error) as error:
                pytest.skip(f"Error en la consulta {error}")

            finally:
                if (self.conn):
                    self.cursor.close()
                    self.conn.close()
                    print("Función pyodbc_query: Se ha cerrado la conexión")


    # Función para buscar el patrón de búsqueda Scenary (incluido en Inicializar) y traer el texto de la variable
    # que pasamos en el FEATURE
    def replace_with_query_values(self, text):
        patronBusqueda = r"(?<=Query:)\w+"

        variable = re.findall(str(patronBusqueda), text, re.IGNORECASE)

        for var in variable:
            text = re.sub('(Query:)' + var, str(self.QUERY[var]), text, re.IGNORECASE)

        return text


    # Función que sirve para realizar la conexión a una DATABASE externa (Ejemplo PostgreSQL)
    def pyodbc_conn(self, _dbdriver=Inicializar.DB_DRIVER, _dbserver=Inicializar.DB_SERVER, _dbport=Inicializar.DB_PORT,
                    _dbname=Inicializar.DB_DATABASE, _dbuser=Inicializar.DB_USER, _dbpass=Inicializar.DB_PASS):
        try:
            self.conn = pyodbc.connect(
                'DRIVER=' + _dbdriver + ';'
                'SERVER=' + _dbserver + ';'
                'PORT=' + _dbport + ';'                                      
                'DATABASE=' + _dbname + ';'
                'UID=' + _dbuser + ';'
                'PWD=' + _dbpass + ';')

            self.cursor = self.conn.cursor()
            print("Conexión DataBase OK")

        except (pyodbc.OperationalError) as error:
            self.conn = None
            self.cursor = None
            pytest.skip("Error en connection strings: " + str(error))

        return self.conn