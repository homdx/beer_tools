# -*- coding: utf-8 -*-
"""
@author: daniel

Arquivo de configuração para todo o sistema do aplicativo de produção de cerveja versão 0.1

"""
import os

# intervalo de tempo em segundo entre coleta de temperatura 
intervalo = 5

# porta do server_side 
porta_server_side = 6003

# path dir - diretório onde está instalado o programa
c_path = '/home/daniel/workspaces/serrazul/geo/version_2/'
img_path = '/home/daniel/workspaces/serrazul/geo/version_2/images/'
db_path = '/home/daniel/workspaces/cerverja/termometro_ios/cerveja.db'

path = os.path.abspath(c_path)

