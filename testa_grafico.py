# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:21:27 2018

@author: daniel
"""
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import config
import sqlite3


# make up some data
x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]


#myFmt = mdates.DateFormatter('%d')



conn = sqlite3.connect(config.db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)




plt.plot(x,y)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
#plt.close()