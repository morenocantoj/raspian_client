#!/usr/bin/env python3

import RPi.GPIO as GPIO
import argparse
import constants

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, help="Numero de puerto del dispositivo",)

args = parser.parse_args()
port = args.port

if port:
    GPIO.setwarnings(False)
    
    if port in constants.GPIO_PORTS:
        print("Activación de puerto GPIO ", port)
        # Activate port
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, True)
    else:
        print("Puerto no válido, usa uno de los siguientes: ", constants.GPIO_PORTS)
else:
    print("¡Debes poner un puerto GPIO!")
