import Adafruit_DHT as Ada
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def abc():
    dht_sensor=Adafruit_DHT.DHT11
    DHT_PIN=23  
    while True:
        humidity, temperature = Ada.read_retry(dht_sensor, DHT_PIN)
        print ("Humidity: " + str(humidity) + ", Temperature: " + str(temperature))
        time.sleep(1)
abc()