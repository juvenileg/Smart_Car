import RPi.GPIO as GPIO # Importa libraria GPIO
from time import sleep
#from sys import argv  #ignoram argumentele deoarece au fost folosite doar ca test
#whichled = argv[1]
#ledaction = argv[2]
GPIO.setwarnings(False) # Ignora alarme GPIO
GPIO.setmode(GPIO.BCM) # Folosim valoarea pinilor BCM
PIN_LIGHT = 21
PIN_LIGHTS = 20 #Trebuie mutat pe pin 20 cand termin luminile
GPIO.setup(PIN_LIGHT, GPIO.OUT) #, initial=GPIO.LOW) # Setam valoarea initiala a pinului 40 cu low
GPIO.setup(PIN_LIGHTS, GPIO.OUT) #, initial=GPIO.LOW) # Setam valoarea initiala a pinului 39 cu low


def procesare(a):
        if a == 0:
                GPIO.output(PIN_LIGHT, 0) # Opreste lumini
        else:
                GPIO.output(PIN_LIGHT, 1) # Porneste lumini 3.3 pe pinul 40

def aprinde(a):
        if (a % 2) == 0:
                GPIO.output(PIN_LIGHTS, 0) # Opreste lumini
        else:
                GPIO.output(PIN_LIGHTS, 1) # Porneste lumini 3.3 pe pinul 40

def danger(a):
        while a<6: # Ruleaza in bucla de 6 ori
                GPIO.output(PIN_LIGHT, GPIO.HIGH) # Turn on
                sleep(0.3) # sleep 0.3 secunde
                GPIO.output(PIN_LIGHT, GPIO.LOW) # Turn off
                sleep(0.3) # sleep 0.3 secunde
                a += 1

procesare(0)

