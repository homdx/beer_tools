# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 05:40:57 2018

@author: daniel
"""

'''
intervalo_geladeira = 1800 #  = 30 minutos
temp_alvo = 18
delta_temp = 2 
'''
#######
# tenho que simular o gettemp()
#####3


#from datetime import timedelta,now
import datetime 
import config
import time
import le_arq_temp
import liga_geladeira
#temp_geladeira = le_arq_temp.gettemp()
# a variavel temp_geladeira serve apenas para teste no desenvolvimento
#temp_geladeira = 20

inter_geladeira = config.intervalo_geladeira 
delta_temperatura = config.delta_temperatura
temperatura_alvo = config.temperatura_alvo

#wait_until = datetime.time() + datetime.timedelta(seconds=delete_TO)
#break_loop = False
#print datetime.datetime.now()
#print datetime.datetime.now() + datetime.timedelta(seconds=30)


liga_gel = False
#date_turn_on

while True:
    if ( le_arq_temp.gettemp()  >= (delta_temperatura + temperatura_alvo)) and (liga_gel == False) :
        date_turn_on = datetime.datetime.now()
        liga_gel = True
        
        ## aqui ficarah o comando para ligar a geladeira
        liga_geladeira.liga_geladeira() 
        #print 'a geladeira foi ligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    if ( le_arq_temp.gettemp()  <= (delta_temperatura - temperatura_alvo)) and (liga_gel == True) :  
        liga_gel = False
        ### comando para desligar a geladeira
        liga_geladeira.desliga_geladeira()
        #print 'a geladeira foi desligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    if (date_turn_on+datetime.timedelta(seconds=10) < datetime.datetime.now()) and (liga_gel == True):
        liga_gel = False
        ### comando para desligar a geladeira
        liga_geladeira.desliga_geladeira()

        #print 'a geladeira foi desligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    #print datetime.datetime.now()    
    time.sleep(2) 






#while not break_loop:
     #do-your loop-stuff
     
     
#     if wait_until < datetime.now() or somecondition:
#          break_loop = True


