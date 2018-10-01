# -*- coding: utf-8 -*-

import sys

reload(sys)  
sys.setdefaultencoding('utf8')

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.network.urlrequest import UrlRequest
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.popup import Popup
from kivy.uix.image import Image, AsyncImage
from kivy.cache import Cache

import requests
import json
import time
import datetime
import random

global config
data = {'hora_feeder': 10800,'motor': {'scheduled': True, 'ligar': True,'hora_config':{'hora':0,'min':0,'sun':True,'mon':True,'tue':True,'wed':True,'thu':True,'fri':True,'sat':True,'duration':60}}}

#data = {'motor': {'scheduled': True, 'ligar': True,'hora_min':0.0},'hora_feeder':10800}
'''
Toda vez que se muda dados contidos no arquivo json, é necessário mudar:
- os dois arquivos config.json, no cliente(kivy) e no servidor(rpi)
- função chave motor, que contem uma cópia de data(json arq)
  -importante - usa-se a variàvel estado para mudar o estado do motor, que deixa de ser o inicial True 
'''

''' definições '''
global url 
#url = "http://10.10.0.1:4000/"

url = "http://192.168.0.109:4000/"


config = json.dumps(data)
#print config
#config = json.loads(config)
#print config
config = data



class ComandosJavatrap(BoxLayout):
    #global config
    carrega_config = ObjectProperty()
    #print est_motor

    
    def para_rpi(self):
        print 'teste'
        
    def atualiza_config_rpi(self):
        global config
        global url
        '''
        A função inicializa o objeto response que conecta no rpi chamando a função config do rpi
        esta função config retorna um dict em response['result'] que é passado para config
        
        '''
        self.ids['swi2'].active = False
        #self.ids['swi1'].active = False

        """ laço para garantir que o motor seja desligado caso o usuàrio clique nas configurações novamente"""
        if self.ids['swi1'].active == True:
            config['motor']['ligar'] = False
            self.liga_motor(**config)
            
          
        
        #print 'o botão está funcionando'
        #url = "http://192.168.0.102:4000/"
    #url = "http://javatrap1:4000/"
        headers = {'content-type': 'application/json'}

        payload = {
        "method": "config",
        #"params":None,
        "jsonrpc": "2.0",
        "id": 1,
        }
        response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
        #print response['result']['motor']
        print 'a var config contém antes: ',config['motor']['ligar']
        # a configuração que está no feeder é passada para a var config
        config = response['result']
        print 'a var config contém depois: ',config['motor']['ligar']
        active = self.ids['swi1']
        active.active = config['motor']['ligar']
        
        swi2 = self.ids['swi2']
        swi2.active = config['motor']['scheduled']
                
        
        active2 = self.ids['hora_feeder']
        time_tuple =  time.localtime(config['hora_feeder'])        
        active2.text = time.strftime('%H:%M',time_tuple)
        
       
        hora_c = self.ids['hora']
        hora_c.text = str(config['motor']['hora_config']['hora'])+':'+str(config['motor']['hora_config']['min'])

        duracao_c = self.ids['du']
        duracao_c.text = str(config['motor']['hora_config']['duration'])
        
        self.ids['sld1'].value = config['motor']['hora_config']['hora']
        self.ids['sld2'].value = config['motor']['hora_config']['min']
        self.ids['sld3'].value = config['motor']['hora_config']['duration']
        
        self.ids['cb_dom'].active = config['motor']['hora_config']['sun']
        self.ids['cb_seg'].active = config['motor']['hora_config']['mon'] 
        self.ids['cb_ter'].active = config['motor']['hora_config']['tue']
        self.ids['cb_qua'].active = config['motor']['hora_config']['wed']
        self.ids['cb_qui'].active = config['motor']['hora_config']['thu']
        self.ids['cb_sex'].active = config['motor']['hora_config']['fri']
        self.ids['cb_sab'].active = config['motor']['hora_config']['sat']
        
        #data = datetime.date
        #print data.
        print 'A configuração carregada na var. config é : ', config 
        
    def relogio_feeder(self):
        global config
        time_tuple =  time.localtime(config['hora_feeder'])        
        print "esperança"
        #return time.strftime('%H:%M',time_tuple)
        
    
        
    def muda_config(self,**kwargs):
        
        global config  
        global url
        
        #print 'o valor de **kargs é: ',kwargs
        #print 'apenas o valor da con figuração do motor: ',config['motor'] 
    #print 'o botão está funcionando'
        #url = "http://192.168.0.102:4000/"
    #url = "http://javatrap1:4000/"
        headers = {'content-type': 'application/json'}

        payload = {
        "method": "muda_config",
        #"params": {'motor': False},
        "params": kwargs,    
        "jsonrpc": "2.0",
        "id": 2,
        }
        response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
        #print config
        #print response
        #return True
     #   self.est_motor = True
        #global config
        
        #return True
    def testa_motor(self,**kwargs):
        global config
        global url
        
        #print 'o valor de **kargs é: ',kwargs
        #print 'apenas o valor da con figuração do motor: ',config['motor'] 
    #print 'o botão está funcionando'
        #url = "http://192.168.0.102:4000/"
    #url = "http://javatrap1:4000/"
        headers = {'content-type': 'application/json'}

        payload = {
        "method": "testa_motor",
        #"params": {'motor': False},
        "params": kwargs,    
        "jsonrpc": "2.0",
        "id": 2,
        }
        response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
        
        
        
    def chave_motor(self):
        global config

        #print type(self.ids['swi1'].active)
        #print type(config['motor'])
        if self.ids['swi1'].active != config['motor']['ligar']:
            config['motor']['ligar'] = self.ids['swi1'].active  
            estado = self.ids['swi1'].active
            print 'O estado é : ',estado
            
            #self.muda_config({'motor': estado}) 
            #self.muda_config(**{"motor": estado})
            #data = {'motor': {'scheduled': True, 'ligar': True,'hora_min':0.0}}
            #self.muda_config(**{'motor': {'scheduled': True, 'ligar': estado,'hora_min':0.0}})
            
            # Para mudar a configuração deve-se chamar a função muda_config(**kgwards)
            # passando a python dict que contém a configuração ( toda ela) com uma variável no lugar do que se quer mudar
            
            #self.muda_config(**{"hora_feeder": 10800,'motor': {'scheduled': True, 'ligar': estado,'hora_config':{'hora':0,'min':0,'sun':True,'mon':True,'tue':True,'wed':True,'thu':True,'fri':True,'sat':True,'duration':60}}})
            #print self.ids['swi1'].active
            self.testa_motor(**config)
    def agenda_funcionamento(self):        
        global config
        
        if self.ids['swi2'].active != config['motor']['scheduled']:
            config['motor']['scheduled'] = self.ids['swi2'].active  

            scheduled = self.ids['swi2'].active
            hora = self.ids['sld1'].value
            minutos = self.ids['sld2'].value
            duration = self.ids['sld3'].value
            sun = self.ids['cb_dom'].active
            mon = self.ids['cb_seg'].active
            tue = self.ids['cb_ter'].active
            wed = self.ids['cb_qua'].active
            thu = self.ids['cb_qui'].active
            fri = self.ids['cb_sex'].active
            sat = self.ids['cb_sab'].active        
            
            '''
            print 'O valor de sld1(hora) é  : ', hora
            print 'O valor de sld2(minutos) é  : ', minutos
            print 'O valor de sld3(duração) é  : ', duration
            print 'O valor de sld3(duração) é  : ', sun,mon,tue,wed,thu,fri,sat
            ################################
            '''
            
            config['motor']['scheduled'] = scheduled
            config['motor']['hora_config']['hora'] = hora 
            config['motor']['hora_config']['min'] = minutos
            config['motor']['hora_config']['duration'] = duration        
            config['motor']['hora_config']['sun'] = sun
            config['motor']['hora_config']['mon'] = mon
            config['motor']['hora_config']['tue'] = tue
            config['motor']['hora_config']['wed'] = wed
            config['motor']['hora_config']['thu'] = thu
            config['motor']['hora_config']['fri'] = fri
            config['motor']['hora_config']['sat'] = sat
            
        #chamo a função muda_config(**kwargs) para mudar a configuração do feeder
        self.muda_config(**config)
        
        
    def cancela_funcionamento(self):        
        global config
        if self.ids['swi2'].active == True:
            config['motor']['scheduled'] = False
            
        self.muda_config(**config)
            
    def pop1(self):
        global url
        #pass
        #pop = Popup(title='camera', content=AsyncImage(source="http://www.ninjaducks.in/images/duck.png"),size_hint=(None, None), size=(400, 400))
        #Image.reload()
        
        Cache.remove('kv.asyncimage')
        Cache.remove('kv.texture')
        #Image.remove_from_cache()
        #Image.reload()
        #img = AsyncImage(source="http://192.168.0.102:5000/img2/"+str(random.randrange(0, 101, 2)))
        img = AsyncImage(source=url[:-5]+"5000/img2/"+str(random.randrange(0, 101, 2)))
        pop = Popup(title='camera', content=img,size_hint=(1, 1))
        #Image.remove_from_cache()
        #size=(400, 400)
        pop.open()         
            
            
            
            
            
            
