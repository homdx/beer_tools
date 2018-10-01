# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:21:27 2018

@author: daniel
"""
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import config
import sqlite3
import dados_para_grafico
from itertools import izip
import json



# make up some data
#x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
#y = [i+random.gauss(0,1) for i,_ in enumerate(x)]


#myFmt = mdates.DateFormatter('%d')



#conn = sqlite3.connect(config.db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
try: 
#    conn = sqlite3.connect(config.db_path)
     conn = sqlite3.connect(config.db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
   
except: 
    print 'não conectou com o banco de dados'

cur = conn.cursor()
#cur.execute('SELECT * FROM temperatura_interna')
cur.execute('SELECT *, tempo as "[timestamp]" FROM temperatura_interna')


rows = cur.fetchall()

#print type(rows)
#print rows

#dates = []
#print [i[2] for i in rows]

dates = [dates.date2num(i[2]) for i in rows]
temps = [i[1] for i in rows]

#print dates

dates_list = []
for row in rows:
    dates_list.append(type(row[2]))
    
#print dates_list[0]    
#date_list = dates.date2num(dates_list[0].now())
#print date_list

#print dates,temps


#plt.plot([],[])
#plt.plot(dates,temps)
#plt.scatter(dates, temps)
#plt.plot_date(dates, temps)
#myFmt = dates.DateFormatter('%H:%M')
#plt.gca().xaxis.set_major_formatter(myFmt)

#rule = dates.rrulewrapper(DAILY)
#loc = dates.RRuleLocator(rule)
#formatter = dates.DateFormatter('%H:%M')
#print dados_para_grafico.data_temp_interna()

#dados = zip(dados_para_grafico.data_temp_interna()[0],dados_para_grafico.data_temp_interna()[1])

#print dados




data_2net = {'dates':dados_para_grafico.data_temp_interna()[0],'temps':dados_para_grafico.data_temp_interna()[1]}

#print data_2net

dados_json = json.dumps(data_2net)

#print dados_json

########### internet


#print dados_json

ishi = json.loads(dados_json)

print ishi['temps']





#i = iter()



fig,ax1 = plt.subplots()

#plt.plot_date(dates,temps,'%H:%M',xdate=True,ydate=False,hold=None,date=None)

plt.plot_date(ishi['dates'],ishi['temps'])

#plt.plot_date(dates,temps)
#plt.plot_date(dados_para_grafico.data_temp_interna()[0],dados_para_grafico.data_temp_interna()[1])

#ax1 = fig.add_subplot(111)
#ax1.plot_date(dates,temps)
#ax1.format_xdata = dates.DateFormatter('%H:%M')
#ax1.xaxis.set_major_formatter(formatter)
#plt.gcf().autofmt_xdate()

plt.show()


#matplotlib.pyplot.plot_date(dates, values)
'''
plt.plot(dates,temps)
plt.gcf().autofmt_xdate()
myFmt = dates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
'''
#plt.close()