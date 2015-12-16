#!/usr/bin/env python

#TODO Metodo de parsing
from parser import parser
from menu import TestApp 
import urllib2, NFC, menu, thread, buttons, sys, os, curses, npyscreen, sys

class Controller:
	def __init__(self):
		self.datos = None
	def run(self):
		os.system('clear')
		print "Acerque la targeta de la universidad al lector."
		nfc = NFC.NFC()
		# Bucle hasta la lectura de una targeta
		while True:
			#response = urllib2.urlopen('http://raiblax.com/pbe/receptor.php?id_alumno=FB68CCF1')
			response = nfc.read('http://raiblax.com/pbe/receptor.php?id_alumno=')
			if response != None: 
				break;
		# Creacion del entorno grafico 
		Menu = TestApp(parser(response),self).run()
	
	# Vuelta al estado inicial
	def stop(self):
		self.run()
if __name__ == "__main__":
    ctrl = Controller()
    try:
    	# Creacion del thread encargado de leer los pins de los botones
    	bd = thread.start_new_thread( buttons_daemon, ("Buttons", 100))
    except:
    	print "Error: unable to start the button daemon"
    ctrl.run()
