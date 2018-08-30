# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 08:15:49 2018

@author: daniel
"""
import config
import sqlite3
import matplotlib.dates as dates
import requests
import json
import simplejson as sjson



    
def fetch_intern_temp():
    '''
        Pega dados do rpi, para montar o gráfico de temperatura interna
    '''    
    
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "data_temp_interna",
        #"params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    teste = response['result']
    uai = json.dumps(teste)
    p_dict = sjson.loads(json.dumps(response['result']))
    return p_dict['dates'],p_dict['temps']
    
    
    
    
    
   




    
    
    
    
    
#print data_temp_interna()    
print fetch_intern_temp()