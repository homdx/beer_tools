# -*- coding: utf-8 -*-

def gettemp(id = '28-0517c0c0c9ff'):
  try:
    mytemp = ''
    filename = 'w1_slave'
    #f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    f = open('/home/daniel/workspaces/cerverja/termometro_ios/' + id + '/' + filename, 'r')
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