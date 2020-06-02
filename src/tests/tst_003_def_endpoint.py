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

API_hostAddressBase = u'http:\\UrlDeLaWebapi.com'
partHost = "\Endpoint\Scenario:Today"

def get_full_host(_PartHost):
    _RegexPartHost = str(replace_with_context_values(_PartHost))
    _endpoint = API_hostAddressBase + _RegexPartHost
    print(_endpoint)

    return _endpoint

def replace_with_context_values(text):
    PatronBusqueda = r"(?<=Scenario:)\w+"

    variable = re.findall(str(PatronBusqueda), text, re.IGNORECASE)

    for var in variable:

        if var == 'Today':
            dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
            text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
            continue

    return text

endpoint = get_full_host(partHost)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
