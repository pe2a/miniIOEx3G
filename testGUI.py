import tkinter as tk
import RPi.GPIO as GPIO
import time
import spidev


#IO DECLERATION
RASP_DIG_IN_1 = 6 #PIN NO 31 OF RASPBERRY PI
RASP_DIG_IN_2 = 13  #PIN NO 33 OF RASPBERRY PI
RASP_DIG_R_OUT_1 = 19 #PIN NO 35 OF RASPBERRY PI
RASP_DIG_R_OUT_2 = 16 #PIN NO 36 OF RASPBERRY PI
RASP_DIG_tr_OUT_1 = 21 #PIN NO 40 OF RASPBERRY PI
RASP_DIG_tr_OUT_2 = 20 #PIN 38 OF RASPBERRY PI
RASP_DIG_tr_LED_1 = 26 #PIN 37 OF RASPBERRY PI

#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629

#definition Analog Input Var. 
AI_5VpowerSupply = 0
AI_24VpowerSupply = 0

AI_ANIN1 = 0
AI_ANIN2 = 0

myCounter = 0

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

#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(RASP_DIG_R_OUT_1,GPIO.OUT)
GPIO.setup(RASP_DIG_R_OUT_2,GPIO.OUT)
GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
GPIO.setup(RASP_DIG_tr_OUT_2,GPIO.OUT)
GPIO.setup(RASP_DIG_tr_LED_1,GPIO.OUT)

GPIO.setwarnings(False)


