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

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')


import matplotlib.pyplot as plt
import matplotlib.dates as dates
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas


import dados_para_grafico



class Controle(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Controle, self).__init__(*args, **kwargs)
        self.add_plot()
        

    def get_fc(self, i):
        hfmt = dates.DateFormatter('%H:%M') #usa matplotlib.dates para formatar o eixo com as datas 
        
        fig1 = plt.figure() #figura normal do matplotlib
        fig1.suptitle('temperatura interna ')
        #ax1 = fig1.add_subplot(211)
        #ax2 = fig1.add_subplot(212)
        ax = fig1.add_subplot(111)
        datas,temps = dados_para_grafico.fetch_intern_temp()
        ax.plot_date(datas,temps)        
        ax.xaxis.set_major_formatter(hfmt)
        plt.setp(ax.get_xticklabels(), rotation=30)
        
        wid = FigureCanvas(fig1) #acho que é aqui que a mágica do kivy.garden acontece
        
        return wid

    def add_plot(self):
        self.add_widget(self.get_fc(1))
        #self.add_widget(self.get_fc(2))

    #pass


class frontendApp(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''

    def build(self):
        return Controle()
        #return Label()
    def on_pause(self):
        return True


if __name__ == "__main__":
    frontendApp().run()