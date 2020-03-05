from led import Led
import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase #thu vien firebase

import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()



#khai bao firebase
firebase = firebase.FirebaseApplication('https://vdkproject-43421.firebaseio.com/', None)
#firebase.put("/dht", "/temp", "0.00")
#firebase.put("/dht", "/humidity", "0.00"
def update_firebase():
    

while True:
        update_firebase()

        #sleepTime = int(sleepTime)
        sleep(5) #update every 5 seconds

