#!/usr/bin/env python3

import RPi.GPIO as GPIO
import constants

def engage(port):
	print("Port %s" % port)
	if port:
		GPIO.setwarnings(False)
		
		if port in constants.GPIO_PORTS:
			int_port = int(port.strip("'"))
			print("Activación de puerto GPIO ", port)
			# Activate port
			GPIO.setmode(GPIO.BCM)

			GPIO.setup(int_port, GPIO.OUT)
			GPIO.output(int_port, True)
		else:
			print("Puerto no válido, usa uno de los siguientes: ", constants.GPIO_PORTS)
	else:
		print("¡Debes poner un puerto GPIO!")
