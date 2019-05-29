import RPi.GPIO as GPIO
import spidev
from time import sleep

"""
It works with Raspbian OS,
Hardware should be: 
-Raspberry Pi 2
-Raspberry Pi 3B
-Raspberry Pi 3B+
-Raspberry Pi Zero W
-Raspberry Pi 3 A+
"""

__author__ = "pe2a"
__license__ = "GPL"

RASP_DIG_IN_1 = 6 #PIN NO 31 OF RASPBERRY PI
RASP_DIG_IN_2 = 13  #PIN NO 33 OF RASPBERRY PI
RASP_DIG_R_OUT_1 = 19 #PIN NO 35 OF RASPBERRY PI
RASP_DIG_R_OUT_2 = 16 #PIN NO 36 OF RASPBERRY PI
RASP_DIG_tr_OUT_1 = 21 #PIN NO 40 OF RASPBERRY PI
RASP_DIG_tr_OUT_2 = 20 #PIN 38 OF RASPBERRY PI
RASP_DIG_tr_LED_1 = 26 #PIN 37 OF RASPBERRY PI

#initial function Raspberry Pi GPIO 
def __myGPIOInit__():

    #init function
    GPIO.setmode(GPIO.BCM) #bcm library
    #for digital inputs
    GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    GPIO.setup(RASP_DIG_R_OUT_1,GPIO.OUT)
    GPIO.setup(RASP_DIG_R_OUT_2,GPIO.OUT)
    GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
    GPIO.setup(RASP_DIG_tr_OUT_2,GPIO.OUT)
    GPIO.setup(RASP_DIG_tr_LED_1,GPIO.OUT)

    GPIO.setwarnings(False)

stIOVal = {

    0: RASP_DIG_R_OUT_1,
    1: RASP_DIG_R_OUT_2,
    2: RASP_DIG_tr_OUT_1,
    3: RASP_DIG_tr_OUT_2,
    4: RASP_DIG_tr_LED_1
}

class miniIOEx():
    def __init__(self):
        #IO decleration

        #definition SPI parameter
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 7629

        #definition Analog Input Var. 
        self.AI_5VpowerSupply = 0
        self.AI_24VpowerSupply = 0

        self.AI_ANIN1 = 0
        self.AI_ANIN2 = 0


        __myGPIOInit__()

 
    #ANALOG INPUT START
    #MiniIOEx has 12 bit ADC and the inputs work between 0-33V 
    #mcp3208 ADC
    def rpi_readAI(self,ch):
            if 7 <= ch <= 0:
                raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

            cmd = 128  # 1000 0000
            cmd += 64  # 1100 0000
            cmd += ((ch & 0x07) << 3)
            ret = self.spi.xfer2([cmd, 0x0, 0x0])

            # get the 12b out of the return
            val = (ret[0] & 0x01) << 11  # only B11 is here
            val |= ret[1] << 3           # B10:B3
            val |= ret[2] >> 5           # MSB has B2:B0 ... need to move down to LSB

            return (val & 0x0FFF)  # ensure we are only sending 12b

    #converts digital number to voltage
    def rpi_dig_vol_converter(self,val):
        return val*33.0/4095.0


    #5V Power Supply
    def ps5V(self):
        return self.rpi_dig_vol_converter(self.rpi_readAI(6))

    #24V Power Supply
    def ps24V(self):
        return self.rpi_dig_vol_converter(self.rpi_readAI(7))
     #ANALOG INPUT FINISH

    def setDO(self,ch,val = False):

        if ch == RASP_DIG_R_OUT_1:
           
            if val == True:
                GPIO.output(RASP_DIG_R_OUT_1, GPIO.HIGH)  # will be ON
            else:
                GPIO.output(RASP_DIG_R_OUT_1, GPIO.LOW)  # will be OFF
              
        elif ch == RASP_DIG_R_OUT_2:
             if val == True:
                GPIO.output(RASP_DIG_R_OUT_2, GPIO.HIGH)  # will be ON
             else:
                GPIO.output(RASP_DIG_R_OUT_2, GPIO.LOW)  # will be OFF
   
        elif ch == RASP_DIG_tr_OUT_1:
             if val == True:
                GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)  # will be ON
             else:
                GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)  # will be OFF
     
        elif ch == RASP_DIG_tr_OUT_2:
             if val == True:
                GPIO.output(RASP_DIG_tr_OUT_2, GPIO.HIGH)  # will be ON
             else:
                GPIO.output(RASP_DIG_tr_OUT_2, GPIO.LOW)  # will be OFF
                  
        elif ch == RASP_DIG_tr_LED_1:
             if val == True:
                GPIO.output(RASP_DIG_tr_LED_1, GPIO.HIGH)  # will be ON
             else:
                GPIO.output(RASP_DIG_tr_LED_1, GPIO.LOW)  # will be OFF

    def getDI(self,ch):

           #Digital Input
        if ch == RASP_DIG_IN_1:

            if GPIO.input(RASP_DIG_IN_1):
                return False
            else:
                return True
                           #Digital Input
        elif ch == RASP_DIG_IN_2:

            if GPIO.input(RASP_DIG_IN_2):
               
                return False
            else:
                return True
    
    def testDO(self):

        for i in range(2):
                
            for i in range(5):
                GPIO.output(stIOVal[i], GPIO.HIGH)  # will be ON
                sleep(0.250) #250ms
                GPIO.output(stIOVal[i], GPIO.LOW)  # will be ON
                sleep(0.25) #250ms



