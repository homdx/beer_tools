#!/usr/bin/env python

"""
Created on Thu Aug 30 07:40:12 2018

@author: daniel
"""
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

import config
import sqlite3
import matplotlib.dates as dates
import json
import time
import logging

logging.basicConfig()

def dia_hora():
    return " -- "+time.strftime('%d/%m/%y %X')

logging.basicConfig(filename='/home/cerverja/beer_tools/cerveja.log',level=logging.DEBUG)
logging.info("o programa server.py foi iniciado"+dia_hora())

#print dados_para_grafico.data_temp_interna()

@dispatcher.add_method
def data_temp_interna():
    '''
        gera dados para o grafico da temperatura interna, inicialmente lendo do banco de dados local, pesteriormente 
        a leitura sera feita via internet
    '''
    try: 
       conn = sqlite3.connect(config.db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
       # conecta com o banco de dados
    except: 
        print 'nao conectou com o banco de dados'    
        
    cur = conn.cursor() # nao sei exatemente o que o cur faz
    cur.execute('SELECT *, tempo as "[timestamp]" FROM temperatura_interna')    
    # executa a querry sql que faz a leitura no banco de dados
    rows = cur.fetchall() 
    
    datas = [dates.date2num(i[2]) for i in rows]
    temps = [i[1] for i in rows]    
    
    data_2net = {'dates':datas,'temps':temps}
    #dados_json = json.dumps(data_2net)
    return data_2net

#print data_temp_interna()

@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


@dispatcher.add_method
def temp_interna():
    
    return data_temp_interna()
    

    #return config

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('0.0.0.0', 4000, application)
