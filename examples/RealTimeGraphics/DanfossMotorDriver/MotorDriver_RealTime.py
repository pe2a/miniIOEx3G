
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

#for modbus lib
import serial
import sys
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.exceptions import ModbusIOException, NotImplementedException
from pymodbus.exceptions import InvalidMessageReceivedException
from pymodbus.constants import Defaults


modbusReadDelayTime = 0.1 #sc


def fModbusDelayTime():
    time.sleep(modbusReadDelayTime)


motorConstantParameter = {
    
    
    "wrMotorSpeedRPM" : 0, #converted data 
    "r_motorDCLinkV" : 0,
    "r_motorPowerkW" : 0,
    "r_motorCurrentA" : 0,
    }

#motor register adress list
motorModbusParameter = {
    
    "motorID " : 0x1,
    "w_motorSpeedReq" : 2810,
    "r_motorDCLinkVReq" : 16299,
    "r_motorPowerkWReq" : 16099,
    "r_motorSpeedFreqReq": 16129,
    "r_motorCurrentAReq" : 16139,
    #"r_motorFreqPerReq" : 16149
    
    }

#sending motor speed
def sendMotorReference(motorSpeed_rpm):
    return (int(motorSpeed_rpm*(21.845/2.0)))


#calculation percent of requency of motor
def calculationPercentFreq(motorSpeedNumber):
    return (motorSpeedNumber / 32767.0*100.0)


client = ModbusClient(method = 'rtu',
                      port = '/dev/ttyS0',
                      baudrate = 9600,
                      timeout = 1,
                      parity = 'N',
                      stopbits = 1)

def motorStartConnect(connect = 0):

    try:

        if connect == 1:
            client.connect()
            rq = client.write_coils(1,[True]*6,unit=1) #motor start
        else:
            rq = client.write_coils(1,[False]*6,unit=1) #motor stop
            client.close()
    except ModbusIOException as e:
        print(e)
         

def readMotorParameter(showPrint = 0):

    #motor parameter read
    try:

            rq = client.read_holding_registers(motorModbusParameter["r_motorDCLinkVReq"],1,unit = 1)
            motorConstantParameter["r_motorDCLinkV"] = rq.registers[0] #V
            fModbusDelayTime()
            #kw
            rq1 = client.read_holding_registers(motorModbusParameter["r_motorPowerkWReq"],1,unit = 1)
            motorConstantParameter["r_motorPowerkW"] = rq1.registers[0] /1000.0 #kW
            fModbusDelayTime()
            #rpm
            rq2 = client.read_holding_registers(motorModbusParameter["r_motorSpeedFreqReq"],1,unit = 1)
            motorConstantParameter["wrMotorSpeedRPM"] = rq2.registers[0]*30.0/10.0 #1Hz = 30rpm , 50Hz = 1500rpm
            fModbusDelayTime()
            #A
            rq3 = client.read_holding_registers(motorModbusParameter["r_motorCurrentAReq"],1,unit = 1)
            motorConstantParameter["r_motorCurrentA"] = rq3.registers[0] /100.0
            fModbusDelayTime()

            if showPrint == 1:
                printMotorParameter()
            else:
                pass

    except (ModbusIOException) as e:
        print(e)

def printMotorParameter():
    print(motorConstantParameter)

def wrSendSpeedRef(motorSpeedRef):#rpm

    try:

        if motorSpeedRef >= 1500: #rpm
            motorSpeedRef = 1500
        rq = client.write_registers(motorModbusParameter["w_motorSpeedReq"],sendMotorReference(motorSpeedRef),unit = 1)
    except (ModbusIOException) as e:
            print(e)

def fMotorProcess(motorRefSpeed):

    
  
    
    try:

            #print("{} : {} ".format(readMotorParameter(1),datetime.datetime.now()))
            wrSendSpeedRef(motorRefSpeed)

    except (ModbusIOException)as e:
            print(e)



