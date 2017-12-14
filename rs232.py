import serial
import os,time

#REENGEN RS232
#for raspberry 3 
port = serial.Serial('/dev/ttyS0',baudrate = 115200,timeout=1)

#for raspberry 2
#port = serial.Serial('/dev/ttyAMA0',baudrate = 115200,timeout=1)

RASP232_SELECT = 20
RASP485_SELECT = 21

#init function
GPIO.setmode(GPIO.BCM) #bcm library

GPIO.output(RASP232_SELECT,GPIO.HIGH) #will be OFF
GPIO.output(RASP485_SELECT,GPIO.HIGH)
time.sleep(0.2)
print ("RS232 OK, RS485 NOT OK")
GPIO.output(RASP232_SELECT,GPIO.LOW) #will be ON
GPIO.output(RASP485_SELECT,GPIO.HIGH) #will be ON


while(1):
        
    print ("RS232 WRITE")
    time.sleep(0.2)
    port.write('RS232'+'\r\n')
    time.sleep(2)
    port.write('pe2a.com'+'\r\n')
    time.sleep(2)

    print ("RS232 READ")
    line = '\0'
    line  = port.read(1024)
    print(line)
        
    time.sleep(1)
    print ('\n')