# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 06:28:55 2018

@author: daniel
"""
import datetime
from le_arq_temp import gettemp
import sqlite3 as sql
import config
from time import sleep




while True:
    
    temp = gettemp()
    if temp == 99999:
        temp = None
    
    time = datetime.datetime.now()
            
    data_list = [time,temp]    
    try:
        with sql.connect(config.db_path) as con:
            cur = con.cursor()
            #print 'conectou com o bd'
            cur.execute('INSERT INTO temperatura_interna (tempo,temperatura) VALUES (?,?)', data_list)
            con.commit()    
            #print 'comitou kkk'
    
    except:
        print 'deu problema no bd'
        con.rollback()
        
    sleep(config.intervalo) 
    
    
    