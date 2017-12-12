#input IO test
from firebase import firebase
import RPi.GPIO as GPIO
import time
import random 

DI_In1 = 6
DI_In2 = 13

#init function
GPIO.setmode(GPIO.BCM) #bcm library

GPIO.setup(DI_In1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DI_In2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(False)

while (1):
	
	
	print ("INPUT TEST START")
	
	#input 
	if GPIO.input(DI_In1)== GPIO.HIGH:
		print("DI_In1 -> HIGH")
	else:
                print("DI_In1 -> LOW")
                
		
	#input 
	if GPIO.input(DI_In2)== GPIO.HIGH:
		print("DI_In2 -> HIGH")
	else:
                print("DI_In2 -> LOW")
                
	 		
        print ("INPUT TEST FINISH")

        time.sleep(2)
