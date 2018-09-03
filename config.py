# -*- coding: utf-8 -*-
"""
@author: daniel

Arquivo de configuração para todo o sistema do aplicativo de produção de cerveja versão 0.1

"""
import os
import glob

# intervalo de tempo em segundo entre coleta de temperatura 
intervalo = 60

intervalo_geladeira = 300 #1800 #  = 30 minutos
temperatura_alvo = 24
delta_temperatura = 2 

temperatura_alvo = float(temperatura_alvo)
delta_temperatura = float(delta_temperatura)

# porta do server_side 
porta_server_side = 4000

id = '28-0517c0c0c9ff'   # number of da18b20 sensor

# path dir - diretório onde está instalado o programa
c_path = '/home/daniel/workspaces/serrazul/geo/version_2/'
img_path = '/home/daniel/workspaces/serrazul/geo/version_2/images/'
db_path = '/home/daniel/workspaces/cerverja/termometro_ios/cerveja.db'

path = os.path.abspath(c_path)

base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#print glob.glob(base_dir + '28*')
#print glob.glob(base_dir+)


device_file = base_dir + id + '/w1_slave'



#db_path = os.path.join(os.getcwd(),'cerveja.db')
db_path = '/home/cerveja/beer_tools/cerveja.db'

