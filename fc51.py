#author: pe2a
#company: pe2a.com
#Danfos FC51 Motor Modbus Sample - 051218

import serial
import sys
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.exceptions import ModbusIOException, NotImplementedException
from pymodbus.exceptions import InvalidMessageReceivedException
from pymodbus.constants import Defaults
import time
import datetime
import RPi.GPIO as GPIO
import threading


modbusReadDelayTime = 0.01 #sc

#miniioex lib.
#start
DO_Relay1 = 19 #relay1 1A,24VDC
DO_Relay2 = 16 #relay2 1A,24VDC
DO_TR1 = 21 #TRANSISTOR 2A,5VDC
DO_TR2 = 20 #TRANSISTOR, 2A,5VDC
DO_RunLed = 26 #RunLED on PCB 

#definition GPIO
RASP_DIG_IN_1 = 6   #DI_1
RASP_DIG_IN_2 = 13  #DI_2

#init function
#https://github.com/pe2a/miniIOEx3G/blob/master/README.md#digital-output
GPIO.setmode(GPIO.BCM) #bcm library
 
GPIO.setup(DO_Relay1,GPIO.OUT)
GPIO.setup(DO_Relay2,GPIO.OUT)
GPIO.setup(DO_TR1,GPIO.OUT) #LOW ON, HIGH OFF
GPIO.setup(DO_TR2,GPIO.OUT) #LOW ON, HIGH OFF
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DO_RunLed,GPIO.OUT)


GPIO.setwarnings(False)
#finish

def fLed():
    #it means a program running on OS
    
    while 1:
        GPIO.output(DO_RunLed,GPIO.HIGH) #ON
        time.sleep(0.2) #200ms
        GPIO.output(DO_RunLed,GPIO.LOW) #OFF
        time.sleep(0.2) #200ms

      
   

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

#def motorSpeed_kmh(motorSpeedRpm): #km/h converting
  #  r = 0.8 #wheel meter
   # return r*motorSpeedRpm*0.10472


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
    except ModbusIOException:
        pass
         

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

    except (ModbusIOException):
        pass
   

def printMotorParameter():
    print(motorConstantParameter)


def wrSendSpeedRef(motorSpeedRef):#rpm

    try:

        if motorSpeedRef >= 1500: #rpm
            motorSpeedRef = 1500
        rq = client.write_registers(motorModbusParameter["w_motorSpeedReq"],sendMotorReference(motorSpeedRef),unit = 1)
    except (ModbusIOException):
            pass

def fMotorProcess(motorRefSpeed):

    
    motorStartConnect(1)
    
    try:

            print("{} : {} ".format(readMotorParameter(1),datetime.datetime.now()))
            wrSendSpeedRef(motorRefSpeed)

    except (AttributeError):
            pass

        
def motorRun():
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)

    motorSpeed = 0
    bStatusMotorProcess = False

    while 1:

        DI_In1 = not GPIO.input(RASP_DIG_IN_1)
        DI_In2 = not GPIO.input(RASP_DIG_IN_2)

        if DI_In1 and DI_In2:
            time.sleep(0.5)
            motorSpeed+=100
            fMotorProcess(motorSpeed)
  
            if motorSpeed >= 1500: #max. speed
                motorSpeed = 750

        if not DI_In2:
            bStatusMotorProcess = False
            fMotorProcess(0)
            motorSpeed = 0
        time.sleep(0.01)

#led or IO function
t1 = threading.Thread(target=fLed, args=[])
t1.start()
t2 = threading.Thread(target=motorRun,args=[])
t2.start()

#if you need to run a program for every reboot
#just add /etc./rc.local
#sample: sudo python3 /etc/rc.local/myProgram.py &
    
    
           
   
    

