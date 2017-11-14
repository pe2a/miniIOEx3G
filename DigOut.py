import RPi.GPIO as GPIO
import time 

#MiniIOEx-3G Using GPIO Sample 
#Digital Output Usage
#chmod +x DigOut.py
#to Run the script : python DigOut.py
#do not hesitate to contact with support@pe2a.com

def all_gpio_low():
	
	GPIO.output(DO_Relay1,GPIO.LOW)
	GPIO.output(DO_Relay2,GPIO.LOW)
	GPIO.output(DO_RunLed,GPIO.LOW)
	GPIO.output(DO_Mosfet1,GPIO.HIGH)
	GPIO.output(DO_Mosfet2,GPIO.HIGH)

counter = 3 #number of repeat
time_delay = 0.5

DO_Relay1 = 21 #relay1 1A,24VDC
DO_Relay2 = 20 #relay2 1A,24VDC
DO_Mosfet1 = 19 #mosfet 2A,5VDC
DO_Mosfet2 = 16 #mosfet, 2A,5VDC
DO_RunLed = 26 #RunLED on PCB 


#init function
GPIO.setmode(GPIO.BCM) #bcm library

GPIO.setup(DO_Relay1,GPIO.OUT)
GPIO.setup(DO_Relay2,GPIO.OUT)
GPIO.setup(DO_Mosfet1,GPIO.OUT)
GPIO.setup(DO_Mosfet2,GPIO.OUT)
GPIO.setup(DO_RunLed,GPIO.OUT)


#for safety reason 
all_gpio_low()

while counter:
	
	
	print("\nDigital Output will be Test\n")
	#relay will be ON/OFF
	GPIO.output(DO_Relay1,GPIO.HIGH) #will be ON
	time.sleep(time_delay)
	GPIO.output(DO_Relay1,GPIO.LOW)   #will be OFF
	time.sleep(time_delay)
	
		
	GPIO.output(DO_Relay2,GPIO.HIGH) #will be ON
	time.sleep(time_delay)
	GPIO.output(DO_Relay2,GPIO.LOW)  #will be OFF
	time.sleep(1)
	
	#LED will be ON/OFF
	GPIO.output(DO_RunLed,GPIO.HIGH) #will be ON
	time.sleep(time_delay)
	GPIO.output(DO_RunLed,GPIO.LOW)  #will be OFF
	time.sleep(1)
	
	#MOSFET Digital Output will be ON/OFF
	GPIO.output(DO_Mosfet1,GPIO.LOW) #will be ON - pnp 
	time.sleep(time_delay)
	GPIO.output(DO_Mosfet1,GPIO.HIGH)  #will be OFF
	time.sleep(1)
	
	GPIO.output(DO_Mosfet2,GPIO.LOW) #will be ON - pnp
	time.sleep(time_delay)
	GPIO.output(DO_Mosfet2,GPIO.HIGH)  #will be OFF
	time.sleep(1)
	
	counter = counter - 1
	 

#for safety reason 
all_gpio_low()

