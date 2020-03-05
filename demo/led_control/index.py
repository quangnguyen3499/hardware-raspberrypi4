from led import Led
import time as time

#define all pin numbers for leds
#ID for each rooms
led_id = {
    "LIVINGROOM":17,
    "WC":27,
    "BATHROOM":22,
    "KITCHEN":5,
    "LBEDROOM":23,
    "SBEDROOM":24,
    "BACONY":25,
    "GARAGE":16
}
print("1:LIVINGROOM\n2:WC\n3:BATHROOM\n4:KITCHEN\n5:LBEDROOM\n6:SBEDROOM\n7:BACONY\n8:GARAGE\nPlease choose led number: ")
id = int(input())
def number(id):
        switcher = {
            1:'LIVINGROOM',
            2:'WC',
            3:'BATHROOM',
            4:'KITCHEN',
            5:'LBEDROOM',
            6:'SBEDROOM',
            7:'BACONY',
            8:'GARAGE'
            }
        return switcher.get(id, "out of list")

Ledcontrol = Led(led_id[number(id)])
Ledcontrol.setLedOn()
time.sleep(1)
Ledcontrol.setLedOff()