#            if self.ids['swi2'].active != config['motor']['scheduled']:
#                config['motor']['scheduled'] = self.ids['swi2'].active  
#    
#                scheduled = self.ids['swi2'].active
#                hora = self.ids['sld1'].value
#                minutos = self.ids['sld2'].value
#                duration = self.ids['sld3'].value
#                sun = self.ids['cb_dom'].active
#                mon = self.ids['cb_seg'].active
#                tue = self.ids['cb_ter'].active
#                wed = self.ids['cb_qua'].active
#                thu = self.ids['cb_qui'].active
#                fri = self.ids['cb_sex'].active
#                sat = self.ids['cb_sab'].active        
#                
#                '''
#                print 'O valor de sld1(hora) é  : ', hora
#                print 'O valor de sld2(minutos) é  : ', minutos
#                print 'O valor de sld3(duração) é  : ', duration
#                print 'O valor de sld3(duração) é  : ', sun,mon,tue,wed,thu,fri,sat
#                ################################
#                '''
#                
#                config['motor']['scheduled'] = scheduled
#                config['motor']['hora_config']['hora'] = hora 
#                config['motor']['hora_config']['min'] = minutos
#                config['motor']['hora_config']['duration'] = duration        
#                config['motor']['hora_config']['sun'] = sun
#                config['motor']['hora_config']['mon'] = mon
#                config['motor']['hora_config']['tue'] = tue
#                config['motor']['hora_config']['wed'] = wed
#                config['motor']['hora_config']['thu'] = thu
#                config['motor']['hora_config']['fri'] = fri
#                config['motor']['hora_config']['sat'] = sat        
#                # chamo a função muda_config(**kwargs) para mudar a configuração do feeder
#                self.muda_config(**config)
#            
    
    
class frontendApp(App):
    def build(self):
        return ComandosJavatrap()
                        
        
if __name__ == '__main__':
    frontendApp().run()


#AddLocationForm:
#<AddLocationForm@BoxLayout>:
