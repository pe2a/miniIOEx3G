#Digital Output Test

import RPi.GPIO as GPIO
import time
import random 

DO_Relay1 = 21 #relay1 1A,24VDC
DO_Relay2 = 20 #relay2 1A,24VDC
DO_Mosfet1 = 19 #mosfet 2A,5VDC
DO_Mosfet2 = 16 #mosfet, 2A,5VDC
DO_RunLed = 26 #RunLED on PCB 

#init function
GPIO.setmode(GPIO.BCM) #bcm library

GPIO.setup(DO_Relay1,GPIO.OUT)
GPIO.setup(DO_Relay2,GPIO.OUT)
GPIO.setup(DO_Mosfet1,GPIO.OUT) #LOW'da ON, HIGH'da OFF
GPIO.setup(DO_Mosfet2,GPIO.OUT) #LOW'da ON, HIGH'da OFF
GPIO.setup(DO_RunLed,GPIO.OUT)

GPIO.setwarnings(False)

while (1):
	
	
	
	#led 
	GPIO.output(DO_RunLed,GPIO.HIGH) #ON
	time.sleep(0.2) #200ms
	GPIO.output(DO_RunLed,GPIO.LOW) #OFF
	time.sleep(0.2) #200ms
	
	#relay1 
	GPIO.output(DO_Relay1,GPIO.HIGH) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_Relay1,GPIO.LOW) 
	time.sleep(0.2) #200ms
	
	#relay2 
	GPIO.output(DO_Relay2,GPIO.HIGH) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_Relay2,GPIO.LOW) 
	time.sleep(0.2) #200ms
	
	#mosfet1 
	GPIO.output(DO_Mosfet1,GPIO.LOW) #ON
	time.sleep(0.2) #200ms
	GPIO.output(DO_Mosfet1,GPIO.HIGH) #OFF
	time.sleep(0.2) #200ms
	
	#mosfet2 
	GPIO.output(DO_Mosfet2,GPIO.LOW) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_Mosfet2,GPIO.HIGH) 
	time.sleep(0.2) #200ms
	


