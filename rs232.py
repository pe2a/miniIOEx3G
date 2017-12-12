import serial
import os,time


#for raspberry 3 
port = serial.Serial('/dev/ttyS0',baudrate = 115200,timeout=1)

#for raspberry 2
#port = serial.Serial('/dev/ttyAMA0',baudrate = 115200,timeout=1)

port.write('hello world'+'\r\n')
time.sleep(2)
port.write('pe2a.com'+'\r\n')
time.sleep(2)
