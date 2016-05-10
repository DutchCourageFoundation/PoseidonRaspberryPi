#
# Poseidon Project GrovePi Sensor Calibration
# 
#	Read the data from Soil-Moisture sensor for Calibration purposes
# 	
#
#	Loop every X minutes, to see whether the water is still above the treshold
#
#	2016. Robert-Jan Sips, IBM / Dutch Courage Foundation
#
import sys
import time
import grovepi
import subprocess
import math

#analog sensor port number
moisture_sensor			= 1  # moisture-sensor op grovepi A1

#Min - Max for moisture
readingIntervalSeconds=10 #number of minutes between readings
wateringTimeSeconds=1 #number of seconds the plant should be watered if the treshold is low. 

def readMoisture():
	moisture = grovepi.analogRead(moisture_sensor)
	print "Moisture " + str(moisture)
	return moisture


while True:
	moisture = readMoisture()
	time.sleep(readingIntervalSeconds) #read every 15 minutes
