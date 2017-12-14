import serial
import os,time



port = serial.Serial('/dev/ttyUSB2',baudrate = 115200,timeout=1)

port.write('ATI'+'\r\n')
time.sleep(1)
port.write('AT+CPIN?'+'\r\n')
time.sleep(1)
port.write('AT+CREG?'+'\r\n')
time.sleep(1)
port.write('AT+CSQ'+'\r\n')
time.sleep(1)
port.write('AT+COPS?'+'\r\n')
time.sleep(1)


