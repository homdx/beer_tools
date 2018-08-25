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


# make up some data
#x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]


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
print [i[2] for i in rows]

dates = [dates.date2num(i[2]) for i in rows]
temps = [i[1] for i in rows]

#print dates,temps

dates_list = []
for row in rows:
    dates_list.append(type(row[2]))
    
#print dates_list[0]    
#date_list = dates.date2num(dates_list[0].now())
#print date_list

#print dates,temps

plt.plot(dates,temps)
#plt.plot(dates,temps)
#plt.scatter(dates, temps)
#plt.plot_date(dates, temps)
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)




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