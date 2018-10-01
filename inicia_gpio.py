# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 06:31:10 2018

@author: daniel
"""
'''
As I noted gpio do not turn off when rpi is turn off, I have to clean the gpio on rpi starting 
'''

import RPi.GPIO as GPIO


GPIO.cleanup()