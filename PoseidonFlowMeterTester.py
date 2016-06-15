#
# Poseidon Project GrovePi
# 
#	Tester for the Water Flow when pumping. 
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
pompPin = 3   				 # pomp-relais op grovepi D3

#### SET PIN MODE
grovepi.pinMode(pompPin, "OUTPUT")

#Min - Max for moisture
moistureDry =1023.0	#0%
moistureWet=438.0	#100%
moistureTreshold=40.0 #water if lower than 40%
readingIntervalMinutes=15 #number of minutes between readings
wateringTimeSeconds=1 #number of seconds the plant should be watered if the treshold is low. 


def activateWater():
	grovepi.digitalWrite(pompPin, 1)

def passivateWater():
    grovepi.digitalWrite(pompPin, 0)

def waterPlant():
	#Start Flow meter
	grovepi.flowEnable()
	[new_val,flow_val] = grovepi.flowRead()
	print(new_val)
	print(flow_val)
	activateWater()
	time.sleep(2) #water for 1 second
	passivateWater()
	[new_val,flow_val] = grovepi.flowRead()
	print(new_val)
	print(flow_val)
	grovepi.flowDisable()


def readMoisture():
	moisture = grovepi.analogRead(moisture_sensor)
	print "Moisture " + str(moisture)
	moisturePercentage = (moistureDry-moisture)/(moistureDry-moistureWet)*100
	print "Moisture Percentage " + str(moisturePercentage)
	return moisturePercentage

try:
	while True:
		moisture = readMoisture()
		if moisture < moistureTreshold:
			waterPlant() #water the plant

		time.sleep(60*readingIntervalMinutes) #read every 15 minutes
except:
	print "unexpected error", sys.exc_info()
finally:
	print "shutting down pump" #make sure the pump is closed when something crashes
	passivateWater()
	grovepi.flowDisable()