class Root(tk.Tk):

    def __init__(self,tasks = None):
        super().__init__()
        

        self.title = ("pe2a Test IO Program")
        self.geometry("250x500")

        self.rDO_1_label = tk.Label(self, text="Relay 1")
        self.rDO_1_entry = tk.Entry(self, bg="white", fg="black")
        self.rDO_2_label = tk.Label(self, text="Relay 2")
        self.rDO_2_entry = tk.Entry(self, bg="white", fg="black")
        self.trDO_1_label = tk.Label(self, text="Tr Out 1")
        self.trDO_1_entry = tk.Entry(self, bg="white", fg="black")
        self.trDO_2_label = tk.Label(self, text="Tr Out 2")
        self.trDO_2_entry = tk.Entry(self, bg="white", fg="black")
        self.trLED_label = tk.Label(self, text="LED")
        self.trLED_entry = tk.Entry(self, bg="white", fg="black")

        #Analog Input
        self.AI_1_label = tk.Label(self, text="Analog Input AI_1")
        self.AI_1_entry = tk.Label(self, text="0")

        self.AI_2_label = tk.Label(self, text="Analog Input AI_2")
        self.AI_2_entry = tk.Label(self, text="0")

        self.AI_3_label = tk.Label(self, text="[5V] Analog Input AI_3")
        self.AI_3_entry = tk.Label(self, text="0")

        self.AI_4_label = tk.Label(self, text="[24V] Analog Input AI_4")
        self.AI_4_entry = tk.Label(self, text="0")
        
        self.DI_1_label = tk.Label(self, text="Digital Input DI_1")
        self.DI_1_entry = tk.Label(self, text="0")
        
        self.DI_2_label = tk.Label(self, text="Digital Input DI_2")
        self.DI_2_entry = tk.Label(self, text="0")


        self.submit_button = tk.Button(self,text = "Submit",command = self.submit)

        self.rDO_1_label.pack(fill=tk.BOTH, expand=3)
        self.rDO_1_entry.pack(fill=tk.BOTH, expand=3)
        self.rDO_2_label.pack(fill=tk.BOTH, expand=3)
        self.rDO_2_entry.pack(fill=tk.BOTH, expand=3)
        self.trDO_1_label.pack(fill=tk.BOTH, expand=3)
        self.trDO_1_entry.pack(fill=tk.BOTH, expand=3)
        self.trDO_2_label.pack(fill=tk.BOTH, expand=3)
        self.trDO_2_entry.pack(fill=tk.BOTH, expand=3)
        self.trLED_label.pack(fill=tk.BOTH, expand=3)
        self.trLED_entry.pack(fill=tk.BOTH, expand=3)
        
        #Digital Input
        self.DI_1_label.pack(fill=tk.BOTH, expand=3)
        self.DI_1_entry.pack(fill=tk.BOTH, expand=3)
        
        self.DI_2_label.pack(fill=tk.BOTH, expand=3)
        self.DI_2_entry.pack(fill=tk.BOTH, expand=3)

        #Analog Input
        self.AI_1_label.pack(fill=tk.BOTH, expand=3)
        self.AI_1_entry.pack(fill=tk.BOTH, expand=3)
        self.AI_2_label.pack(fill=tk.BOTH, expand=3)
        self.AI_2_entry.pack(fill=tk.BOTH, expand=3)
        self.AI_3_label.pack(fill=tk.BOTH, expand=3)
        self.AI_3_entry.pack(fill=tk.BOTH, expand=3)
        self.AI_4_label.pack(fill=tk.BOTH, expand=3)
        self.AI_4_entry.pack(fill=tk.BOTH, expand=3)
        
       

        self.submit_button.pack(fill = tk.X)
        
        
        self.fGPIOUpdate()
        
        #4DO,2DI,4AI = 10

    def submit(self):
        strDig_IO_1 = self.rDO_1_entry.get()
        strDig_IO_2 = self.rDO_2_entry.get()
        strDig_IO_3 = self.trDO_1_entry.get()
        strDig_IO_4 = self.trDO_2_entry.get()
        strDig_IO_5 = self.trDO_2_entry.get()

        self.rpi_GPIO_set()
	
    def fGPIOUpdate(self):
        #update every 1000ms
        
        #Analog Input
        strAI1 = str(rpi_readAI(0)) + ' Dig. Number  ' + str(round(rpi_dig_vol_converter(rpi_readAI(0)),2)) + ' [V]' 
        self.AI_1_entry.config(text = strAI1,font=("Consolas", 12,"bold"))
        strAI2 = str(rpi_readAI(1)) + ' Dig. Number  ' + str(round(rpi_dig_vol_converter(rpi_readAI(1)),2)) + ' [V]' 
        self.AI_2_entry.config(text = strAI2,font=("Consolas", 12,"bold"))
        strAI3 = str(rpi_readAI(6)) + ' Dig. Number  ' + str(round(rpi_dig_vol_converter(rpi_readAI(6)),2)) + ' [V]' 
        self.AI_3_entry.config(text = strAI3,font=("Consolas", 12,"bold"))
        strAI4 = str(rpi_readAI(7)) + ' Dig. Number  ' + str(round(rpi_dig_vol_converter(rpi_readAI(7)),2)) + ' [V]' 
        self.AI_4_entry.config(text = strAI4,font=("Consolas", 12,"bold"))
        
        #Digital Input
        if GPIO.input(RASP_DIG_IN_1):
            strDI1 = str(0)
        else:
            strDI1 = str(1)
            
        #Digital Input
        if GPIO.input(RASP_DIG_IN_2):
            strDI2 = str(0)
        else:
            strDI2 = str(1)
            
        
        self.DI_1_entry.config(text = strDI1,font=("Consolas", 12,"bold"))
        self.DI_2_entry.config(text = strDI2,font=("Consolas", 12,"bold"))
        
       
        
        
        self.after(1000, self.fGPIOUpdate)
       
	
    def rpi_GPIO_set(self):

        if (self.rDO_1_entry.get() == '1'):
            GPIO.output(RASP_DIG_R_OUT_1, GPIO.HIGH)  # will be ON
        else:
            GPIO.output(RASP_DIG_R_OUT_1, GPIO.LOW)  # will be OFF

        if (self.rDO_2_entry.get() == '1'):
            GPIO.output(RASP_DIG_R_OUT_2, GPIO.HIGH)  # will be ON
        else:
            GPIO.output(RASP_DIG_R_OUT_2, GPIO.LOW)  # will be OFF

        if (self.trDO_1_entry.get() == '1'):
            GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)  # will be ON
        else:
            GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)  # will be OFF

        if (self.trDO_2_entry.get() == '1'):
            GPIO.output(RASP_DIG_tr_OUT_2, GPIO.HIGH)  # will be ON
        else:
            GPIO.output(RASP_DIG_tr_OUT_2, GPIO.LOW)  # will be OFF

        if (self.trLED_entry.get() == '1'):
            GPIO.output(RASP_DIG_tr_LED_1, GPIO.HIGH)  # will be ON
        else:
            GPIO.output(RASP_DIG_tr_LED_1, GPIO.LOW)  # will be OFF
            
       
        
       
            
       



if __name__ == "__main__":
    root = Root()
    root.mainloop()



