import serial
import os,time

#GPS SAMPLE CODE 
#UC20 module and MiniIOEx Raspberry Shield will be used 


port = serial.Serial('/dev/ttyUSB2',baudrate = 115200,timeout=1)



port.write('AT+QGPSGNMEA=?'+'\r\n')
time.sleep(2)
port.write('AT+QGPSGNMEA?'+'\r\n')
time.sleep(2)
port.write('AT+QGPSGNMEA="GGA"'+'\r\n')
time.sleep(2)


port.write('AT+QGPS=1'+'\r\n')
time.sleep(3)
port.write('AT+QGPS=?'+'\r\n')
time.sleep(1)
port.write('AT+QGPS?'+'\r\n')
time.sleep(1)

port.write('AT+GPRMC'+'\r\n')
time.sleep(3)

port.write('AT+QGPSLOC=?'+'\r\n')
time.sleep(1)

while(1):
    
   
    port.write('AT+QGPSLOC=1'+'\r\n')
  
    line = '\0'
    line  = port.read(1024)
    print(line)
    
    
    time.sleep(1)
    print ('\n')





port.write('AT+QGPSEND'+'\r\n') #gps stop - NEVER USED for this code
time.sleep(1)





