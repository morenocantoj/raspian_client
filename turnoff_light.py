#!/usr/bin/env python

#import RPi.GPIO as GPIO
import argparse
import constants

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, help="Numero de puerto del dispositivo",)

if port:
    if port in constants.GPIO_PORTS:
        print("Desactivación de puerto GPIO ", port)
        # Activate port
        #GPIO.setmode(GPIO.BCM)

        #GPIO.setup(port, GPIO.OUT)
        #GPIO.output(port, False)
    else:
        print("Puerto no válido, usa uno de los siguientes: ", constants.GPIO_PORTS)
else:
    print("¡Debes poner un puerto GPIO!")
