# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:14:46 2018

@author: daniel
"""

import RPi.GPIO as GPIO


def liga_geladeira():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)       
    
def desliga_geladeira():
    
    GPIO.output(23,GPIO.LOW)
    GPIO.cleanup()