#GLOBAL VARIABLE

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
       
        #UP button
       self.up = Image.open("./pics/up.png")
       self.photoImg_up = ImageTk.PhotoImage(self.up)
       buttonUp = tk.Button(self, image=self.photoImg_up,
            text="optional text" ,command=self.upSpeed).place(x=20,y=150)
       
        #Down button
       self.down = Image.open("./pics/down.png")
       self.photoImg_down = ImageTk.PhotoImage(self.down)
       buttonDown = tk.Button(self, image=self.photoImg_down,
            text="optional text" ,command=self.downSpeed).place(x=20,y=195)
       
       #Stop Button
       self.stop = Image.open("./pics/stop.png")
       self.photoImg_stop = ImageTk.PhotoImage(self.stop)
       buttonStopSpeed = tk.Button(self, image=self.photoImg_stop,
            text="optional text" ,command=self.stopSpeed).place(x=20,y=245)

       #verilerin kayit edilmesi
       self.tTimer = [] #time Counter
       self.iCounter  = 0
       self.tMotorSpeed = [] #Real Motor Speed 
       self.tMotorSpeedRef = [] #Motor Speed Ref
       
       self.motorSpeedRef = 0 #Motor Speed Ref

       self.xSide = []
       self.ySide_1 = []
       self.ySide_2 = []
       
    #motor Speed Increase as rpm  
   def upSpeed(self):
       self.motorSpeedRef+=30
       
    #motor Speed Decrease as rpm
   def downSpeed(self):
      
       self.motorSpeedRef-=30
       
       if self.motorSpeedRef < 0:
           self.motorSpeedRef = 0
       
    #motorStop   
   def stopSpeed(self):
       self.motorSpeedRef=0
      


   def fMotorControl(self):
       
        motorStartConnect(1)
        fMotorProcess(self.motorSpeedRef)
        
        self.lbl = tk.Label(self,text = "Ref Speed:"+str(self.motorSpeedRef)+"rpm").place(x=0,y=80)
        self.lbl = tk.Label(self,text = "Speed:"+str(motorConstantParameter["wrMotorSpeedRPM"])+"rpm").place(x=0,y=95)
        
        #reading motor parameter on terminal      
        readMotorParameter(1)
            
         

   def fsave_to_Charts(self):
        
       
        self.iCounter+=1 
        #time
     
        self.tTimer.append(self.iCounter)
        self.tMotorSpeed.append(motorConstantParameter["wrMotorSpeedRPM"])
        self.tMotorSpeedRef.append(self.motorSpeedRef)


        for i in range(len(self.tTimer)):

            self.xSide.append(self.tTimer[i])
            self.ySide_1.append(self.tMotorSpeed[i])
            self.ySide_2.append(self.tMotorSpeedRef[i]) 
        
        #Motor Speed and Motor Speed Ref
        self.fig.add_subplot(111).plot(self.xSide,self.ySide_1,self.ySide_2)
     
        
        self.fig.suptitle("AC Motor Speed Real Time Charts via Modbus RTU")
        self.canvas.draw()
        self.fig.clf()
        #verilerin temizlenmesi
        self.tTimer.clear()
        self.tMotorSpeed.clear()
        self.tMotorSpeedRef.clear()


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

        
        #help button
        self.cloud = Image.open("./pics/help.png")
        self.photoImg_cloud = ImageTk.PhotoImage(self.cloud)
        buttonCloud = tk.Button(buttonframe, image=self.photoImg_cloud,
            text="optional text" ,command=pCloud.lift)


        buttonCharts.pack(side="left", fill="both", expand=True)
        buttonCloud.pack(side = "left",fill = "both",expand = True)

        self.pCharts.show()
        self.fEmbeddedCall()

 
    def fEmbeddedCall(self):
        self.pCharts.fMotorControl()
        self.pCharts.fsave_to_Charts()
		
        #100ms cycle time		
        self.after(100,self.fEmbeddedCall)

    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x800")
    #root.attributes("-fullscreen",True)
   
    root.mainloop()
  

