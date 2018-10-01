# -*- coding: utf-8 -*-
'''
 - inplementa a função gettemp que abre o arquivo gerado peo termometro e lê dentro dele a temperatura
 - se a função retornar o valor 99999 é porque não foi possível a leitura da temperatura
'''
import config

def gettemp():
  try:
    mytemp = ''
    filename = 'w1_slave'
    #f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    f = open(config.device_file,'r')
    line = f.readline() # read 1st line
    #print line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
      
    else:
      mytemp = 99999
    f.close()
 
    return int(mytemp[1])/float(1000)
 
  except:
    return 99999
 
if __name__ == '__main__':
 
  # Script has been called
   id = '28-0517c0c0c9ff'
   #print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
   print gettemp(id)