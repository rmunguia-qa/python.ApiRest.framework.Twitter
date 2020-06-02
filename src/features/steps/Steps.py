# -*- coding: utf-8 -*-

# Importando clase Functions e Inicializar
from functions.Functions import Functions
from functions.Inicializar import Inicializar

# Importando librerías BDD - Behave
from behave import *

import requests
import json

# Use matcher ("Regular Expresions")
use_step_matcher("re")

# Definición de la clase de Steps
class StepsDefinitions():

##################################################################
########################## - WEB  API - ##########################
##################################################################

    @step("Conectamos con el endpoint (.*)")
    def step_impl(self, host):
        self._endpoint = Functions.get_full_host(self, host)

        return self._endpoint

    @when("Realizamos un GET al endpoint")
    def step_impl(self):
        self.response = Functions.get_request(self)

        return self.response

    @then("Mostramos el RESPONSE por pantalla")
    def step_impl(self):
        Functions.print_api_response(self)

    @step("El status code del RESPONSE es (.*)")
    def step_impl(self, code):
        Functions.response_is(self, code)

    @step("El status code del RESPONSE debe ser 200 OK")
    def step_impl(self):
        Functions.response_is_200(self)

    @step("El status code del RESPONSE debe ser 404 NOT FOUND")
    def step_impl(self):
        Functions.response_is_404(self)

    @then("Asignar a la entidad (.*) el valor (.*)")
    def step_impl(self, entity, value):
        Functions.set_body_values(self, entity, value)

    @when("Asignar el body con el JSON (.*)")
    def step_impl(self, file):
        Functions.set_initial_json_body(self, file)

    @when("Realizamos un PUT al endpoint")
    def step_impl(self):
        Functions.put_request(self)

    @when("Realizamos un POST al endpoint")
    def step_impl(self):
        Functions.post_request(self)

    @step("Validamos el JSON RESPONSE de la entidad (.*) con el valor (.*)")
    def step_impl(self, entity, expected_value):
        Functions.assert_json_response_expected(self, entity, expected_value)

    @step("Validamos el JSON RESPONSE en la que la entidad (.*) en el path (.*) con el valor (.*)")
    def step_impl(self, entity, subPath, expected_value):
        Functions.assert_json_response_expected(self, entity, expected_value, subPath)

    @then("Los elementos (.*) muestran los valores (.*)")
    def step_impl(self, entity, expected_value):
        for row in self.table:
            print(row)

            entity = row['Entity']
            value = row['Value']

            Functions.assert_json_response_expected(self, entity, value)

    @step("Comprobamos el elemento (.*) en el path (.*) muestran los valores (.*)")
    def step_impl(self, entity, subPath, expected):
        for row in self.table:
            print(row)

            entity = row['Entity']
            subPath = row['Path']
            value = row['Value']

            Functions.assert_json_response_expected(self, entity, value, subPath)

    @step("Comparar JSON file Response (.*) con Response")
    def step_impl(self, file):
        Functions.expected_results_value(self, file)

    @step("Asignar al sub-body (.*) el valor (.*)")
    def step_impl(self, entity, value):
        Functions.set_sub_body_dict_values(self, entity, value)

    @step("Añadir valores al sub-body (.*)")
    def step_impl(self, key):
        Functions.set_sub_body_dict(self, key)

    @step("Asignar al sub-array el valor (.*)")
    def step_impl(self, value):
        Functions.set_sub_body_array_values(self, value)

    @step("Añadir valores al sub-array (.*)")
    def step_impl(self, key):
        Functions.set_sub_body_array(self, key)

    @then('Hacer esta SQL Query """(.*)"""')
    def step_impl(self, _query):
        self._result = Functions.pyodbc_query(self, _query)

    @then("Asignar la entidad (.*) con el valor (.*)")
    def step_impl(self, entity, value):
        Functions.set_body_values(self, entity, value)

    @step("Login en Twitter con credenciales OAuth 2.0")
    def step_impl(self):
        auth_body = {"grant_type": "client_credentials"}
        
        bearer_response = requests.post(Inicializar.API_hostAddressBase + "oauth2/token",
                                        auth=(Inicializar.api_key, Inicializar.api_key_secret), data=auth_body)
        
        auth_response = json.loads(bearer_response.text)
        print(json.dumps(auth_response, indent=3))

        Inicializar.API_headers["Authorization"] = "Bearer " + auth_response['access_token']

    @step("Verificar que el RESPONSE de la entidad (.*) tenga el valor (.*)")
    def step_impl(self, entity, expected):
        Functions.new_compare_entity_values(self, entity, expected)

    @step("Verificar que (.*) tenga el valor (.*)")
    def step_impl(self, entity, value):
        for row in self.table:
            print(row)

            entity = row['Entity']
            value = row['Value']

            Functions.new_compare_entity_values(self, entity, value)
