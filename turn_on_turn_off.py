# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 05:40:57 2018

@author: daniel
"""

intervalo_geladeira = 1800 #  = 30 minutos
temp_alvo = 18
delta_temp = 2 

from datetime import timedelta


delete_TO = 1
wait_until = datetime.now() + timedelta(hours=delete_TO)
break_loop = False
while not break_loop:
     do-your loop-stuff
     if wait_until < datetime.now() or somecondition:
          break_loop = True


