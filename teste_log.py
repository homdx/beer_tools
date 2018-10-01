# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 05:44:21 2018

@author: daniel
"""

import time

import logging

def dia_hora():
    return " -- "+time.strftime('%d/%m/%y %X')
    
logging.basicConfig(filename='cerveja.log',level=logging.DEBUG)
logging.info(" teste_log.py comecou a funcionar às "+dia_hora())