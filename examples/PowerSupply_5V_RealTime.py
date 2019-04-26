
#Raspberry Pi IO library
import RPi.GPIO as GPIO
import spidev
#Python3 Library
import tkinter as tk
import time
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#sudo pip3 install matplotlib
#sudo apt-get install python3-pil.imagetk

#GLOBAL VARIABLE
#xAxis
iCounter  = 0

#definition Analog Input Var. 
AI_5VpowerSupply = 0

#SPI must be ENABLED from Raspberry Pi Configuration(raspi-config)
#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629


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


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class pgCharts(Page):
   def __init__(self, *args, **kwargs):

       Page.__init__(self, *args, **kwargs)

       self.fig = Figure(figsize=(5, 4), dpi=100)
       self.fig.patch.set_facecolor('grey')

       self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
       self.canvas.draw()
       self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

       self.toolbar = NavigationToolbar2Tk(self.canvas, self)
       self.toolbar.update()
       self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

       #verilerin kayit edilmesi
       self.tTimer = [] #time Counter
       self.t5V = [] #5V 
       #self.t24V = [] #24V

       self.xSide = []
       self.ySide_1 = []
       #self.ySide_2 = []


    
   def fsave_to_Charts(self):
        #saving sensor data
        global iCounter
        global AI_5VpowerSupply

        AI_5VpowerSupply = rpi_dig_vol_converter(rpi_readAI(6))
        AI_24VpowerSupply = rpi_dig_vol_converter(rpi_readAI(7))
        

        iCounter+=1 
        #time
     
      
        self.tTimer.append(iCounter)
        self.t5V.append(AI_5VpowerSupply)
        #self.t24V.append(AI_24VpowerSupply)


        for i in range(len(self.tTimer)):

            self.xSide.append(self.tTimer[i])
            self.ySide_1.append(self.t5V[i])
            #self.ySide_2.append(self.t3[i]) for 24V



        self.fig.add_subplot(111).plot(self.xSide,self.ySide_1)
        #for 5V and 24V
        #self.fig.add_subplot(111).plot(self.xSide,self.ySide_1,self.ySide_2)
     
        
        self.fig.suptitle("5VDC Voltage Real Time Charts")
        self.canvas.draw()
        self.fig.clf()
        #verilerin temizlenmesi
        self.tTimer.clear()
        self.t5V.clear()




#cloud page 
class pgCloud(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
   

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


        self.pCharts = pgCharts(self)
        pCloud = pgCloud(self)
   
      
        buttonframe = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        #placing charts page
        self.pCharts.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pCloud.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


         #charts button
        self.charts = Image.open("./pics/charts.png")
        self.photoImg_charts = ImageTk.PhotoImage(self.charts)
        buttonCharts = tk.Button(buttonframe, image=self.photoImg_charts,
            text="optional text" ,command=self.pCharts.lift)

        
        #cloud button
        self.cloud = Image.open("./pics/help.png")
        self.photoImg_cloud = ImageTk.PhotoImage(self.cloud)
        buttonCloud = tk.Button(buttonframe, image=self.photoImg_cloud,
            text="optional text" ,command=pCloud.lift)


        buttonCharts.pack(side="left", fill="both", expand=True)
        buttonCloud.pack(side = "left",fill = "both",expand = True)

        self.pCharts.show()
        self.fEmbeddedCall()

 
    def fEmbeddedCall(self):

        #anlık grafiklerin gosterilmesi
        self.pCharts.fsave_to_Charts()
        self.after(1000,self.fEmbeddedCall)

    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x400")
    #root.attributes("-fullscreen",True)
   
    root.mainloop()
  

