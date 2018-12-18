#Raspberry Pi Power Supply Datalogger
# Author : pe2a
#18.12.2018 Rev0

import matplotlib
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
import spidev
import datetime


#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629

#definition Analog Input Var. 
AI_5VpowerSupply = 0
AI_24VpowerSupply = 0

#mcp3208 ADC
def rpi_readAI(ch):
		if 7 <= ch <= 0:
			raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

		cmd = 128  # 1000 0000
		cmd += 64  # 1100 0000
		cmd += ((ch & 0x07) << 3)
		ret = spi.xfer2([cmd, 0x0, 0x0])

		# get the 12b out of the return
		val = (ret[0] & 0x01) << 11  # only B11 is here
		val |= ret[1] << 3           # B10:B3
		val |= ret[2] >> 5           # MSB has B2:B0 ... need to move down to LSB

		return (val & 0x0FFF)  # ensure we are only sending 12b

#converts digital number to voltage
def rpi_dig_vol_converter(val):
	return val*33.0/4095.0

#init function
GPIO.setmode(GPIO.BCM) #bcm library
GPIO.setwarnings(False)

# Data for plotting
tTime = []
#Raspberry Pi Feed Voltage
arrRPIVoltage = []
#Battery Voltage
arrBatterVoltage = []

#file Name
strFileName = ""


counter = 0

while counter < 60:
       counter+=1
       #time function
       tTime.append(datetime.datetime.now())
       #analog function
       arrRPIVoltage.append(round(rpi_dig_vol_converter(rpi_readAI(6)),2))
       arrBatterVoltage.append(round(rpi_dig_vol_converter(rpi_readAI(7)),2))
       time.sleep(10)


plt.subplot(2, 1, 1)

plt.plot(tTime, arrRPIVoltage, 'o-')

plt.title('Power Supply Graphics 10min')
plt.ylabel('Raspberry Pi Voltage ')

plt.subplot(2, 1, 2)
plt.plot(tTime, arrBatterVoltage, '.-')
plt.xlabel('time (s)')
plt.ylabel('Battery Voltage')

strFileName = "/home/pi/Desktop/"+"PowerSupply"+str(datetime.datetime.now())+".png" 

plt.savefig(strFileName)
plt.show()

