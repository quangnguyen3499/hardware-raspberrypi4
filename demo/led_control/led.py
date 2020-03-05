import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Led:
    def __init__(self, ID):
        self.ID = ID
        self.status = False
        GPIO.setup(ID,GPIO.OUT)

    def getID(self):
        return self.ID

    def getStatus(self):
        return self.status

    def setLedOn(self):
        self.Status = True
        GPIO.output(self.ID,GPIO.HIGH)

    def setLedOff(self):
        self.status = False
        GPIO.output(self.ID,GPIO.LOW)
        