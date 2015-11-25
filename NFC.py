#!/usr/bin/python

import os, sys, time                             
sys.path.insert(1, os.path.split(sys.path[0])[0])
                                                                           
import re                                                                  
import time                                                                
import errno
import argparse                                  
import logging                                   
logging.basicConfig(format='%(relativeCreated)d ms [%(name)s] %(message)s')
                                                                           
import nfc                                                                 
import nfc.clf                                                             
import urllib2

class NFC():
	def read(self,web):
        # Seleccion de la interfaz con la que se leera la tarjeta
		clf = nfc.ContactlessFrontend("usb")                     
        # Seleccion del objetivo de la lectura
		target1 = nfc.clf.RemoteTarget("106A")          
		str2 = str(clf.sense(target1, iterations=100, interval=0.5))[13:21]
        # Request al servidor web de los datos del alumno
		response = urllib2.urlopen(web+str2)
	   	clf.close()
		return (response, str2)
